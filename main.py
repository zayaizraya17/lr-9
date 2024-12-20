import json

count = 0


def save_flowers(flowers, filename="dump.json"):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(flowers, f, indent=4, ensure_ascii=False)

def print_all_flowers(flowers):
    if not flowers:
        print("Нет записей о цветах.")
        return
    for flower in flowers:
        print(f"""Номер цветка: {flower["id"]} 
    Название: {flower["name"]}
    Латинское название: {flower["latin_name"]}
    Краснокнижный цветок? {flower["is_red_book_flower"]}
    Цена: {flower["price"]} BYN\n""")

def print_flower_by_id(flowers, flower_id):
    for i, flower in enumerate(flowers):
        if flower['id'] == flower_id:
            print(f"""Номер цветка: {flower["id"]} 
    Название: {flower["name"]}
    Латинское название: {flower["latin_name"]}
    Краснокнижный цветок? {flower["is_red_book_flower"]}
    Цена: {flower["price"]} BYN\n""")
            return
    print(f"Запись с ID {flower_id} не найдена.")

def add_flower(flowers):
    flower_id = max(flower["id"] for flower in flowers) + 1

    while True:
            name = input("Введите названия цветка ")
            if name != "":
                break
            else:
                print("Вы не ввели")

    while True:
        latin_name = input("Введите латинское имя цветка ")
        if latin_name != "":
            break
        else:
            print("Вы не ввели")

    while True:
        is_red_book_flower = input("Введите краснокнижный ли цветок True/False ")
        if is_red_book_flower.lower() in ["true", "false"]:
            is_red_book_flower = is_red_book_flower.lower() == "true"
            break
        else:
            print("Некорректный ввод")

    while True: 
        try: 
            price = float(input("Введите цену цветка ")) 
            break 
        except ValueError: 
            print("Некорректный ввод") 

    flowers.append({
        "id": flower_id,
        "name": name,
        "latin_name": latin_name,
        "is_red_book_flower": is_red_book_flower,
        "price": price
    })
    print("Запись добавлена.")

def delete_flower_by_id(flowers, flower_id):
    for i, flower in enumerate(flowers):
        if flower['id'] == flower_id:
            del flowers[i]
            print(f"Запись с ID {flower_id} удалена.")
            return
    print(f"Запись с ID {flower_id} не найдена.")

def main():
    with open('dump.json', 'r', encoding='utf-8') as file:
        flowers = json.load(file)
    count = 0
    while True:
        print("\nМеню:")
        print(" 1 Вывести все записи\n 2 Вывести запись по полю\n 3 Добавить запись\n 4 Удалить запись по полю\n 5 Выйти из программы")

        choice = input("Что выберете? ")
        if choice == "1":
            print_all_flowers(flowers)
            count += 1
        elif choice == "2":
            flower_id = int(input("Введите ID записи: "))
            print_flower_by_id(flowers, flower_id)
            count += 1
        elif choice == "3":
            add_flower(flowers)
            count += 1
        elif choice == "4":
            flower_id = int(input("Введите ID записи для удаления: "))
            delete_flower_by_id(flowers, flower_id)
            count += 1
        elif choice == "5":
            print(f"Выполнено операций: {count}")
            break
        else:
            print("Неверный выбор.")
        save_flowers(flowers)

main()

from collision.CorrectRect import isCorrectRect, RectCorrectError
from collision.CollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect 
def main():
    while True:
        num = int(input("Выберите: 1. isCorrectRect, 2. isCollisionRect, 3. intersectionAreaRect, 4. intersectionAreaMultiRect, 5. Выход:"))
       
        if num == 1:
            rec = []
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rec.append([(x1,y1), (x2,y2)])
            try:
                print(isCorrectRect(rec))
            except RectCorrectError as e:
                print(e)
        
        elif num == 2:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [(x1, y1), (x2, y2)],[(x3, y3), (x4, y4)]
            print(f"Пересекаются ли прямоугольники: ", isCollisionRect(rectangles))
        
        elif num ==3:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [(x1, y1), (x2, y2) ],[(x3, y3), (x4, y4)]
            print(f"Площадь пересечения: ", intersectionAreaRect(rectangles))

        elif num == 4:
            n = int(input("Кол-во прямоугольников: "))
            rectangles = []
            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                rectangles.append([(x1, y1), (x2, y2)])
            else:  
                try:
                    print(f"Уникальная площадь пересечения: ", intersectionAreaMultiRect(rectangles))
                except RectCorrectError as e:
                    print(e)
                    return 0
        elif num == 5:
            print("Вы вышли из программы")
            break
        else:
            print("Некорректный пункт. Выберите другой")
main()