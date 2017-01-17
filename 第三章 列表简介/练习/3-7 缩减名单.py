import string
people = ['makesi', 'engesi', 'dengbuliduo', 'fudimo']

people[0] = 'rongrong'

people.insert(0, 'Harry')
people.insert(3, 'Luolin')
people.append('gaosilin')

print(people)
print("--------")

sorry_message =  "we are sorry about that"
people1 = people.pop(0)
print(people1 + ", " + sorry_message)

sorry_message =  "we are sorry about that"
people1 = people.pop(0)
print(people1 + ", " + sorry_message)

sorry_message =  "we are sorry about that"
people1 = people.pop(0)
print(people1 + ", " + sorry_message)

sorry_message =  "we are sorry about that"
people1 = people.pop(0)
print(people1 + ", " + sorry_message)

sorry_message =  "we are sorry about that"
people1 = people.pop(0)
print(people1 + ", " + sorry_message)


message = "I would like to have a dance with "

print("\n")
print(message + people[0].title() + ".")
print(message + people[1].title() + ".")

del people[0]
del people[0]
print(people)




