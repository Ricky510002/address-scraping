from selenium import webdriver
import time
import csv
import pandas as pd
from selenium.webdriver.chrome.options import Options
 
options = Options()
options.add_argument('--headless')  

df = pd.read_csv('こに読み込みたいCSVシートのパス（データの入っているCSVファイル）',header=None, usecols=[0])

print(df)  #データフレームの確認

address_list = []

for i in range():#rangeのなかにデータ数を表示

  driver = webdriver.Chrome('/Users/ryuki/Desktop/chromedriver',options=options)
  driver.get('https://www.google.co.jp')
  search_bar = driver.find_element_by_name("q")
  search_bar.send_keys(df[0][i] + " 住所")
  search_bar.submit()
  try:
    address = driver.find_element_by_class_name('sXLaOe').text
  except Exception:
           # address = None
           address = ''
  finally:
    print(i)  #データの読み込みをどこまでやっているか確認
    address_list.append(address)
    time.sleep(1)    

print(address_list)

df = pd.read_csv('CSVシートのパス',names = ["店名", "住所"]) #データフレーム名に店名と住所を追加

for k in address_list:
  df["住所"] = address_list
print(df)

df.to_csv('ここに書き込みたいCSVシートのパス', mode='w')

print("Finish")
