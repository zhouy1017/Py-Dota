import requests
from bs4 import BeautifulSoup
import time
class League:
    def __init__(self, name,links,date):
        self.name = name
        self.links = links
        self.date = date # the date is the split date instead of starting date of the tournament

def links_creater(link,pages):
    links = []
    links.append(link)
    i = 2
    while i != (pages + 1):
        links.append(link + "&page=" + str(i))
        i = i + 1
    return links

def date_compare(date1,date2):
    date1_list = date1.split("-")
    date2_list = date2.split("-")
    i = 0
    while i < 3:
        if date1_list[i] == date2_list[i]:
            i = i + 1
            continue
        if date1_list[i] > date2_list[i]:
            return 0
        else:
            return 1
        
    raise Exception('the split date should not equal to any actual match date.')

def get_matchid_of_league(league):
    match_table = {}
    qualifier = []
    main_event = []
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
            if date_compare(date,league.date) == 1:
                qualifier.append(match_id)
            else:
                main_event.append(match_id)

        time.sleep(1) # limit request rate to prevent unusual traffic toward Dotabuff
        # If code runs normally, we should only request each page once 
        


    return match_table, qualifier, main_event



def differed_id(league_name):
    league = None
    if league_name == "Bucharest Minor":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10452-the-bucharest-minor-2019/matches?original_slug=10452-the-bucharest-minor-2019",7)
        league = League('Bucharest Minor',links_b,"2019-01-08")
    if league_name == "DreamLeague S10":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10326-dreamleague-season-10/matches?original_slug=10326-dreamleague-season-10",8)
        league = League('DreamLeague S10',links_b,"2018-10-28")    
    if league_name == "DreamLeague S11":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10681-dreamleague-season-11/matches?original_slug=10681-dreamleague-season-11",23)
        league = League('DreamLeague S11',links_b,"2019-03-12")  
    if league_name == "SL-i Minor":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10733-starladder-imbatv-dota2-minor/matches?original_slug=10733-starladder-imbatv-dota2-minor",7)
        league = League('SL-i Minor',links_b,"2019-03-05")  
    if league_name == "Kuala Lumpur Major":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10296-the-kuala-lumpur-major/matches?original_slug=10296-the-kuala-lumpur-major",20)
        league = League('Kuala Lumpur Major',links_b,"2018-11-07")  
    if league_name == "Chongqing Major":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10482-the-chongqing-major/matches?original_slug=10482-the-chongqing-major",15)
        league = League('Chongqing Major',links_b,"2019-01-17")    
    if league_name == "Paris Major":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10810-mdl-disneyland-paris-major/matches?original_slug=10810-mdl-disneyland-paris-major",12)
        league = League('Paris Major',links_b,"2019-05-02")   
    if league_name == "PIT Minor":
        links_b = links_creater("https://www.dotabuff.com/esports/leagues/10869-amd-sapphire-dota-pit-minor-2019/matches?original_slug=10869-amd-sapphire-dota-pit-minor-2019",6)
        league = League('PIT Minor',links_b,"2019-04-20")     
    
    table,qualifier,main_event = get_matchid_of_league(league)
    return table, qualifier, main_event
    

