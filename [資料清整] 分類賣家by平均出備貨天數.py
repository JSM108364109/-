# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
#from datetime import datetime


SellerType=[]
temp=[]
week=[]
cluster=[]

categoery_list=["PS","OS","CB","C2C"]
Electroic_list=["Hardware & 3C","Mobile & Gadgets","Home Electronic"]
FMCG_list=["Health & Beauty","Home & Living","Food & Beverages","Mother & Baby"]
Fashion_list=["Men's Bags& Accessories","Women Accessories","Women Shoes","Women Bags","Women's Apparel","Men Shoes","Men's Apparel","Women's Bags"]
Lifestyle_list=["Pets","Sports & Outdoors","Motors","Everything Else","Tickets & Services","Game Kingdom","Life & Entertainment","Helpbuy"]

df=pd.read_excel(r'C:\Users\jasmine.lu\Desktop\py\OS&PS_DTS&APT_20190509.xlsx')
df=df.drop('userid', axis=1)
df=df.drop('username', axis=1)
df=df.drop('shop_name', axis=1)
df=df.dropna() #for20190509
df=df[df.avg_shipping_require_days != '未到貨'] #for20190430


week= '20190509'
###當日更新-抓取日期方式###
#today_time=datetime.now()
#week=today_time.strftime('%Y%m%d')

for num_of_data in range(len(df)):  #執行每一列資料
#############################################判斷屬於哪個cluster
    if df.iloc[num_of_data,1]  in Electroic_list:
        cluster.append('Electronic')
    elif df.iloc[num_of_data,1]  in FMCG_list:
        cluster.append('FMCG')
    elif df.iloc[num_of_data,1]  in Fashion_list:
        cluster.append('Fashion')    
    else:
        cluster.append('Lifestyle')
        
 ############################################判斷AP>DTS###
    if df.iloc[num_of_data,6]>df.iloc[num_of_data,5]: 
       temp.append(1)
    elif temp.append(0):
        break 
##############################################判斷SellerType###    
    checkIsC2C=True 
    for num_of_col in range(4,1,-1):
        if df.iloc[num_of_data,num_of_col]>0 :
            checkIsC2C=False
            SellerType.append(categoery_list[num_of_col-2])
            break
    if checkIsC2C:
        SellerType.append("C2C")
        
df=df.drop('is_cross_border', axis=1)
df=df.drop('is_official_store', axis=1)
df=df.drop('is_preferred', axis=1)
df=df.drop('main_category', axis=1)
df=df.drop('shopid', axis=1)

df['Week']=week       
df['SellerType']=SellerType
df['APT>DTS']=temp
df['Cluster']=cluster         

df.to_excel(r'C:\Users\jasmine.lu\Desktop\py\20190509_result.xlsx',index=False, header=True)