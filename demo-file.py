import pandas as pd


data = {
    'Username': ['Viper', 'Ghost', 'Shadow', 'Nova', 'Apex'],
    'Device': ['iPhone 15', 'Android', 'Mac', 'Android', 'iPhone 15'],
    'Control_Layout': ['4-Finger Gyro', '2-Finger', 'Keyboard/Mouse', '4-Finger Gyro', '3-Finger'],
    'Matches_Played': [145, 89, 312, 210, 54],
    'Win_Rate_Pct': [22.5, 12.0, 18.4, 28.1, 8.5]
}


df = pd.DataFrame(data)


df.to_csv('player_stats.csv', index=False)

print("Success! The file 'player_stats.csv' has been generated.")