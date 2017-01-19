import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'history-2016'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, value in enumerate(header_row):
        print(index, value)
    header_row = next(reader)

    for index, value in enumerate(header_row):
        print(index, value)

    highs, lows, avgs = [], [], []
    dates = []
    for row in reader:

        try:
            high = float(row[1])
            avg = float(row[2])
            low = float(row[3])
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            avgs.append(avg)
            lows.append(low)
            dates.append(current_date)

# 根据数据绘制图形
    fig = plt.figure(dpi=128)
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# 设置图形的格式
    plt.title("Tempperatures in one 2016.", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()