import numpy as np
import pandas as pd
import os
import plotly.express as px
import seaborn as sns
import plotly.express as px
import cv2
import TimKiem
class DanhSach(): 
    def __init__(self): 
        self.Ds = pd.read_csv('ThuVien.csv')
        
    #ThuVien = pd.read_csv('ThuVien.csv')
    def createListbook(self, keyword): 
        newrecord = {'Name': keyword }
        self.Ds = self.Ds.append(newrecord, ignore_index=True)
        (self.Ds).to_csv('ThuVien.csv', index=False)
        newlist = { 'product_id': [],
               'title': [], 
               'authors': [],
               'original_price': [], 
               'current_price': [], 
               'quantity': [],
               'category': [], 
               'n_review': [], 
               'avg_rating': [],
               'pages': [], 
               'manufacturer': [], 
               'discount': []}
        newlist = pd.DataFrame(newlist)
        newlist.to_csv('{}.csv'.format(keyword), index= False)

    def addnewbook(self, product_id, nameList): 
        df = pd.read_csv('{}.csv'.format(nameList))
        Tim = TimKiem.Tim()
        newbook = Tim.TimTheoID(product_id)
        df = df.append(newbook, ignore_index=True)
        df.to_csv('{}.csv'.format(nameList), index= False)
    
    def showDSThuVien(self): 
        self.Ds = pd.read_csv('ThuVien.csv')
        return self.Ds
    
    def showThuVien(self, nameList): 
        return pd.read_csv('{}.csv'.format(nameList))
    
        
        
    