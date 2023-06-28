# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
things = {
    'компас': 0.5,
    'спальник': 2,
    'фляжка': 0.8,
    'палатка': 2.5,
    'нож': 0.2,
    'еда': 2,
    'спички': 0.2,
    'котелок': 1.2
}

max_weihgt = 5

sort_things = []
for thing, weigth in things.items():
    sort_things.append((weigth, thing))
sort_things.sort()

backpack = []
total_weigth = 0
for weigth, thing in sort_things:
    if total_weigth + weigth <= max_weihgt:
        backpack.append((thing))
        total_weigth += weigth

print(f"В рюкзак поместятся следующие вещи: {', '.join(backpack)}")