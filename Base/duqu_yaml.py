import sys

import os

import yaml

class Duquyaml():
    def __init__(self,filename):
        self.file_path=os.getcwd()+os.sep+"Data"+os.sep+filename
    def duqu_yaml(self):
        with open(self.file_path,"r",encoding="utf-8")as f:
            return yaml.load(f)