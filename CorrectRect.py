class RectCorrectError(Exception):
    pass

def isCorrectRect(rec):
    count = 0

    for i in rec:
        if i[0][0] >= i[1][0] or i[0][1] >= i[1][1]:
            raise RectCorrectError(f'Один из прямоугольников некорректный номер {count}')
    return True
             