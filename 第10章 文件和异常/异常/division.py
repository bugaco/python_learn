try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('没毛病')