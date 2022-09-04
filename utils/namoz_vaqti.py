import requests
from bs4 import BeautifulSoup

mintaqalar = { "Toshkеnt":27, "Andijon":1, "Buxoro":4, "Guliston":5, "Samarqand":18, "Namangan":15, "Navoiy":14, "Jizzax":9, "Nukus":16, "Qarshi":25, "Qoʻqon":26, "Xiva":21, "Margʻilon":13 }

oylar = ["Yanvar", "Fevral", "March""Aprel" , "May" , "Iyun" , "Iyul" , "Avgust" ,"Sentyabr" ,"Oktyabr" ,"Noyabr" ,"Dekabr"]





def vaqti(mintaqa,oy):
    URL=f'https://islom.uz/vaqtlar/{mintaqa}/{oy}'
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    contents = soup.find_all('tr',class_='p_day bugun')[0]
    content = list(contents.find_all('td'))
    bugungi_vaqt = [x.text for x in content]
    # for i in content:
    #     print(i.text)
    # print(contents)
    # print(content)
    return bugungi_vaqt

# vaqti()