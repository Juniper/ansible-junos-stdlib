#!/usr/bin/env python
# inventory.py
# by Jason Pack for Juniper Networks 2015-2016
# returns the list of devices managed by Junos Space as an inventory for Ansible.

# To use this script, make sure that you place a file  containing Space credentials
# into the same directory as this script, and name it junos_space.json
# Look at junos_space_example.json for an example.


#================================#
#====== Lawyer stuffs below.=====#
#================================#
# Copyright (c) 1999-2015, Juniper Networks Inc.
#               2015, Jason Pack
#
# All rights reserved.
#
# License: Apache 2.0
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of the Juniper Networks nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Juniper Networks, Inc. ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Juniper Networks, Inc. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#================================#
#====== Lawyer stuffs above.=====#
#================================#

import optparse
import requests
import json
import sys
import os

class Space:
  def __init__(self, host, user, passwd):
   
   self.host = host;
   self.user = user
   self.passwd = passwd
   self._devices = []

  def _request(self, url, method='get', headers={}, postData=None,retries=0):
   '''
   Executes an arbitrary request against this Space instance. 
   '''
   if self.host not in url:
       if url[0] is not '/':
         url = "/%s" % url
       url =  "https://%s%s" % (self.host, url)
   if method=='get':
     retrieve = requests.get
   elif method=='post':
     retrieve = requests.post
   elif method=='put':
     retrieve = requests.put
   elif method=='delete':
     retrieve = requests.delete
   else:
     raise Exception("Invalid HTTP method %s requested in call to Space.request" % method);
   print "Requesting %s" % url
   r = retrieve(url, verify=False, auth=(self.user, self.passwd), headers=headers, data=postData)
   if r.status_code==204:
     # "No Content"
     return None
     #sys.stderr.write("Got status code 204 while retrieving %s!:\n%s" % (url, r.content))
   if r.status_code!=200:
     sys.stderr.write("Got status code %d while retrieving %s!:\n%s" % (r.status_code, url, r.content))
     sys.stderr.flush()
   try:
     return r.content
   except:
     sys.stderr.write("Couldn't get content from response for %s:\n%s" % (url, r.content))
     sys.stderr.flush()
     if retries==0:
       return None
     return self._request(url, method, headers, postData, retries-1)

  def getDevices(self):
    '''
    Retrieves the list of devices from Space. 
    '''
    if len(self._devices) > 0:
      return self._devices;
    url = "https://" + self.host + "/api/space/device-management/devices?"
    headers = {'Accept' : "application/vnd.net.juniper.space.device-management.devices+json;version=1"}
    devices = []
    pageOffset = 0;
    pageMax = 1000;
    theseDevs = 1;
    while theseDevs is not None:
     pagingUrl = url +  "paging=(start eq "+str(pageOffset)+", limit eq "+str(pageMax)+ ")"
     theseDevs = self._request(pagingUrl, 'get', headers)
     try:
       theseDevs = json.loads(theseDevs)
       theseDevs = theseDevs['devices']['device']
       devices = devices + theseDevs;
       pageOffset = pageOffset + pageMax;
     except:
       theseDevs = None
    for dev in devices:
     # clean hostnames because Space likes to include re[0|1]-
     for prefix in ['re0-','re1-']:
       if 'name' in dev.keys() and dev['name'][0:4] == prefix:
         dev['name'] = dev['name'][4:]
    self._devices = devices
    return devices;
  def exportJson(self):
    '''
    Creates ansible host entries for the given device objects
    Expects the devices to have the 'name' attribute.
    All the device's attributes are added as metavars.
    '''
    data = {    "_meta"  :  {
        "hostvars" : {}
      }
    }
    devices = self.getDevices()
    for device in devices:
      if 'name' in device.keys() and 'ipAddr' in device.keys():
        data[device['name']] = [device['ipAddr']]
        data["_meta"]["hostvars"][device["name"]] = device

    return data;


def parseArgs():
  '''
  Parses the arguments passed on the command line.
  '''
  parser = optparse.OptionParser()
  parser.add_option( '--host', dest="opt_host", action="store",)
  parser.add_option( '--list', dest="opt_list", action="store_true",)
  parser.add_option( '--config', dest="config_file", action="store", default="junos_space.json")
  options, remainder = parser.parse_args()
  return options
  
def loadConfig(filename):
  '''
  loads a JSON-formatted config file.
  Config file must contain data for all of the following keys:
  ['SPACE_HOST','SPACE_USER','SPACE_PASSWORD']
  '''
  filename  = os.path.join( os.path.dirname(os.path.abspath(__file__)) ,filename)
  
  #import the config file.
  try:
    fh = open(filename);
    text = fh.read()
    fh.close()
  except:
    sys.stderr.write("Problem opening config file %s.\n" % filename)
    sys.stderr.flush()
    exit(-1)
  try:
    config = json.loads(text)
  except:
    sys.stderr.write("Config file %s is not valid JSON.\n" % filename)
    sys.stderr.flush()
    exit(-1)

  #validate config
  necessary = [ 'SPACE_HOST','SPACE_USER','SPACE_PASSWORD']
  for i in necessary:
    if i not in config.keys():
      raise Exception("Config file %s is missing config value %s.\n" % (filename, i)) 
  return config;
  
if __name__ == "__main__":
  args = parseArgs()
  config = loadConfig(args.config_file)
  [host, user, password] = [ config['SPACE_HOST'], config['SPACE_USER'], config['SPACE_PASSWORD'] ]
  space = Space(host, user, password)
  space.getDevices()
  data = space.exportJson()
  if args.opt_hostj and args.opt_host in data['_meta']['hostvars'].keys():
    data = data['meta']['hostvars'][args.opt_host]
  data = json.dumps(data)
  sys.stdout.write(data)
  sys.stdout.flush()
