# VLR Stats
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a project that uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to scrape data from matches of the game [Valorant](https://playvalorant.com/en-us/).

With this project, you can obtain player and team statistics, as well as match results and maps played.

## Prerequisites

Before you start, you need to have Python 3 installed on your machine.

## Installation

1. Clone the repository using `gh repo clone Kelvinsantosyz/VLRStats`.
2. Install the project dependencies using the command `pip install -r requirements.txt`.

## How to use

To use the project, follow these steps:

1. ``` import vlr_stats```
3. Insert the URL of the team you want to see the rank of. Example: `https://www.vlr.gg/team/6961/loud`
4. Insert the URL of the match you want to analyze. Example: `https://www.vlr.gg/183809/loud-vs-100-thieves-champions-tour-2023-americas-league-w6`.
5. Choose which type of analysis you want to perform:

- Team and roster information: `Get_team_stats(url)`
  - `current_rank()` - current team ranking

- Played maps and agents: `TeamStats(url)`

- Overall match statistics: `MatchAnalyzer(url)`
  - `players()` - list of team players
  - `agents()` - win rate by used agent
  - `rating_all()` - overall team rating in all matches
  - `rating_all_ct()` - overall team rating when playing as CT
  - `rating_all_tr()` - overall team rating when playing as TR
  - `acs_all()` - overall team ACS (Average Combat Score) in all matches
  - `acs_all_ct()` - overall team ACS when playing as CT
  - `acs_all_tr()` - overall team ACS when playing as TR
  - `kda_all()` - overall team KDA (Kill/Death/Assist) in all matches
  - `kda_all_ct()` - overall team KDA when playing as CT
  - `kda_all_tr()` - overall team KDA when playing as TR
  - `fk_fd_all()` - overall team first kills/first deaths in all matches
  - `fk_fd_ct_all()` - overall team first kills/first deaths when playing as CT
  - `fk_fd_tr_all()` - overall team first kills/first deaths when playing as TR

- First map statistics: `MatchAnalyzer_map1(url)`
  - `result_map1()` - result of the first map

- Second map statistics: `MatchAnalyzer_map2(url)`
  - `result_map2()` - result of the second map

- Third map statistics: `MatchAnalyzer_map3(url)`
  - `result_map3()` - result of the third map (if played)

## Contributing

This project is open source and anyone can contribute. If you find any issues or have any ideas to improve it, feel free to open an issue or submit a pull request.
