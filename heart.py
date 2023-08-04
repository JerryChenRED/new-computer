import turtle

# 設置畫布和海龜
screen = turtle.Screen()
screen.setup(800, 600)  # 設置畫布大小
screen.bgcolor("white")
screen.title("Filled and Rotating Heart")
heart = turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.speed(1)

# 計算愛心的寬度和高度
heart_width = 100
heart_height = 88

# 定義愛心函數
def draw_heart():
    heart.penup()
    heart.goto(-heart_width/2, heart_height/2)
    heart.pendown()
    heart.begin_fill()
    heart.left(50)
    heart.forward(133)
    heart.circle(50, 200)
    heart.right(140)
    heart.circle(50, 200)
    heart.forward(133)
    heart.end_fill()

# 塗滿愛心
draw_heart()

# 設定愛心的轉速
turtle_speed = 0.00000000005  # 調整這個值來改變轉速，值越大轉速越快

# 主程式
heart.hideturtle()
heart.speed(turtle_speed)  # 設定愛心的轉速
screen.tracer(0)  # 關閉自動更新畫面

# 讓愛心轉個圈函數
def rotate_heart():
    for angle in range(0, 360, 5):  # 變化愛心的角度
        heart.clear()  # 清除之前的愛心
        heart.begin_fill()  # 開始填充
        heart.setheading(angle)  # 設置愛心的角度
        draw_heart()
        heart.end_fill()  # 結束填充
        screen.update()  # 更新畫面

rotate_heart()

turtle.done()



