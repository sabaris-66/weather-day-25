import pandas

sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
sq_dict = {'grey': 0,
           'red': 0,
           'black': 0}
for fur_color in sq_data["Primary Fur Color"].to_list():
    if fur_color == "Gray":
        sq_dict["grey"] += 1
    elif fur_color == "Cinnamon":
        sq_dict["red"] += 1
    elif fur_color == "Black":
        sq_dict["black"] += 1
print(sq_dict)
sq_data_frame = pandas.DataFrame.from_dict(sq_dict, orient='index')
sq_data_frame.to_csv("sq_data.csv")
print(sq_data_frame)
# from statistics import mean
# with open("weather_data.csv") as file:
#     weekly_weather = file.readlines()
# print(weekly_weather)
#
new_method = pandas.read_csv("weather_data.csv")
# print(new_method)
# print(new_method['day'])
to_find_avg = new_method.to_dict()
print(to_find_avg)
# print(to_find_avg)
# print(round(mean(to_find_avg)))
# print(sum(to_find_avg)/len(to_find_avg))
# max_temp = new_method["temp"].max()
# print(new_method.condition)
# print(new_method[new_method['temp'] == max_temp])
# monday = new_method[new_method.day == 'Monday']
# print(monday.temp[0]*9/5+32)