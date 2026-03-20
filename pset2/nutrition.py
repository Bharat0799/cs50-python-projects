fruit = input("Item: ").lower()

calories = {
    "apple": 130,
    "banana": 110,
    "orange": 80,
    "grapefruit": 60,
    "grapes": 90,
    "kiwifruit": 90,
    "pear": 100,
    "peach": 60,
    "pineapple": 50,
    "sweet cherries": 100,
    "avocado": 50
}

if fruit in calories:
    print(calories[fruit])