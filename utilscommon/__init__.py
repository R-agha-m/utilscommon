try:
    from utilscommon import logo
    from utilscommon.setting import *
    from utilscommon.exception import *
    from utilscommon.file_and_dir import *
    from utilscommon.is_test_mode import is_test_mode

except ImportError:
    from utilscommon.utilscommon import logo
    from utilscommon.utilscommon.setting import *
    from utilscommon.utilscommon.exception import *
    from utilscommon.utilscommon.file_and_dir import *
    from utilscommon.utilscommon.is_test_mode import is_test_mode



