from bs4 import BeautifulSoup
import requests

with open('home.html', 'r',) as html_file: ### We open the html file in read mode. We then read the whole file
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml') ###format the text we grabbed earlier in a nicer way.
    courses_cards = soup.find_all('div', class_='card')
    for course in courses_cards:
        course_name = course.h5.text ###We preemptively pull out only the text from the tags we grab.
        course_price = course.a.text

        print(course_name)
        print(course_price)
        print()