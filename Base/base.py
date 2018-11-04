# 初始化类

import os
# 导入系统模块包，能获取到当前系统路径，系统的版本，转义符

from selenium.webdriver.common.by import By
# 导入By类
from selenium.webdriver.support.wait import WebDriverWait
# 导入显示等待
class Base():
# 导入类.为后期调用。
    def __init__(self,driver):
        # 初始化driver
        self.driver=driver
    # 显示等待
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # 显示等待
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    '''
        显示等待,WebDriverWait函数先导用,timeout总等待时间,
        poll-frequency=0.5,间隔的时间默认0.5秒，可以后期调，lambda幂名函数
    '''

    # 封装点击方法
    def  base_click(self,loc):
        self.base_find_element(loc).click()
    '''
    点击方法封装,base_findelement是显示等待力的，然后调用到这里，进行封装，loc是封装好的元祖，*一星解元祖，**二星解字典
    loc是需要传入的元祖， 或者其他的数据
    '''
    # 封装输入方法
    def base_input(self,loc,text):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(text)
    '''
    el是接受变量的函数，clear()是清除，输入的时候首先必须要清除文本，在输入新的信息，send_keys输文本信息，text是存入的文本
    需要在self,这行中传入，在调用种输入的函数,
    '''
    # 封装截图操作
    def base_get_screenshot(self):
        img_path=os.getcwd()+os.sep+"Imge"+os.sep+"faild.png"
        self.driver.get_screenshot_as_file(img_path)
    '''
    img_path是接受截图路径的变量值,os.getcwd()获取到的当前路径,os.sep是系统分隔符,可根据系统不同转成不同的系统的分隔符，
    Imge是系统的文件夹，find.png是名字格式
    '''
    # 获取toos封装
    def base_get_toast(self,message):
        meg=By.XPATH,"//*[contains(@text,'"+message+"')]"
        return self.base_find_element(meg,poll=0.1).text

    '''
    message一个函数,message=是可以覆盖slef里的message, By是类，查找"xpath，//*[contains（@text,'')]"固定格式
    '"+message+"',是拼接起来动态值是toast弹出的文本信息,return poll=0.1是间隔一秒，因为toast间隔0.1-0.3秒
    text是获取的文本信息
    '''
    # 获取元素文本信息
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    '''
    这一步是获取文本元素的信息，然后返回值loc获取到的.text文本信息..
    '''
    # 滑动方法封装从一个元素划到另一个元素
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)
    '''
    el1:是起点因素，
    el2,是落点元素
    drag_是起,and是到,drop是落
    '''
#