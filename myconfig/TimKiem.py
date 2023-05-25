import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.express as px
import cv2
from PIL import Image
class Tim(): 
    def __init__(self): 
        self.data = pd.read_csv('prepared_data_book.csv')
    
    
    def TimTheoTacGia(self, keyword):
        #keylower = keyword.lower()
        dt = self.data.query("authors.str.lower().str.contains(@keyword)", local_dict={'keyword': keyword.lower()})
        fig, ax = plt.subplots()
        ax= dt.plot(kind='barh', color='gray')
        plt.xlabel('{}'.format(keyword))
        plt.ylabel('Doanh Số')
        plt.title('Doanh số các sách của tác giả {}'.format(keyword))
        #plt.show()
        return dt
    def TimTheoTen(self, keyword): 
        return self.data.query("title.str.lower().str.contains(@keyword)", local_dict={'keyword': keyword.lower()})
    def TimTheoID(self, id): 
        return self.data.query("product_id == @keyword", local_dict={'keyword': id})