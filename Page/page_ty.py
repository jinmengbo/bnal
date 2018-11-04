from Base.get_driver import get_driver
from Page.page_ymm import  PageYmm


class PageTy():
    def __init__(self):
        self.driver=get_driver()
    def page_ym(self):
       return PageYmm(self.driver)
'''
说明: 统一入口管理类，主要解决一下两个方面
    1.对Page页面对象统一进行管理
    2.解决批量导入page问题
    3，扩展-->>解决driver问题
操作:
    1.利用类与方法的机制，在统一管理入口类，新建或取多个页面方法
'''