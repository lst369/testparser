import requests
from bs4 import BeautifulSoup
import lxml
import time
import random

# Парсим список всех кандидатов и записываем его в файл
# person_url_list = []

# for i in range (0, 760, 20):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"
    
#     q = requests.get(url)
#     result = q.content

#     soup =  BeautifulSoup(result, "lxml")

#     persons = soup.find_all("a")


#     for person in persons:
#         person_page_url = person.get("href")
#         person_url_list.append(person_page_url)
    
#     time.sleep(random.randrange(2, 4))

    

# with open ("scrap_bundestag/data/person_url_list.txt", "a") as file:
#     for line in person_url_list:
#         file.write(f"{line}\n")

with open ("scrap_bundestag/data/person_url_list.txt") as file:

    lines = [line.strip() for line in file.readlines()]

    for line in lines:
        q = requests.get(line)
        result = q.content
