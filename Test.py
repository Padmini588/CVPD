# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 00:18:26 2021

@author: padmini
"""

class Test(object):
    def __init__(self,model,dataloader):
    
    def truth_predictiction(self):
        retun prediction, ground_truth



class classification_metrics(Test):
    def __init__(self,confusion_matrix):
    
    def accuarcy(self):
        return test_accuracy
    
    def f1_score(self):
        return f1_score
    
    def recall(self):
        return recall
    
    def precision(self):
        return precision

class segmentation_metrics(Test):
     def __init__(self,confusion_matrix):
    
    def iou_loss(self):
        return iou_loss
    
    def dice_loss(self):
        return dice_loss