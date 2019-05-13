import mysql.connector
import requests
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="Wox2VHeqfX",
  passwd="9bcMKoUSKy",
  database="Wox2VHeqfX"
)
mycursor = mydb.cursor() 

def add(ts,pew):
  global mycursor,mydb
  mycursor.execute("INSERT INTO subs (ts, pew) VALUES (%d, %d)"%(ts,pew)) 
  mydb.commit()
  
def get():
  global mycursor,mydb
  mycursor.execute("select * from subs")
  result=mycursor.fetchall()
  for x in result:
    print(x)

def delete():
  global mycursor,mydb 
  mycursor.execute("TRUNCATE TABLE subs")
  
def update(ts,pew):
  delete()
  add(ts,pew)

 

url = 'https://m.youtube.com/user/PewDiePie'

headers = requests.utils.default_headers()
headers.update(
    {
      'User-Agent':'Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX3 Build/HUAWEIFIG-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
    }
)
def getsub(url):
  response = requests.get(url, headers=headers)
  txt=response.text
  num=txt.find("subscriberCount")
  sub=txt[num+39:].split()[0][0:12].replace(',','').replace('\"','')
  return int(sub)
while True:
  update(getsub("https://m.youtube.com/user/PewDiePie"),getsub("https://m.youtube.com/user/tseries"))
       
