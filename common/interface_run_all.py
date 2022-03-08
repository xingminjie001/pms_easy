import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import os,time
from common.file_path import REPORT_PATH,INTERFACE_CASE_PATH
from common.HTMLTestRunner_PY import HTMLTestRunner
from common.mail import Email

def all_case():
    discover = unittest.defaultTestLoader.discover(INTERFACE_CASE_PATH,
                                                    pattern="test_*.py",
                                                    top_level_dir=None)
    return discover
if __name__ == "__main__":
    # report_time = time.strftime('%Y%m%d%H%M%S')
    report = os.path.join(REPORT_PATH,'zhonghui_report.html')

    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='慧云接口测试', description='慧云接口测试')
        runner.run(all_case())

    #e = Email()
    #e.send()