# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:50:16 2022

@author: AVERKHO
"""

from dataclasses import dataclass

@dataclass
class Utils:
    
    
    purple_hex:str='#00FFFF'
    green_hex:str='#00FF00'
    yellow_hex:str='#FFFF00'
    rose_hex:str='#FF00FF'
    red_hex:str='#FF0000'
    blue_hex:str='#0000FF'
    white_hex:str='#FFFFFF'
    black_hex:str='#000000'
    
    purple_rgba:tuple=(0,1,1,1)
    green_rgba:tuple=(0,1,0,1)
    yellow_rgba:tuple=(1,1,0,1)
    rose_rgba:tuple=(1,0,1,1)
    red_rgba:tuple=(1,0,0,1)
    blue_rgba:tuple=(0,0,1,1)
    white_rgba:tuple=(1,1,1,1)
    black_rgba:tuple=(0,0,0,1)
    
    csfont:str='Comic Sans MS'
    
    ax_kwargs={'color':purple_hex,'fontweight':'bold','fontproperties':{'family':csfont,'size':20}}
    grid_kwargs={'color':white_hex,'linestyle':'--'}
    i=10
    
