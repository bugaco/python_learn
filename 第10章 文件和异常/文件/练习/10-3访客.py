guest_name = input('来访者请先登记，输入您的名字：')
print('Welcom, ', guest_name)
file_name = 'guest_2.txt'
with open(file_name, 'a') as file_object:
    file_object.write(guest_name + '\n')
