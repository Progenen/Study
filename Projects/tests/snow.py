import turtle
import random

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Снежинки")

# Настройка черепашки
snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.color("white")
snowflake.hideturtle()

def draw_branch(size, levels):
    """
    Рисует ветвь снежинки рекурсивно.
    :param size: Длина ветки
    :param levels: Глубина рекурсии
    """
    if levels == 0:
        snowflake.forward(size)
        snowflake.backward(size)
        return
    
    snowflake.forward(size / 3)
    snowflake.left(45)
    draw_branch(size / 2, levels - 1)
    snowflake.right(90)
    draw_branch(size / 2, levels - 1)
    snowflake.left(45)
    snowflake.backward(size / 3)

def draw_snowflake(size, levels, branches):
    """
    Рисует снежинку с указанным количеством ветвей.
    :param size: Длина основной ветви
    :param levels: Глубина рекурсии
    :param branches: Количество ветвей
    """
    for _ in range(branches):
        draw_branch(size, levels)
        snowflake.right(360 / branches)

# Генерация нескольких снежинок
for _ in range(8):  # Количество снежинок
    snowflake.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    snowflake.goto(x, y)
    snowflake.pendown()
    size = random.randint(50, 150)
    levels = random.randint(2, 4)
    branches = random.randint(6, 10)
    draw_snowflake(size, levels, branches)

# Завершение программы
screen.mainloop()