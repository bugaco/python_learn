import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, value in enumerate(header_row):
        print(index, value)
    header_row = next(reader)

    for index, value in enumerate(header_row):
        print(index, value)

    temperatures = []
    dates = []
    for row in reader:
        temperature = float(row[1])
        temperatures.append(temperature)

        date = datetime.strptime(row[14], "%Y-%m-%d %H:%M:%S")
        print(date)
        dates.append(date)
    print(temperatures)

# 根据数据绘制图形
    fig = plt.figure(dpi=128)
    plt.plot(dates, temperatures, c='red')

# 设置图形的格式
    plt.title("Tempperatures in one day.", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()