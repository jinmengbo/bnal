# 三大步骤
import os,sys
sys.path.append(os.getcwd())
import pytest

from Base.duqu_yaml import Duquyaml

import allure
from Page.page_ty import PageTy
# 读取参数函数，封装
def get_data():
    abbs=[]
    for data in Duquyaml("shuju.yaml").duqu_yaml().values():
        abbs.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    return abbs
class TestBn():
    # 首先是实列化入口类
    # 导入配置页面
    def setup_class(self):
        self.page=PageTy()
        self.yemian=self.page.page_ym()
        self.yemian.page_dianjiwo()
        self.yemian.page_dianjiyiyou()
    def teardown_class(self):
        self.page.driver.quit()
    @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data())
    def test_001(self,username,password,expect_result,expect_toast):
        #这是正确的,执行以下用列
        if expect_result:
            try:
                self.yemian.page_dianjishuru()
                self.yemian.page_shuru(username)
                self.yemian.page_shurumi(password)
                self.yemian.page_dianjidenglu()
                nickname = self.yemian.page_paduannicheng()
                assert expect_result in nickname
                self.yemian.page_dianjishezhi()
                self.yemian.page_hudong()
                self.yemian.page_tui()
                self.yemian.page_tui_ok()
                self.yemian.page_dianjiwo()
                self.yemian.page_dianjiyiyou()
                self.yemian.page_dianjishuru()
            except:
                self.yemian.base_get_screenshot()
                with open("./Imge/faild.png","rb") as f:
                    allure.attach("失败原因请看截图：",f.read(),allure.attach_type.PNG)
                    # raise
        else:
            try:
                # 这是以成功完后，开始执行逆向用列
                self.yemian.page_shuru(username)
                self.yemian.page_shurumi(password)
                self.yemian.page_dianjidenglu()
                # 开始断言，name1的数据是否和抓取到的数据是否一致
                assert expect_toast in self.yemian.base_get_toast(expect_toast)
                # 失败后开始截图
            except:
                self.yemian.base_get_screenshot()
                with open("./Imge/faild.png","rb")as f:
                    allure.attach("失败后截图: ",f.read(),allure.attach_type.PNG)
                    raise
