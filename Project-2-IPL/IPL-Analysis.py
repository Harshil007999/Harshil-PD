import pandas as pd


matches = pd.read_csv('matches.csv')

print("Shape:", matches.shape)
print("\nColumns:", matches.columns.tolist())
print("\nMissing values:\n", matches.isnull().sum())


total_matches = len(matches)
print(f"\n1. Total matches played: {total_matches}")


most_wins = matches['winner'].value_counts()
print(f"\n2. Top 5 teams by wins:\n{most_wins.head()}")


matches_per_season = matches.groupby('season')['id'].count()
print(f"\n3. Matches per season:\n{matches_per_season}")


most_hosted = matches['city'].value_counts()
print(f"\n4. Top 5 hosting cities:\n{most_hosted.head()}")


matches['toss_match_winner'] = matches['toss_winner'] == matches['winner']
toss_win_rate = matches['toss_match_winner'].mean() * 100
print(f"\n5. Toss winner also won the match: {toss_win_rate:.1f}%")


toss_decision = matches['toss_decision'].value_counts()
print(f"\n6. Toss decision counts:\n{toss_decision}")


best_player = matches['player_of_match'].value_counts()
print(f"\n7. Top 5 players of the match:\n{best_player.head()}")


top_venues = matches['venue'].value_counts()
print(f"\n8. Top 5 venues:\n{top_venues.head()}")


biggest_win = matches.loc[matches['win_by_runs'].idxmax()]
print(f"\n9. Biggest win by runs:")
print(biggest_win[['season', 'team1', 'team2', 'winner', 'win_by_runs']])


most_toss_wins = matches['toss_winner'].value_counts()
print(f"\n10. Top 5 toss winners:\n{most_toss_wins.head()}")