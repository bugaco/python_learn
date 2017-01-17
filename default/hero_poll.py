heros = {}
polling_active = True
while polling_active:
    name = input("您的名字是？")
    hero = input("您最喜欢的英雄是？")
    heros[name] = hero

    repeat = input("是否继续呢？")
    if repeat == 'no':
        polling_active = False
print(heros)
