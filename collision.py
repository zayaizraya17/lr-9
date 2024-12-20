from collision.CorrectRect import isCorrectRect, RectCorrectError

def intersectionAreaRect(rec): 
    area = 0  

    try:
        isCorrectRect(rec)
    except RectCorrectError as e:
        print(e)
        return 0  
    
    n = len(rec)  # Количество прямоугольников 
    is_intersection = False  # Есть ли пересечения

    for i in range(n):
        for j in range(i + 1, n):
            # Границы 1го прямоугольника
            x1, y1 = rec[i][0]
            x2, y2 = rec[i][1]

            # Границы 2го прямоугольника
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

            # Площадь пересечения
            if width > 0 and height > 0:
                area += width * height  
                is_intersection = True  

    if not is_intersection:
        return 0

    return area  