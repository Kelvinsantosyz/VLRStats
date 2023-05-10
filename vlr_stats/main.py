from bs4 import BeautifulSoup
import requests

class Vlranalyzer:
    def __init__(self, url):
        self.url = url
        self._page = requests.get(url)
        self._soup = BeautifulSoup(self._page.content, "html.parser")
        
class Get_team_stats(Vlranalyzer):
    def __init__(self, url):
        super().__init__(url)

    def get_team_names(self):
        nomes = []
        for nome in self._soup.find_all("div", class_="team-roster-item-name-alias"):
            nomes.append(nome.text.strip())
        return nomes

    def get_page_title(self):
        titulo = self._soup.find("h1", class_="wf-title")
        return titulo.text.strip()

    def current_rank(self):
        rank_team = self._soup.find("div", class_="rank-num mod-")
        country_team = self._soup.find("div", class_="rating-txt")
        rating_team = self._soup.find("div", class_="rating-num")
        record_team = self._soup.find("div", class_="team-rating-info-section mod-streak")
        win_span = record_team.find("span", class_="win")
        lose_span = record_team.find("span", class_="loss")
        data = {
            "Team": [self.get_page_title()],
            "Players": [", ".join(self.get_team_names())],
            "Rank": [rank_team.text.strip() if rank_team else ""],
            "Country": [country_team.text.strip() if country_team else ""],
            "Rating": [rating_team.text.strip() if rating_team else ""],
            "Wins": [win_span.text.strip() if win_span else ""],
            "Loses": [lose_span.text.strip() if lose_span else ""],
        }
        print(data)

        return data

class TeamStats(Vlranalyzer):
    def __init__(self, url):
        super().__init__(url)  
        rows= self._soup.select("tbody > tr:not(.mod-toggle)")
        self.maps = dict()

        for row in rows:
            cols = row.find_all("td")
            map = cols[0].text.strip().split(' ')
            name = map[0]
            self.maps[name]={
                "played" : int(map[1][1:-1]),
                "win_rate" : int(cols[2].text.strip()[:-1]),  
                "win_number": int(cols[3].text.strip()[0:]),
                "l_number" : int(cols[4].text.strip()[0:]),
                "atk1_st" :int(cols[5].text.strip()[0:]),
                "def1_st" : int(cols[6].text.strip()[0:]),
                "atkwin_rate" :int(cols[7].text.strip()[:-1]),
                "rw_atk" : int(cols[8].text.strip()[0:]),
                "rl_atk" :int(cols[9].text.strip()[0:]),
                "defwin_rate": int(cols[10].text.strip()[:-1]),
                "rw_def": int(cols[11].text.strip()[0:]),
                "rl_def": int(cols[12].text.strip()[0:]),
                "comp": []
            }
            comp_elements = cols[13].find_all('div',class_='agent-comp-agg')
            for element in comp_elements: 
                agents = element.find_all("img")
                comp_number = int(element.find_all('span')[1].text.strip()[1:-1])
                agent_names = [agent["src"].split("/")[-1].split(".")[0] for agent in agents]
                self.maps[name]["comp"].append({
                    'number':comp_number,
                    'agents': agent_names,
                })
        
        return(self.maps)

