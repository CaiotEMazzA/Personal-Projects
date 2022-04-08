import requests
from bs4 import BeautifulSoup
from datetime import date
from os import startfile

url = 'https://wol.jw.org/pt/wol/h/r5/lp-t'
gross_html = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'})
todays_date_for_div = f'{date.today().year}-{date.today().month:02}-{date.today().day:02}T00:00:00.000Z'

soup = BeautifulSoup(gross_html.text, 'lxml')
html_today_div = soup.find('div', {'data-date': todays_date_for_div})

soup_html_today_div = BeautifulSoup(str(html_today_div), 'lxml')
html_today_div_comments = soup_html_today_div.find_all('p')[-1].text

txt_header = soup_html_today_div.h2.text
txt_bible_versicle = soup_html_today_div.p.text
txt_comments = soup_html_today_div.find_all('p')[-1].text

with open(f'Texto Diário - {date.today().day:02}-{date.today().month:02}-{date.today().year}.txt', 'w') as file:
    file.write(txt_header + '\n\n')
    file.write(txt_bible_versicle + '\n\n')
    file.write(txt_comments)

startfile(f'Texto Diário - {date.today().day:02}-{date.today().month:02}-{date.today().year}.txt')
