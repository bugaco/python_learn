import string
people = ['makesi', 'engesi', 'dengbuliduo', 'fudimo']

people[0] = 'rongrong'

people.insert(0, 'Harry')
people.insert(3, 'Luolin')
people.append('gaosilin')

message = "I would like to have a dance with "

print(message + people[0].title() + ".")
print(message + people[1].title() + ".")
print(message + people[2].title() + ".")
print(message + people[3].title() + ".")
print(message + people[4].title() + ".")
print(message + people[5].title() + ".")
print(message + people[6].title() + ".")

