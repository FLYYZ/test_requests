import pytest
import random

'''
使用--reruns参数指定运行失败时重新运行的次数
pytest --reruns 3 -s -v test_rerun.py
'''
def test_rerunfailure():
    a=random.randint(1,3)
    print(a)
    assert a==3