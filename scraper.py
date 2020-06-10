import csv

import requests
from bs4 import BeautifulSoup
import xlsxwriter

URL = "https://ca.indeed.com/jobs?q=software+developer&l=Vancouver%2C+BC"
# conducting a request of the stated URL above:
page = requests.get(URL)
# specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")


def extract_job_title_from_result(soup):
    global jobs
    jobs = []
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return jobs


extract_job_title_from_result(soup)


def extract_location_from_result(soup):
    global locations
    locations = []
    spans = soup.findAll('span', attrs={'class': 'location'})
    for span in spans:
        locations.append(span.text)
    return locations


extract_location_from_result(soup)


def extract_companyName_from_result(soup):
    global company
    company = []
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        try:
            company.append(div.find('nobr').text)
        except:
            try:
                div_two = div.find(name="div", attrs={"class": "sjcl"})
                div_three = div_two.find("div")
                company.append(div_three.text.strip())
            except:
                company.append("Nothing_found")
    return company


extract_companyName_from_result(soup)


def extract_summary_from_result(soup):
    global summaries
    summaries = []
    spans = soup.findAll('div', attrs={'class': 'summary'})
    for span in spans:
        summaries.append(span.text.strip())
    return summaries


extract_summary_from_result(soup)

for (j, c, l, s) in zip(jobs, company, locations, summaries):
    new_list = [j, c, l, s]

    for item in enumerate(new_list):
        print(item)
