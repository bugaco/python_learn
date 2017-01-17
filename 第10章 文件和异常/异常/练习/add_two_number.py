while True:
    number1 = input('请输入第一个数字：')
    number2 = input('请输入第二个数字：')
    try:
        sum = int(number1) + int(number2)
    except ValueError:
        # print('输入的值无效')
        pass
    else:
        print(str(sum))
