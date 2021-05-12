from googlesearch import search
import requests as rs 
from bs4 import BeautifulSoup
import urllib3,json

target='中國'   #目標書名
urllib3.disable_warnings()
target_list=[]
for page in range(5):
    url='https://www.ptt.cc/bbs/CFantasy/index{}.html'.format(3243-page)
    res=rs.session().get(url,verify=False)
    soup=BeautifulSoup(res.text,features="html.parser")
    for entry in soup.find_all("div",class_='r-ent'):    
        if target in entry.find('div',class_="title").text:
            target_list.append("https://www.ptt.cc/"+entry.find('a')['href'])
"""print("---------------\n")
print(target_list)"""
for links in target_list:
    res=rs.session().get(links,verify=False)
    soup=BeautifulSoup(res.text,features="html.parser")