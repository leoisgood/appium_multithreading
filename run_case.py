# TODO(Leo): 用多线程的方式启动Appium
# 根据设备启动信息，通过pytest.main来收集并执行用例。
import pytest
import os


def run_cases(device):
    """
  参数：device为设备启动参数。在pytest.main当中，传递给--cmdopt选项。
  """
    # reports_dir = os.path.dirname('__file__')
    print(["-s", "-v", "--cmdopt={}".format(device)])
    # reports_path = os.path.join(reports_dir, '..', 'reports\\'
    #                             "test_result_{}_{}.html".format(device["caps"]["deviceName"], device["port"]))
    pytest.main(["-s", "-v",
                 "--cmdopt={}".format(device)]
                )
                 # "--html={}".format(reports_path)
