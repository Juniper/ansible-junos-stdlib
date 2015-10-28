#!/usr/bin/env python
# inventory.py
# returns the list of devices managed by Space as an inventory for Ansible.


#Here's global variables so all the functions can use them.  

import requests
import json
from xml.etree.ElementTree import XML
import sys
import os

#dev-only.
import sys
from pprint import pprint as pp
requests.packages.urllib3.disable_warnings() #disable insecure request warnings from urllib3.
def retrieve(url, user, password, postData=None, headers={}):
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
    try:
        return XML(content)
    except:
        return None

class Space:
  def __init__(self, config_filename='junos_space.json'):
    self.config_filename = config_filename
    self.loadConfig()
  def loadConfig(self):
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
    
  def getDomains(self, domain_id=2):
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
                      children = self.getDomains(domain_id = child_id)
                      domains.update(children)
                  else:
                      new_domain = {}
                      new_domain['id'] = child_id
                      new_domain['name'] = i.find('name').text
                      domains[child_id]  = new_domain
      self.domains = domains
      return domains

  def getDevices(self, device_filter=None):
      if self.domains is None:
          domains  = self.getDomains()
      devices = {}
      if device_filter is None:
          for d_id in domains.keys():
              new_devices = self.getDevices( device_filter="(domain-id eq '" + d_id + "')")
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
if __name__ == "__main__":
    # load config from space.ini
    space = Space()
    devs = space.getDevices()
    print "There were %d devices" % len(devs.keys())

