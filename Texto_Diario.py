import requests
from bs4 import BeautifulSoup
from datetime import date
from os import startfile

##################################################################################
####### Examine as Escrituras Diariamente / Examining the Scriptures Daily #######
##################################################################################
# Este programa tem o objetivo de buscar o conteúdo da página inicial do website
# oficial da Biblioteca Online da Torre de Vigia referente ao texto do dia na 
# publicação Examine as Escrituras Diariamente. Ele busca o cabeçalho contendo a
# data do dia em que se executa o programa, o versículo bíblico para aquele dia e
# os comentários retirados da revista A Sentinela a respeito daquele versículo e
# os transcreve em um arquivo .txt.

# This program is intended to fetch content from the home page of the Watchtower
# Online Library official website regarding the versicle of the day in the
# publication Examining the Scriptures Daily. It searches the header containing
# the date of the day you're running the program, the Bible verse for that day,
# and the Watchtower comment about that verse and transcribes them into a .txt
# file.



# OBSERVAÇÃO: Estou tendo dificuldades com o html que vem da requisição HTTP feita
# pela biblioteca 'requests'. Há dias em que executo o programa e o texto
# daquele dia não está no html recebido. Sugestões quanto a isso são muito bem-
# vindas.

# NOTE: I'm having difficulties with the html that comes from the HTTP request
# made by the 'requests' library. There are days when I run the program and
# the text for that day is not in the html received. Suggestions in this regard
# are most welcome.

# Definindo função que junta as informações necessárias para o texto do dia em que
# o progaram é executado.
# Defining function that gathers needed information for the text of the day that
# the program runs.
def gather_info(url):
    # Solicitando html por meio da biblioteca requests.
    # Requesting html with the rquests library.
    gross_html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'})
    # Formatando data do dia atual de acordo com parâmetro da div em que o texto
    # se encontra.
    # Formatting current day's date according to the parameter of the div
    # containing the text.
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
