# 讀取測試
import pandas as pd
import numpy as np

csv_file = 'D:/Magento2UIS/magento.output/2017-10-03-08-45-52-AllStore-Order-export-csv-to-ERP.csv'
#英文的欄位名稱
colnames=['orderid', 'storeid', 'sku', 'itemname','quantity','price','placeordertime']
#讀取MAGENTO吐出BIG5的CSV檔，並丟掉第一行的欄位名稱
df = pd.read_csv(csv_file,names=colnames,encoding='big5',header=0)

#先針對STOREID做一次樞紐分析
pvt1 = pd.pivot_table(df,index=['storeid'],values=['quantity'])
#將樞紐分析表轉成DF
df1 = pd.DataFrame( pvt1.to_records())
#把DF轉成series
storelist = df1['storeid']

#在針對STOREID跟ORDERID做一次樞紐分析
pvt2 = pd.pivot_table(df,index=['storeid','orderid'],values=['quantity'])
#把分析表轉成DF
orderlist = pd.DataFrame( pvt2.to_records())

for store in storelist :
    #依STOREID過濾出該店的訂單
    orderinstore = orderlist.loc[ orderlist['storeid'] == store]
    print (orderinstore)
    print ('========================')





"""
for idx , row in df1.iterrows():
    df_detail_by_order = df.loc[ (df['storeid']==idx[0]) & (df['orderid']==idx[1]) ]
    print (df_detail_by_order)
"""
"""
for idx , row in pvt1.iterrows():
    print ('storeid:', idx)
    df_order_by_store = df.loc[df['storeid'] == idx]
    print (df_order_by_store)
    print('========================')
"""
