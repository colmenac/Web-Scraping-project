import time

from bs4 import BeautifulSoup
import requests

###This will only take the first page!No worries.

print("Put a skill you're not familiar with:")
unfamiliar_text = input('>')
print(f"Filtering out {unfamiliar_text}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    h = html_text
    soup = BeautifulSoup(h.text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx") #Now we're grabbing ALL the posts! Not just the 1st.
    for job in jobs:
        published_date = job.find('span', class_ = "sim-posted").span.text
        #Without .span.text. we print out another tag. Let's just go for the text.
        if 'few' in published_date:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
            coms= job.find('h3', class_ = "joblist-comp-name")
            skills = job.find('span', class_ = "srp-skills").text.replace(' ','')
            more_info = job.header.h2.a['href'] #We use . operator to get to the link and then filter the href with []
            if unfamiliar_text not in skills:
                #Don't conduse .split() with .replace()
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info.strip()}")

                print(" --------------------------------------")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        time.sleep(time_wait * 60)
        print(f"Waiting {time_wait} minutes...") #Runs every 10 minutes
