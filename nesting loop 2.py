rows = input("Input a list of weather: ").split()
cols = ["windy", "breezy", "calm"]

weather_list = [[row + " " + col for col in cols] for row in rows]

print(weather_list)
