import requests
from bs4 import BeautifulSoup
import time
class League:
    def __init__(self, name,links,date):
        self.name = name
        self.links = links
        self.date = date

def links_creater(link,pages):
    links = []
    links.append(link)
    i = 2
    while i != (pages + 1):
        links.append(link + "&page=" + str(i))
        i = i + 1
    return links
def get_matchid_of_league(league):
    match_table = {}
    for link in league.links:
        target = link
        # fake UA to bypass Dotabuff's anti spider mechanism
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        r = requests.get(url = target, headers = headers)
        html = r.text
        #print(html)
        bf = BeautifulSoup(html,features="html.parser")
        list_match = []
        for entry in bf.find_all('td',class_ = "cell-mediumlarge"):
            list_match.append(entry)
        #print( len(list_match))
        for match in list_match:
            bf_sub = BeautifulSoup(str(match),features="html.parser")
            match_id = str(bf_sub.a.contents[0])
            date_list = bf_sub.time['datetime'].split('T')
            date = date_list[0]
            match_table[match_id] = date

        time.sleep(1) # limit request rate to prevent unusual traffic toward Dotabuff
        # If code runs normally, we should only request each page once 
        


    return match_table

def differ_qua(matchid_list, split_time):
    return

links_b = links_creater("https://www.dotabuff.com/esports/leagues/10452-the-bucharest-minor-2019/matches?original_slug=10452-the-bucharest-minor-2019",7)
B_Minor = League('Bucharest Minor',links_b,"2019-01-08")
table = get_matchid_of_league(B_Minor)
print(len(table))