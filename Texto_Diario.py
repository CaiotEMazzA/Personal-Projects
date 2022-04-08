import requests
from bs4 import BeautifulSoup
from datetime import date
from os import startfile

def gather_info(url):
    gross_html = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'})
    todays_date_for_div = f'{date.today().year}-{date.today().month:02}-{date.today().day:02}T00:00:00.000Z'
    return gross_html, todays_date_for_div

def html_handling(gross_html, todays_date_for_div):
    soup = BeautifulSoup(gross_html.text, 'lxml')
    html_today_div = soup.find('div', {'data-date': todays_date_for_div})
    return html_today_div

def txt_info(html_today_div):
    txt_header = html_today_div.h2.text
    txt_bible_versicle = html_today_div.p.text
    txt_comments = html_today_div.find_all('p')[-1].text
    return txt_header, txt_bible_versicle, txt_comments

def writing_txt(txt_header, txt_bible_versicle, txt_comments):
    with open(f'Texto Diário - {date.today().day:02}-{date.today().month:02}-{date.today().year}.txt', 'w') as file:
        file.write(txt_header + '\n\n')
        file.write(txt_bible_versicle + '\n\n')
        file.write(txt_comments)

html, current_date = gather_info('https://wol.jw.org/pt/wol/h/r5/lp-t')
div = html_handling(html, current_date)
header, bible_versicle, comments = txt_info(div)
writing_txt(header, bible_versicle, comments)

startfile(f'Texto Diário - {date.today().day:02}-{date.today().month:02}-{date.today().year}.txt')
