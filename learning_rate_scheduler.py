# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:02:09 2021

@author: padmini
"""

from torch.optim import lr_scheduler


class LRscheduler(object):
    def __init__(self,optimizer,last_epoch,verbose):
      
        
    def step(self):
        return scheduler.step()
    
class stepLR(LRscheduler):
    def __init__(self, optimizer, step_size, gamma, last_epoch, verbose=False):
         super(stepLR, self).__init__(optimizer, last_epoch, verbose)
    
        
    def get_lr(self):
        pass
    
class multistepLR(LRScheduler):
     def __init__(self, optimizer, milestones, gamma,last_epoch, verbose):
         super(multistepLR, self).__init__(optimizer, last_epoch, verbose)
     
     def get_lr(self):
        pass
    
class exponentialLR(LRScheduler):   

    def __init__(self, optimizer, gamma, last_epoch, verbose):
        super(exponentialLR, self).__init__(optimizer, last_epoch, verbose)
        
     def get_lr(self):
        pass