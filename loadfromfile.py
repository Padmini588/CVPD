# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 19:57:52 2021

@author: padmini
"""
import torch
from torch.utils.data import Dataset
import os

class LoadFromFile(Dataset):
    def __init__(self,dataFolder):
        self.dataFolder=dataFolder
    
    def split_train_valid_test_paths(self):
        return train_path,valid_path,test_path
    #def read_image_file(image_path):
    #    return image
    #def read_label_file(label_path):
    #    return label

class Dataloader(LoadFromFile):
    def __init__(self,path,mode,augment,transform,task):
        super().__init__()
    def __getitem__(self,index):
        return image,target
    def __len__(self):
        return len(path)
    
    
        