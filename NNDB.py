#%%EXCEL
import csv


# 開啟輸出的 CSV 檔案
with open('read.csv', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  #writer = csv.writer(csvfile)
  reader=csv.reader(csvfile)
  li=list(reader)
  Name=li[0]
  Fname=li[1]
  Lname=li[2]

#%%合併沒用
Name=[]
for (x,F,L) in zip(range(len(Fname)),Fname,Lname):
    Name.append(Fname[x]+' '+Lname[x])

#%%import
import csv
import requests
from bs4 import BeautifulSoup

import re

#%%
test = open("test.txt","w",encoding='UTF-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
NameSearch=[]
NameNotFind=[]
NameGet=[]
OccupationGet=[]
urlGet=[]
for n in range(len(Fname)):
    url="http://search.nndb.com/search/nndb.cgi?type=unspecified&query="+str(Fname[n])+'+'+str(Lname[n])
    r = requests.get(url, headers=headers) #將網頁資料GET下來
    status=r.status_code#200表示正常、404表示找不到網頁等
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    sel= soup.select("a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    selOccupation=soup.select("font[size='-1']")
    print("第"+str(n+1)+"個:")
    findone=0
    for s,o,x in zip(sel,selOccupation, range(len(sel))):
        if x>=2:
            if Fname[n] in s.string and Lname[n] in s.string:
                NameSearch.append(Name[n])
                urlGet.append(s["href"])
                NameGet.append(s.string)
                OccupationGet.append(o.string)

                print([Name[n],s.string,o.string]) 
                findone=1
    if findone==0:
        print('找不到') 
        NameNotFind.append(Name[n])

#%%
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(Name)
  writer.writerow(NameGet)
  writer.writerow(OccupationGet)
  writer.writerow(urlGet)
#%%
NameList=[]
Birthplace=['']*len(urlGet)
Born=['']*len(urlGet)
Gender=['']*len(urlGet)
RaceOrEthnicity=['']*len(urlGet)
Nationality=['']*len(urlGet)
ExecutiveSummary=['']*len(urlGet)
Education=['']*len(urlGet)
MaritalStatus=['']*len(urlGet)
Children=['']*len(urlGet)
SexualOrientation=['']*len(urlGet)
#%%
Occupation= ['']*len(urlGet)
Aka= ['']*len(urlGet)
NameList=[]
#%%寫入EXCEL

# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='',encoding="utf-8") as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  for entries1 in entry1:
    writer.writerow(entries1)
  
  
  #%%
  writer.writerow(Birthplace)
  writer.writerow(Born)
  writer.writerow(Gender)
  writer.writerow(RaceOrEthnicity)
  writer.writerow(Nationality)
  writer.writerow(ExecutiveSummary)
  #writer.writerow(Education)
  #writer.writerow(MaritalStatus)
  #writer.writerow(Children)
  writer.writerow(SexualOrientation)
  writer.writerow(Occupation)

#%%
  
import csv


entry2=[]
# 開啟 CSV 檔案
with open('317.csv', newline='',encoding="utf-8") as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    entry2.append(row)
    

Family=['']*2342

Education=['']*2342

Work=['']*2342
Corp=['']*2342
for row in rows:
   entry2.append(row)
  
for x,row in zip(range(len(entry2)),entry2):
   for r in row:
   if '**' in r:
       Family[x]=r
       break
for x,row in zip(range(len(entry2)),entry2):
   for r in row:
       if 'University' in r:
           Education[x]=r
           break
 #%%
      
with open('output.csv', 'w', newline='',encoding="utf-8") as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料

  writer.writerow(Family)
  writer.writerow(Education)
  writer.writerow(Work)
#%% 擷取資料擷取資料擷取資料擷取資料擷取資料擷取資料擷取資料

soupGet=[]

for url,x in zip(urlGet,range(len(urlGet))):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    soupGet.append(soup)
    print("第"+str(x+1)+"個:")

#%% 
    
for soup,x in zip(soupGet,range(len(soupGet))):
    
    #print("第"+str(x+1)+"個:")

    name=soup.select('font b')
    name=name[0].string
    NameList.append(name)
    #print('Name'+name)
    
    target=soup.select('p b')
    for elem in target:
        if 'Occupation' in elem.string:
            Occupation[x] = elem.next_sibling.string
            if elem.next_sibling.string==' ':
                Occupation[x] = elem.next_sibling.next_sibling.string
        if 'AKA' in elem.string:
            Aka[x] = elem.next_sibling.string

    if Occupation[x]==' ': 
        print(x) 
            #%% 
        if 'Born' in elem.string:
            if '?' in elem.next_sibling.string:
                Born[x] ='?'
            else:
                Born[x] = elem.next_sibling.next_sibling.string
                if '-' in elem.next_sibling.next_sibling.string:
                    Born[x]=elem.next_sibling.next_sibling.next_sibling.next_sibling.string
            print('Born: '+Born[x])
            #%% 
        if 'Gender' in elem.string:
            Gender[x] = elem.next_sibling.string
            print('Gender:'+elem.next_sibling.string)
        if 'Race' in elem.string:
            RaceOrEthnicity[x] = elem.next_sibling.string
            print('Race or Ethnicity: '+elem.next_sibling.string)
        if 'Occupation' in elem.string:
            Occupation[x] = elem.next_sibling.string
            print('Occupation: '+elem.next_sibling.string)
        if 'Nationality' in elem.string:
            Nationality[x] = elem.next_sibling.string
            print('Nationality:'+elem.next_sibling.string)
        if 'Executive' in elem.string:
            ExecutiveSummary[x] = elem.next_sibling.string
            print('Executive Summary: '+elem.next_sibling.string)
        if 'Birthplace' in elem.string:
            if elem.next_sibling.string==' ':
                Birthplace[x] = elem.next_sibling.next_sibling.string
            else:
                Birthplace[x] = elem.next_sibling.string
            print('Birthplace: '+Birthplace[x])
        if 'Education' in elem.string:
            Education[x] = elem.next_sibling.string
            print('Education'+elem.next_sibling.string)
        if 'Marital' in elem.string:
            MaritalStatus[x] = elem.next_sibling.string
            print('Marital'+elem.next_sibling.string)
        if 'Children' in elem.string:
            Children[x] = elem.next_sibling.string
            print('Children'+elem.next_sibling.string)
        if 'Sexual' in elem.string:
            SexualOrientation[x] = elem.next_sibling.string
            print('Sexual'+elem.next_sibling.string)
            
            
#%%
import html2text   
h = html2text.HTML2Text()
# Ignore converting links from HTML
h.ignore_links = True


Education=['']*len(soupGet)

for soup,x in zip(soupGet,range(len(soupGet))):
    print("第"+str(x+1)+"個:")
    target=soup.select('p a')
    #Education.append(target[1].parent.stripped_strings)
    #for string in target[3].parent.stripped_strings:
        #print(repr(string))
    Education[x]= h.handle(str(target[2].parent))
    if x in W:
        Education[x]= h.handle(str(target[1].parent))


#%%

entry1=[]


for entry,x in zip(Education,range(len(Education))):

    if "\n\n" in entry:
        entry1.append(re.split("\n\n", str(entry)))
    else:
        print(x)

#%%
"""
wrong1=[]
wrong2=[]

for entry,x in zip(entry1,range(len(entry1))):
    if(len(entry)==1):
        print(entry)
        wrong1.append(x)
        
    else: 
        while('NNDB MAPPER' in entry[1]==False):
             print(entry)
             wrong2.append(x)
"""
#%%

for entries1 in entry1:
    for entry in entries1:
        if entry=='':
            entries1.remove(entry)
        if entry==' ':
            entries1.remove(entry)  
        if entry=='  ':
            entries1.remove(entry) 
        if entry=='/n':
            entries1.remove(entry) 


#%%
L=['']*len(entry1)
W=[]
for entries1,x in zip(entry1,range(len(entry1))):
    for st in entries1:
        if '  \n  ' in str(st):
            L[x]=entries1.index(st)
            break;
        if 'Do you know' in str(st):
            L[x]=entries1.index(st)
            break;
        if 'New!' in str(st):
            L[x]=entries1.index(st)
            break;
    if L[x]=='':
        W.append(x)
        print(x)
        print(entries1)

#%%
for entries1,x in zip(entry1,range(len(entry1))):
    while len(entries1) > L[x] :
        entries1.pop(L[x])
        print(x)
#%%寫入EXCEL
a1=[]
a2=[]
for aa in a:
    a1.append(aa[0])
    a2.append(aa[1])

# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(a1)
  writer.writerow(a2)




