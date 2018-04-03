#不同模块存在相同函数 调用会挑战最后一个
#想要调用必须通过别名来调用
from aa_01_测试模块1 import test as test1
from aa_01_测试模块1 import test
from aa_02_测试模块2 import test

test()
test1()