class MatchAnalyzer(Vlranalyzer):
    def __init__(self, url):
        super().__init__(url)
        
    def players(self):
        table = self._soup.find("div", class_='vm-stats-game')
        rows = table.select("tbody > tr:not(.mod-toggle)")
        stats_player = []
        
        for row in rows:
            cols = row.find_all("td")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            team = cols[0].find('div',class_='ge-text-light').text.strip()
            value = (f'{stats_player}:{team}')
            print (value)
    
    def agents(self):
        table = self._soup.find("div", class_='vm-stats-game')
        rows = table.select("tbody > tr:not(.mod-toggle)")
        agents_list = []
        
        for row in rows:
            cols = row.find_all("td")
            stats_agents = cols[1].find_all("span", class_='stats-sq mod-agent small')
            agent_data = []
            for agent in stats_agents:
                agent_img = agent.find('img').get('alt').strip()

                agent_data.append({agent_img,})
            agents_list.append(agent_data)
        return agents_list
                
    def rating_all(self):
        table = self._soup.find("div", class_='vm-stats-game mod-active')
        rows = table.select("tbody > tr:not(.mod-toggle)")
    
        for row in rows:
            cols = row.select("td")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            rating = cols[2].find_all('span',class_='side mod-side mod-both')
            
            for i, r in enumerate(rating):
                if i % 5 == 0:
                    print(stats_player.split()[i//5], r.text, end=" ")
                print()
  
    def rating_all_tr(self):
        table = self._soup.find("div",class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        
        for row in rows:
            cols = row.select("td")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            rating_all_ct = cols[2].find_all("span",class_="side mod-side mod-t")
            
            for i, r in enumerate(rating_all_ct):
                if i % 5 == 0:
                    print(stats_player.split()[i//5], r.text, end=" ")

    def rating_all_ct(self):
        table = self._soup.find("div",class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        
        for row in rows:
            cols = row.select("td")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            rating_all_ct = cols[2].find_all("span",class_="side mod-side mod-ct")
            
            for i, r in enumerate(rating_all_ct):
                if i % 5 == 0:
                    print(stats_player.split()[i//5], r.text, end=" ")

  
  
    def acs_all(self):
        table = self._soup.find("div",class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        
        for row in rows:
            cols = row.select("td")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            acs_all = cols[3].find_all("span",class_="side mod-side mod-both")
            for i, r in enumerate(acs_all):
                if i % 5 == 0:
                    print(stats_player.split()[i//5], r.text, end=" ")
                print()
    def acs_all_tr(self):
        table = self._soup.find("div",class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        
        for row in rows:
            cols = row.select("td")
            acs_tr = cols[3].find_all("span",class_="side mod-side mod-t")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            
            for i, r in enumerate(acs_tr):
                if i % 5 == 0:
                    print(stats_player.split()[i//5], r.text, end=" ")
                    
    def acs_all_ct(self):
        table = self._soup.find("div",class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        
        for row in rows:
            cols = row.select("td")
            stats_player = cols[0].find('div',class_='text-of').text.strip()
            acs_ct = cols[3].find_all("span",class_="side mod-side mod-ct")
            
            for i, r in enumerate(acs_ct):
                if i% 5 ==0:
                    print(stats_player.split()[i//5], r.text, end=" ")
                    
    def kda_all(self):
        table = self._soup.find("div", class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        teams = {} 

        for row in rows:
            cols = row.select("td")
            player = cols[0].find('div',class_='text-of').text.replace('\n', '').replace('\t', '').strip()
            team = cols[0].find('div',class_='ge-text-light').text.replace('\n', '').replace('\t', '').strip()
            kills = cols[4].find_all("span", class_="side mod-side mod-both")
            deaths = cols[5].find_all("span", class_="side mod-both")
            ass = cols[6].find_all("span", class_="side mod-both")

            kda = f"{kills[0].text}/{deaths[0].text}/{ass[0].text}"
            
            if team not in teams:
                teams[team] = []
                
            teams[team].append((player, kda))

        for team, players in teams.items():
            print()
            print(f"{team}:")
            for i, player in enumerate(players, 1):
                print()
                print(f"{i}.{player[0]}({player[1]})")
           

    def kda_all_tr(self):
        table = self._soup.find("div", class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        teams = {} 

        for row in rows:
            cols = row.select("td")
            player = cols[0].find('div',class_='text-of').text.replace('\n', '').replace('\t', '').strip()
            team = cols[0].find('div',class_='ge-text-light').text.replace('\n', '').replace('\t', '').strip()
            kills = cols[4].find_all("span", class_="side mod-side mod-t")
            deaths = cols[5].find_all("span", class_="side mod-t")
            ass = cols[6].find_all("span", class_="side mod-t")

            kda = f"{kills[0].text}/{deaths[0].text}/{ass[0].text}"
            
            if team not in teams:
                teams[team] = []
                
            teams[team].append((player, kda))

        for team, players in teams.items():
            print()
            print(f"{team}:")
            for  player in enumerate(players, 1):
                print()
                print(f"{player[0]}({player[1]})")

    def kda_all_ct(self):
        table = self._soup.find("div", class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        teams = {}
        for row in rows:
            cols = row.select("td")
            player = cols[0].find('div',class_='text-of').text.replace('\n', '').replace('\t', '').strip()
            team = cols[0].find('div',class_='ge-text-light').text.replace('\n', '').replace('\t', '').strip()
            kills = cols[4].find_all("span", class_="side mod-side mod-ct")
            deaths = cols[5].find_all("span", class_="side mod-ct")
            ass = cols[6].find_all("span", class_="side mod-ct")
            kda = f"{kills[0].text}/{deaths[0].text}/{ass[0].text}"
            
            if team not in teams:
                teams[team] = []
                
            teams[team].append((player, kda))

        for team, players in teams.items():
            print()
            print(f"{team}:")
            for  player in enumerate(players, 1):
                print()
                print(f"{player[0]}({player[1]})")
                
        
    def fk_fd_all(self):
        table = self._soup.find("div", class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        teams_output = []
        teams = {}
        for row in rows:
            cols = row.select("td")
            player = cols[0].find('div',class_='text-of').text.replace('\n', '').replace('\t', '').strip()
            team = cols[0].find('div',class_='ge-text-light').text
            fk = cols[11].find("span",class_="side mod-both").text
            fd = cols[12].find("span",class_="side mod-both").text

            if team not in teams:
                teams[team] = []

            teams[team].append((player, fk, fd))

        for team, players in teams.items():
            print()
            teams_output.append(f"{team}:")
            for i, player in enumerate(players, 1):
                teams_output.append(f"{i}:{player[0]:<20}{player[1]:>10}/{player[2]:<5}")
                print(player)
        return player
    
    
    def fk_fd_tr_all(self):
        table = self._soup.find("div", class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")
        teams_output = []
        teams = {}
        for row in rows:
            cols = row.select("td")
            player = cols[0].find('div',class_='text-of').text.replace('\n', '').replace('\t', '').strip()
            team = cols[0].find('div',class_='ge-text-light').text
            fk = cols[11].find("span",class_="side mod-t").text
            fd = cols[12].find("span",class_="side mod-t").text

            if team not in teams:
                teams[team] = []

            teams[team].append((player, fk, fd))

        for team, players in teams.items():
            teams_output.append(f"{team}:")
            for i, player in enumerate(players, 1):
                teams_output.append(f"{i}:{player[0]:<20}{player[0]:>10}/{player[0]:<5}")
                print(player)
       
        return player
    
    
    def fk_fd_ct_all(self):
        table = self._soup.find("div", class_="vm-stats-game mod-active")
        rows = table.select("tbody > tr:not(.mod-toggle)")

        teams_output = []
        teams = {}
        for row in rows:
            cols = row.select("td")
            player = cols[0].find('div',class_='text-of').text.replace('\n', '').replace('\t', '').strip()
            team = cols[0].find('div',class_='ge-text-light').text
            fk = cols[11].find("span",class_="side mod-ct").text
            fd = cols[12].find("span",class_="side mod-ct").text

            if team not in teams:
                teams[team] = []

            teams[team].append((player, fk, fd))

        for team, players in teams.items():
            print()
            teams_output.append(f"{team}:")
            for i, player in enumerate(players, 1):
                teams_output.append(f"{i}:{player[0]:<20}{player[1]:>10}/{player[2]:<5}")
                print(player)
        
        return player

class MatchAnalyzer_map1(Vlranalyzer):
    def __init__(self, url):
        super().__init__(url)

    def result_map1(self):
        table = self._soup.select('div.vm-stats-game-header')
        table1 = self._soup.select('div.team-name')
        team1_name = table1[0].text.strip()
        team2_name = table1[1].text.strip()
        score_1 = table[0].select('div.score')[1].text.strip()
        score_2 = table[0].select('div.score')[0].text.strip()
        map_elements = self._soup.find("div", class_='map')
        map_play = map_elements.find("span").text.replace('\n', '').replace('\t', '').strip()
        map_duration = map_elements.find("div", class_='map-duration ge-text-light').text.strip()
        stats_players = []
        table = self._soup.find("div", class_='vm-stats-game')
        rows = table.select("tbody > tr:not(.mod-toggle)")
        for row in rows:
            cols = row.find_all("td")
            stats_player = cols[0].find('div', class_='text-of').text.strip()
            stats_players.append(stats_player)

        data = {
            "Team": [f'{team1_name} / {team2_name}'],
            "Result": [f'{score_1} / {score_2}'],
            "Map": [map_play],
            "Time": [map_duration],
            "Players": stats_players
        }
        return data
          
class MatchAnalyzer_map2(Vlranalyzer):
    
    def __init__(self, url):
        super().__init__(url)
        
    def result_map2(self):
        table = self._soup.select('div.vm-stats-game-header')
        table1 = self._soup.select('div.team-name')
        team1_name = table1[0].text.strip()
        team2_name = table1[1].text.strip()
        score_1 = table[1].select('div.score')[0].text.strip()
        score_2 = table[1].select('div.score')[1].text.strip()
        map_elements = table[1].find("div", class_='map')
        map_play = map_elements.find("span").text.replace('\n', '').replace('\t', '').strip()
        map_duration = map_elements.find("div", class_='map-duration ge-text-light').text.strip()
        stats_players = []
        table = self._soup.find("div", class_='vm-stats-game')
        rows = table.select("tbody > tr:not(.mod-toggle)")
        for row in rows:
            cols = row.find_all("td")
            stats_player = cols[0].find('div', class_='text-of').text.strip()
            stats_players.append(stats_player)

        data = {
            "Team": [f'{team1_name} / {team2_name}'],
            "Result": [f'{score_1} / {score_2}'],
            "Map": [map_play],
            "Time": [map_duration],
            "Players": stats_players
        }
        return(data)
    
class MatchAnalyzer_map3(Vlranalyzer):
    def __init__(self, url):
        super().__init__(url)
        
    def result_map3(self):
        try:
            table = self._soup.select('div.vm-stats-game-header')
            table1 = self._soup.select('div.team-name')
            team1_name = table1[0].text.strip()
            team2_name = table1[1].text.strip()
            score_1 = table[2].select('div.score')[0].text.strip()
            score_2 = table[2].select('div.score')[1].text.strip()
            map_elements = table[2].find("div", class_='map')
            map_play = map_elements.find("span").text.replace('\n', '').replace('\t', '').strip()
            map_duration = map_elements.find("div", class_='map-duration ge-text-light').text.strip()
            stats_players = []

            table = self._soup.find("div", class_='vm-stats-game')
            rows = table.select("tbody > tr:not(.mod-toggle)")
            for row in rows:
                cols = row.find_all("td")
                stats_player = cols[0].find('div', class_='text-of').text.strip()
                stats_players.append(stats_player)

            data = {
                "Team": [f'{team1_name} / {team2_name}'],
                "Result": [f'{score_1} / {score_2}'],
                "Map": [map_play],
                "Time": [map_duration],
                "Players": stats_players
            }
           
        except IndexError as e:
            raise ValueError("Unable to retrieve match information. Please verify that the page is correct.") from e
        
        return data


