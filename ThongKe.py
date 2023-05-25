import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.express as px
import cv2
from PIL import Image

class Plot(): 
    def __init__(self): 
        self.data = pd.read_csv('prepared_data_book.csv')
    
    def sort_title_by_col(self, col):
    # I used a trick here, because we group by title (without duplicated value).
    # The aim is to map with title against.
        res = self.data.groupby("title")[col].max()\
            .sort_values(ascending=False)\
            .index.tolist()
    
        return res
    
    def Topauthors(self, k, name): 
        key = name
        if name == 'n_review': 
            key = 'Review'
        if name == 'avg_rating': 
            key = 'Rating'
        if name == 'discount': 
            key = 'Discount'
        if key == 'quantity': 
            key = 'Doanh số'
        a = self.data.groupby('authors')[name].sum().sort_values(ascending=False)[:k]
        a.drop(labels='Unknown', inplace=True)
        fig, ax = plt.subplots()
        ax=a.plot(kind='barh', color='gray')
        plt.xlabel('Tác giả')
        plt.ylabel(key)
        plt.title('Top {} tác giả với lượng {} nhiều nhất'.format(k, key))
        #plt.show()
        return fig
    
    def Topbook(self, k, name): 
        key = name
        if name == 'n_review': 
            key = 'Review'
        if name == 'avg_rating': 
            key = 'Rating'
        if name == 'discount': 
            key = 'Discount'
        if key == 'quantity': 
            key = 'Doanh số'
            
        a = self.data.groupby('title')[name].sum().sort_values(ascending=False)[:k]
        #a.drop(labels='Unknown', inplace=True)
        fig, ax = plt.subplots()
        ax=a.plot(kind='barh', color='gray')
        plt.xlabel('Sách')
        plt.ylabel(key)
        plt.title('Top {} cuốn sách có {} nhiều nhất'.format(k, key))
        #plt.show()
        return fig
    
    def Topcategory(self, k, name): 
        key = name
        if name == 'n_review': 
            key = 'Review'
        if name == 'avg_rating': 
            key = 'Rating'
        if name == 'discount': 
            key = 'Discount'
        if key == 'quantity': 
            key = 'Doanh số'
        a = self.data.groupby('category')[name].sum().sort_values(ascending=False)[:k]
        a.drop(labels='Others', inplace=True)
        fig, ax = plt.subplots()
        ax=a.plot(kind='barh', color='gray')
        plt.xlabel('Thể loại')
        plt.ylabel(key)
        plt.title('Top {} thể loại có {} nhiều nhất'.format(k, key))
        #plt.show()
        return fig
    def meanbook(self, k): 
        dt = (self.data.sort_values(by='quantity', ascending=False)).copy()
        column_to_drop = ['product_id']
        dt = dt.drop(columns= column_to_drop)
        meantop_book = dt.head(k).mean()
        meanallbook = dt.mean()
        return meanallbook, meantop_book
    def meanauthor(self, k): 
        dt = (self.data.sort_values(by='authors', ascending=False)).copy()
        column_to_drop = ['product_id']
        dt = dt.drop(columns= column_to_drop)
        meantopauthor = dt.head(k).mean()
        meanallbook = dt.mean()
        return meanallbook, meantopauthor
    def meancategory(self, k): 
        dt = (self.data.sort_values(by='category', ascending=False)).copy()
        column_to_drop = ['product_id']
        dt = dt.drop(columns= column_to_drop)
        meantopcategory = dt.head(k).mean()
        meanallbook = dt.mean()
        return meanallbook, meantopcategory
    def topTacGiaNhieuSach(self, k): 
        dt = self.data.copy()
        dt = dt.drop_duplicates(subset=['title'])
        topTacGiaNhieuSach = dt.authors.value_counts()
        return topTacGiaNhieuSach[1:k+1]
    def categoryInTop(self, k): 
        dt = self.data.copy()
        top100 = dt.nlargest(100, 'quantity')
        book_counts = top100['category'].value_counts()
        return book_counts[1:k+1]

    def price(self): 
        fig, ax = plt.subplots()
        ax = sns.kdeplot(self.data.original_price, color='gray', shade=True, label='Giá ban đầu')
        ax = sns.kdeplot(self.data.current_price, color='g', shade=True, label='Giá hiện tại')
        plt.xlabel('Giá')
        plt.title('Mật độ giá hiện tại và giá ban đầu')
        plt.legend()
        return fig
    def pages(self): 
        fig, ax = plt.subplots()
        ax = sns.kdeplot(self.data.pages, color='gray', shade=True, label='Số trang sách')
        plt.xlabel('Số trang')
        plt.title('Mật độ số trang ')
        plt.legend()
        return fig






 
        


        


