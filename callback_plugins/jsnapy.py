
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import collections
import os
import time
import pprint
import json

from ansible.plugins.callback import CallbackBase
from ansible import constants as C

class CallbackModule(CallbackBase):
  """
  This callback add extra logging for the module junos_jsnapy .
  """
  CALLBACK_VERSION = 2.0
  CALLBACK_TYPE = 'aggregate'
  CALLBACK_NAME = 'jsnapy'

## useful links regarding Callback
## https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/callback/__init__.py

  def __init__(self):
    self._pp = pprint.PrettyPrinter(indent=4)
    self._results = {}

    super(CallbackModule, self).__init__()

  def v2_runner_on_ok(self, result):
    """
    Collect test results for all tests executed if module is junos_jsnapy
    """

    ## Extract module name
    module_name = ''
    module_args = {}
    if 'invocation' in result._result:
      if 'module_name' in result._result['invocation']:
        module_name = result._result['invocation']['module_name']
        module_args = result._result['invocation']['module_args']

    ## Check if dic return has all valid information
    if module_name == '' or module_args == {}:
        return None
    elif not module_args.has_key('action'):
        return None

    if module_name == 'junos_jsnapy' and \
    ( module_args['action'] == 'snapcheck' or module_args['action'] == 'check' ):

      ## Check if dict entry already exist for this host
      host = result._host.name
      if not host in self._results.keys():
        self._results[host] = []

      self._results[host].append(result)

  def v2_playbook_on_stats(self, stats):

    ## Go over all results for all hosts
    for host, results in self._results.iteritems():
      has_printed_banner = False
      for result in results:
        # self._pp.pprint(result.__dict__)
        res = result._result
        if res['final_result'] == "Failed":
          for test_name, test_results in res['test_results'].iteritems():
            for testlet in test_results:
              if testlet['count']['fail'] != 0:

                if not has_printed_banner:
                  self._display.banner("JSNAPy Results for: " + str(host))
                  has_printed_banner = True

                for test in testlet['failed']:

                  # Check if POST exist in the response
                  data = ''
                  if test.has_key('post'):
                      data = test['post']
                  else:
                      data = test

                  self._display.display(
                    "Value of '{0}' not '{1}' at '{2}' with {3}".format(
                      str(testlet['node_name']),
                      str(testlet['testoperation']),
                      str(testlet['xpath']),
                      json.dumps(data)),
                    color=C.COLOR_ERROR)
