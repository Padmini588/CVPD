# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:42:35 2021

@author: padmini
"""

import view

class Controller(object):
    
    def bind(view:View):
        pass

class Datapath(Controller):
    def __init__(self,path:str):
        
    def bind(self,view:Form):
        pass
    
    def validate_entries(self):
        retrun path

class Model(Controller):
    def __init__(self,option):
        
    def bind(self,view:Form):
        pass
    def validate_button(self):
        return model      

class Optimizer(Controller):
    def __init__(self,option):
        
    def bind(self,view:Form):
        pass
    def validate_button(self):
        return optimizer
    
class Lr_scheduler(Controller):
    def __init__(self,option):
        
    def bind(self,view:Form):
        pass
    def validate_button(self):
        return lr_scheduler
