from  distutils.core import setup

setup(name="aa_message",
      version="1.0",
      description="wing发送和接收消息模块",
      long_description="完整的发送和接受消息模块",
      author="wing",
      author_email="wj2206906091@hotmail.com",
      url="......",
      #指定包里面的模块名
      py_modules=["aa_message.send_message",
                  "aa_message.receive_message"])

#python3 setup.py build
#python3 setup.py sdist