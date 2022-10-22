from bs4 import BeautifulSoup
import requests

with open('home.html', 'r',) as html_file: ### We open the html file in read mode. We then read the whole file
    ###into the variable html_file.
    content = html_file.read()
    ###print(content) ### Remember the html file we read from is just HTML!!! So us printing it would just be...HTML!
    soup = BeautifulSoup(content, 'lxml') ###Just the tags
    print(soup)
    tags = soup.find('h1')###Find only searches for the first element not all!!!
    print("-------------------------------------------------------------------------------------------")
    print(tags)
    ###Python find_all returns a list, not just the first element!!!

    tags = soup.find_all('h5')  ###Find only searches for the first element not all!!!
    print("-------------------------------------------------------------------------------------------")
    print(tags)






