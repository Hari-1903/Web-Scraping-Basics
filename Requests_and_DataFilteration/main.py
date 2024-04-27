from bs4 import BeautifulSoup
import requests
import time

unfamilar_skills = input('Enter the skills you are not familiar with: ')
print(f'Filtering out {unfamilar_skills}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Data+Science%22&txtKeywords=%22Data+Science%22&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        job_posted = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in job_posted:
            company_name_full = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            company_name = company_name_full.split('\n')[0]
            skills_required = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info= job.header.h2.a['href']

            if unfamilar_skills not in skills_required:
    
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Skills Required: {skills_required.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                    f.write('')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)