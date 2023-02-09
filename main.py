from urllib import request
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')




with open('home.html', 'r',) as html_file: ### We open the html file in read mode. We then read the whole file
    ###into the variable html_file.
    content = html_file.read()
    print(content) ### Remember the html file we read from is just HTML!!! So us printing it would just be...HTML!
    soup = BeautifulSoup(content, 'lxml') ###Just the tags 
    tags = soup.find('h5')
    print(tags)


    word = "Difference between built-in Python copying directly to Python vs. using Beautiful Soup's .prettify()"
    print(f"----------------------------{word}-----------------------------------------------------------------")
    print(soup.prettify())

    print("---------------Example using requests----------------------------------------------------------------------")

    # Web URL
    Web_url = "https://www.geeksforgeeks.org/transparent-window-in-tkinter/"

    # Get URL Content
    r = requests.get(Web_url)

    # Parse HTML Code
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())



