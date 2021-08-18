# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:01:43 2021

@author: padmini
"""


        
import data 
import inference
import Train
import validation 
import Test
import Controller
import model
import optimizer
import learning_rate_scheduler        

class Initialise_values(object):
    def __init__(self, path):
    
    def split_data(self):
        split_train_test_valid()
        
    def model(self):
        initialise_model()
        
    def optimizer(self):
        optimizer()
        
    def lr_scheduler(self):
        LR-scheduler()
        
    def train_valid_test(self,model,optimizer,lr_scheduler):
        train()
        Validation()
        test
        return results

class Return_results(object):
    def __init__(self):
        
    def infer_results(self):
        return image,characters,num_of_characters,masked_image