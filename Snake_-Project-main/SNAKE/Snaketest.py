x = [0, 10, 20, 30]
y = [0, 10, 20, 30]
color = [0, 10, 20, 30]

snake = x, y, color


def dead(snake):
    ret = False
    x, y, H = snake
    for i in range(2, len(x)):
        if (x[i] - x[0])**2 + (y[i] - y[0])**2 < 5:
            ret = True
    if x[0] > 200 or x[0] < 0 or y[0] > 200 or y[0] < 0: 
        ret = True       
    return ret

dead(snake)