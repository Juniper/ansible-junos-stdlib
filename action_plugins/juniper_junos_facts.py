import os.path
import sys

module_utils_path = os.path.normpath(os.path.dirname(__file__) + '/../module_utils')

if module_utils_path is not None:
    sys.path.insert(0,module_utils_path)
    import juniper_junos_common
    del sys.path[0]

from juniper_junos_common import JuniperJunosActionModule as ActionModule
