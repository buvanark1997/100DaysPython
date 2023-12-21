import csv
with open("weather_data.csv") as datafile:
    data = csv.reader(datafile)
    temperature = []
    for row in data:
        # filter only temperature
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    # print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# filter only temperature
print(data["temp"])
# to convert csv data to dictionary
print(data.to_dict())
# to list
print(data["temp"].to_list())
#to take avarage temperature
print(data["temp"].mean())
#to take row wise
print(data[data["day"]=="Monday"])
print(data[data.day =="Monday"])
#to print the row with high temperature
print(data[data.temp == data["temp"].max()])
print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
data_dict = {
    "students":["amy","jacob","margret","kayla"],
    "scores":[76,86,93,79]
}
data = pandas.DataFrame(data_dict)
data.to_csv("generatedCSV.csv")

csv_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#filter the squirrels by colors and take its count
gray_colored_squirrels = len(csv_data[csv_data["Primary Fur Color"] == "Gray"])
red_colored_squirrels = len(csv_data[csv_data["Primary Fur Color"] == "Red"])
black_colored_squirrels = len(csv_data[csv_data["Primary Fur Color"] == "Black"])
data_dict1 = {
    "Fur color":["Gray","Red","Black"],
    "Count":[gray_colored_squirrels,red_colored_squirrels,black_colored_squirrels]
}
df = pandas.DataFrame(data_dict1)
#to write/create a csv file with dictionary
df.to_csv("Filtered_Squirrels.csv")


