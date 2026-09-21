# playoff_predictor.py
team_name = "Wildcats"

wins = 12
losses = 4

games_played = wins + losses

win_percentage = wins / games_played

if win_percentage >= .58:
    print(team_name, "are likely to make the playoffs!")
else:
    print(team_name, "needs to win more games.")

print("Team:", team_name)

#When checking a condition or using an if statement, 
#make sure to tab! or space.... your choice....
if wins > 10:
    print("Winning season!")

def winning_record(wins, losses):
    return wins > losses

result = winning_record(wins, losses)

print("Winning Record?", result)

#PRINT GAMES PLAYED AND WIN PERCENTAGE
print("Games Played:", games_played)
print("Win Percentage:", win_percentage)
print("Win Percentage:", round(win_percentage * 100, 1), "%")