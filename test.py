import vlr_stats


url = "https://www.vlr.gg/team/6961/loud"
match_analyzer = vlr_stats.Get_team_stats(url)
output_list = match_analyzer.current_rank() 
print(output_list)
