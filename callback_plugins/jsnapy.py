
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import collections
import os
import time
import pprint
import json

from ansible.plugins.callback import CallbackBase
from ansible import constants as C
'''
The JSNAPy result structure is constructed as follows:
{
  action: # one of: snap_pre, snap_post, snapcheck, check
  changed:
  final_result:
  msg:
  passPercentage:
  router:
  test_results: {
    test_rpc_or_cli_used: [
      {
        count: {
          fail: # number of entries in failed[]
          pass: # number of entries in passed[]
        }
        expected_note_value: # value expected of xpath node
        failed: [  # filled in if a test failed
                   # Failure can be test test condition was false
                   # or no valid data to test against.
          {
            actual_node_value:
            id: {} # if set in test definition
            message: "" # error message templated by test run 
                    # may be empty if test did not find valid data
                    # ex. an IS-IS test where IS-IS is not running
            post: {} # key/value pairs defined in test
            pre: {} # key/value pairs defined in test 
          }
          ... # {} repeated for number of tests that failed 
        ]
        node_name: # xpath test searched
        passed: [ # filled in if a test failed
          {
            actual_node_value:
            id: {} # if set in test definition
            message: "" # error message templated by test run 
            post: {} # key/value pairs defined in test
            pre: {} # key/value pairs defined in test 
          }
          ... # {} repeated for number of tests that passed
        ]
        result:
        test_name:
        testoperation:
        xpath:
      }
      ... # {} repeated for number of times this test executed
    ]
    ... # test key/value pair repeated for each test invoked
  }
}
'''
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
        callback = None
        # Get the callback from 'invocation' structure.
        res = result._result
        action = ''
        if 'invocation' in res:
          if 'module_args' in res['invocation']:
            if 'callback' in res['invocation']['module_args']:
              callback = res['invocation']['module_args']['callback']
            if 'action' in res['invocation']['module_args']:
              action = res['invocation']['module_args']['action']
        if action in ['check', 'snapcheck']:
          if callback is None:
              # self._pp.pprint(result.__dict__)
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
          else:
            self._display.banner("Results for: " + str(host), color=C.COLOR_VERBOSE )
            for test_name, test_results in res['test_results'].iteritems(): # test_name is cmd or rpc
                has_printed_banner = False
                if not has_printed_banner:
                  self._display.display(" -- Test: " + str(test_name))
                  has_printed_banner = True
                for testlet in test_results:
                  if callback == 'info':
                    self._display.display("\tResults for test: " + str(testlet['test_name']))
                    if testlet['count']['pass'] != 0:
                        for test in testlet['passed']:
                          if test['message'] is not None:
                            self._display.display( "\t\t'{0}'".format( str(test['message'])))
                         # With jsnapy 1.2 info field parsed into message for each passed test
                  if callback == 'error' or callback == 'info':
                    if testlet['count']['fail'] != 0:
                      self._display.display("\tErrors for test: " + str(testlet['test_name']))
                      for test in testlet['failed']:
                        if 'message' in test:
                          if test['message'] is not None:
                            self._display.display( "\t\t'{0}'".format( str(test['message'])),
                              color=C.COLOR_ERROR)
                            # With jsnapy 1.2 err field parsed into message for each failed test
                        else:
                          self._display.display( "\t\tTest failed without providing message.",
                            color=C.COLOR_ERROR)
    #self._display.display("Checking for callback value, in '{0}'".format(json.dumps(result)))
