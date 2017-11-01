import re, requests

def Search(url, depth):
    Passed_Pages.add(url)    
    HTTP = requests.get(url)

    #Почты
    Mails = re.findall(r"(?<=<a href=\"mailto:)[a-zA-Z0-9\._\-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", HTTP.text)
    for mail in Mails:
        Set_Mail.add(mail)

    #Абсолютные ссылки
    Link_Absolute = re.findall(r'(?:(?<=<a href=\")'+Modified_URL+'(?:(?:[%\-_a-zA-Z0-9\:]+\/?)+)+)', HTTP.text)
    Set_Link_Absolute = set(Link_Absolute)

    #Относительные ссылки
    Link_Relative = re.findall(r'(?:(?:(?<=<a href=\")\/?(?:[%\-_a-zA-Z0-9\:]+\/?)+))', HTTP.text)
    Set_Link_Relative = set(Link_Relative)
    Set_Link_Relative.discard('http:/')
    Set_Link_Relative.discard('https:/')
    Set_Link_Relative.discard('ftp:/')

    #Превращение относительных ссылок в абсолютные
    for link in Set_Link_Relative:
        link = URL + link
        Set_Link_Absolute.add(link)

    #Поиск по сайту
    for link in Set_Link_Absolute:
        if depth <= 0:
            continue
        if link in Passed_Pages:
            continue
        Search(link, depth-1)


#Начальные данные
Passed_Pages = set()
Set_Mail = set()
URL = "http://www.csd.tsu.ru/"
Depth = 2

Modified_URL=URL.replace('/','\/')
Modified_URL=Modified_URL.replace('.','\.')

Search(URL, Depth)

#Вывод
for mail in Set_Mail:
    print(mail)