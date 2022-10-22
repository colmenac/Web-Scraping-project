from bs4 import BeautifulSoup
import requests

###This will only take the first page!No worries.

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
h = html_text
soup = BeautifulSoup(h.text, 'lxml')
job = soup.find('li', class_="clearfix job-bx wht-shd-bx")
company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
coms= job.find('h3', class_ = "joblist-comp-name")
skills = job.find('span', class_ = "srp-skills").text.replace(' ','')
#Don't conduse .split() with .replace()
published_date = job.find('span', class_ = "sim-posted").span.text
#Without .span.text. we print out another tag. Let's just go for the text.
print(published_date)
print("Now let's show this off with String interpolation:")
print(f'''
Company Name: {company_name},
Required Skills: {skills}
''')