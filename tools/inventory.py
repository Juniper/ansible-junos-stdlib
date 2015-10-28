#!/usr/bin/env python
# inventory.py
# by Jason Pack for Juniper Networks
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

import requests
import json
from xml.etree.ElementTree import XML
import sys
import os

def retrieve(url, user, password, postData=None, headers={}):
  '''Retrieve some HTTP-accessible resource.'''
  returnVal = None
  if "https://" not in url:
    url =  "https://" + url
  r = None
  sys.stderr.write("Requesting %s..\n" % url);
  if postData is None:
    r = requests.get(url, verify=False, auth=(user, password), headers=headers)
  else:
    r = requests.post(url, verify=False, auth=(user, password), headers=headers, data=postData)
  if r.status_code!=200 and r.status_code!=204:
    raise Exception("Got status code %d while retrieving %s!\n" % (r.status_code, url))
  return r.content

def xmlize(content):
  '''Attempt to convert something to XML. otherwise return none.'''
  try:
    return XML(content)
  except:
    return None

class Space:
  def __init__(self, config_filename='junos_space.json'):
    self.config_filename = config_filename
    self.loadConfig()
    
  def loadConfig(self):
    ''' 
    loads the JSON-formatted config file.
    Config file must contain data for all of the following keys:
    ['SPACE_HOST','SPACE_USER','SPACE_PASSWORD']
    '''
    filename  = os.path.join( os.getcwd() , self.config_filename)
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
    self.host = config['SPACE_HOST']
    self.user = config['SPACE_USER']    
    self.password = config['SPACE_PASSWORD']
    self.devices = None
    self.domains = None
    
  def getDevices(self):
    '''Return the devices managed by this Space instance.'''
    if self.devices is None:
      self.updateDevices()
    return self.devices
    
  def getDomains(self):
    '''Return the domains managed by this Space instance.'''
    if self.domains is None:
      self.updateDomains()
    return self.domains
  def updateDomains(self, domain_id=2):
    '''Get info about all domains managed by the Space instance.'''
    url = "https://" + self.host + "/api/space/domain-management/domains/" + str(domain_id)
    data = retrieve(url, user=self.user, password=self.password);
    domains = {}
    xml = xmlize(data)
    if xml is None:
      return domains
    name = xml.find('name').text
    id = xml.find('id').text
    new_domain = {}
    new_domain['id'] = id
    new_domain['name'] = name
    domains[id] = new_domain
    if xml.find('child-count') is not None:
      if int(xml.find('child-count').text) > 0:
        for i in xml.findall('children/domain'):
          child_id = i.find('id').text
          if int(i.find('child-count').text) > 0:
            #babies havin babies
            children = self.updateDomains(domain_id = child_id)
            domains.update(children)
        else:
            new_domain = {}
            new_domain['id'] = child_id
            new_domain['name'] = i.find('name').text
            domains[child_id]  = new_domain
    self.domains = domains
    return domains

  def updateDevices(self, device_filter=None):
    '''Get info about all devices managed by the Space instance.'''
    domains  = self.getDomains()
    devices = {}
    if device_filter is None:
        for d_id in domains.keys():
            new_devices = self.updateDevices( device_filter="(domain-id eq '" + d_id + "')")
            for (dev_id, device) in new_devices.items():
                device['domain_id'] = d_id
            devices.update(new_devices)
        return devices;
    url = "https://" + self.host + "/api/space/device-management/devices?filter=" + device_filter + "&"
    pageOffset = 0;
    pageMax = 1000;
    xmlDevs = [];
    numDevices = 9999
    while pageOffset < numDevices:
      #print "%d is less than %d" % (pageOffset, numDevices)
      theseDevs = retrieve(url + "paging=(start eq "+str(pageOffset)+", limit eq "+str(pageMax)+ ")",user=self.user, password=self.password);
      theseDevs = xmlize(theseDevs)
      if theseDevs is None:
          break
      xmlDevs = xmlDevs + theseDevs.getchildren()
      pageOffset = pageOffset + pageMax
    for xml in xmlDevs:
      platform = xml.find('platform')
      if (platform is None):
        sys.stderr.write("%s: Unable to determine platform.  It will not be included in inventory.\n" % xml.find('name').text)
        continue;
      version = xml.find('OSVersion')
      if version is None:
        sys.stderr.write("%s: Unable to determine Junos version.  It will not be included in inventory.\n" % xml.find('name').text)
        continue;
      ip = xml.find('ipAddr')
      if ip is None:
        sys.stderr.write("%s: Unable to determine IP address. It will not be included in inventory.\n" % xml.find('name').text)
        continue;
      devId = xml.get('key')
      device = {'name'  :  xml.find('name').text,
                'id'    :  devId,
                'platform':  platform.text,
                'version'  :  version.text,
                'ip'      :  ip.text}
      devices[devId] = device
    self.devices = devices
    return devices;  
def export(devices):
  ''' 
  Creates ansible host entries for the given device objects
  Expects the devices to have the 'name' attribute.
  All the device's attributes are added as metavars.
  '''
  data = {    "_meta"  :  {
      "hostvars" : {}
    }
  }
  for (id, device) in devices.items():
    data[device['name']] = [device['ip']]
    data["_meta"]["hostvars"][device["name"]] = device
  data = json.dumps(data)
  return data
  	

if __name__ == "__main__":
	space = Space()
	devs = space.getDevices()
	data = export(devs)
	sys.stdout.write(data)
	sys.stdout.flush()
