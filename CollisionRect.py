from collision.CorrectRect import isCorrectRect, RectCorrectError

def isCollisionRect(rec):
    
    try:
        isCorrectRect(rec)
    except RectCorrectError as e:
        print(e)
        return False
    n = len(rec)

    for i in range(n): 
        for j in range(i + 1, n):
            # 1-ый прямоугольник
            x1, y1 = rec[i][0]
            x2, y2 = rec[i][1]
            # 2-ой прямоугольник
            x3, y3 = rec[j][0]
            x4, y4 = rec[j][1]
            # Границы пересечения
            left = max(x1, x3)
            top = min(y2, y4)
            right = min(x2, x4)
            bottom = max(y1, y3)
            # Ширина и высота пересечения
            width = right - left
            height = top - bottom
            # Проверяем пересечение
            if width > 0 and height > 0:
                return True  
    return False  