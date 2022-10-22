from bs4 import BeautifulSoup
import requests

###This will only take the first page!No worries.

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
#print(html_text) #The html_text variable is diferent then it's form in html_text.text
h = html_text.text

soup = BeautifulSoup(h, 'lxml')
job = soup.find('li', class_="clearfix job-bx wht-shd-bx")
#We want to search for the h3 tag in only our job variable
#print(job+"/n")
company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
print(company_name)
print("-------------------------------------------------\n")
coms= job.find('h3', class_ = "joblist-comp-name")
print(coms.text)

#Our prev. attempt at this failed bc we performed .find_all on soup which returned a list assigned to a var job.
#Then we tried to apply .find() on that same variable and it failed. To fix this we just call .find() on soup
#and then .find() on job. NOTE: We actually can do find_all on the result of soup.find() result, the job variable.
#But here we decided to further format it with .text.replace(' ','')
print("-------------------------------------------------\n")

skills = job.find('span', class_ = "srp-skills").text
print(skills)