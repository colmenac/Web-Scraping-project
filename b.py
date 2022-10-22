from bs4 import BeautifulSoup
import requests

with open('home.html', 'r',) as html_file: ### We open the html file in read mode. We then read the whole file
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml') ###format the text we grabbed earlier in a nicer way.
    courses_html_tags = soup.find_all('h5') #Find ALL instances of h5 and return them in a list.
    for course in courses_html_tags: #for each loop
        print(course) ###We grab the tags with h5, which includes all it's stuff like h5 class =...
        ###...But maybe we just want the text typically in the middle of the tags.


    print("---------------------------------------------------------------------------------------------")
    for course in courses_html_tags:
        print(course.text) ### With the text attribute, we just grab the text in-between rather than the stuff
        ###around h5
