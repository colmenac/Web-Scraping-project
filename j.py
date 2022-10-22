import time

from bs4 import BeautifulSoup
import requests

###This will only take the first page!No worries.

print("Put a skill you're not familiar with:")
unfamiliar_text = input('>')
print(f"Filtering out {unfamiliar_text}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    h = html_text #Note how the above request NEEDS to be in .text form NOT in its literal response form.
    soup = BeautifulSoup(h.text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx") #Now we're grabbing ALL the posts! Not just the 1st.
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = "sim-posted").span.text
        #Without .span.text. we print out another tag. Let's just go for the text.
        if 'few' in published_date:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ', '')
            coms= job.find('h3', class_ = "joblist-comp-name")
            skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href'] #We use . operator to get to the link and then filter the href with []
            if unfamiliar_text not in skills:
                with open(f'posts/{index}.txt', 'w') as f:

                    #Don't conduse .split() with .replace()
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info.strip()} \n")
                    print(f"File saved: {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        time.sleep(time_wait * 60)
        print(f"Waiting {time_wait} minutes...") #Runs every 10 minutes

#enumrate() is a python function that lets us iterate while keeping tabs on the index of our object. It starts
#at 0, so the first element is 0. It's done like index, job in enumerate(jobs) so the thing being passed into it,
#is the object to iterate through and the x and y are: x to keep tabs and y the actual object to perform
#iterations from.