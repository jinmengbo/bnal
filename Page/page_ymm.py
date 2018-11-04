import Page
from Base.base import Base
class PageYmm(Base):
    def page_dianjiwo(self):
        self.base_click(Page.log_wo)
    def page_dianjiyiyou(self):
        self.base_click(Page.log_you)
    def page_dianjishuru(self):
        self.base_click(Page.log_shu)
    def page_shuru(self,username):
        self.base_input(Page.log_shu,username)
    def page_shurumi(self,password):
        self.base_input(Page.log_mi,password)
    def page_dianjidenglu(self):
        self.base_click(Page.log_deng)
    def page_paduannicheng(self):
        return self.base_get_text(Page.log_niceng)
    def page_dianjishezhi(self):
        self.base_click(Page.log_she)
    def page_hudong(self):
        el1=self.base_find_element(Page.log_duan)
        el2=self.base_find_element(Page.log_xiumi)
        self.base_drag_and_drop(el1,el2)
    def page_tui(self):
        self.base_click(Page.log_tui)
    def page_tui_ok(self):
        self.base_click(Page.log_tui_ok)
    