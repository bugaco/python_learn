with open('other/hello.txt') as file_object:
    line = file_object.readline(100)
    print(line)