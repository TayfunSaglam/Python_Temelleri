import turtle
import random
import time

# === KİŞİYE ÖZEL MESAJ ===

isim = "İsim"  # Buraya istediğin adı yaz
mesaj = f"{isim}, kalbim hep seninle <3"

# === Ekran ve kalem ayarları ===
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Sana Özel Kalp")

kalp = turtle.Turtle()
kalp.pensize(3)
kalp.speed(3)

def draw_big_heart():
    kalp.color("red")
    kalp.begin_fill()
    kalp.left(140)
    kalp.forward(180)
    kalp.circle(-90, 200)
    kalp.left(120)
    kalp.circle(-90, 200)
    kalp.forward(180)
    kalp.end_fill()

def draw_small_heart(x, y, color="pink", size=0.5):
    mini = turtle.Turtle()
    mini.hideturtle()
    mini.speed(0)
    mini.penup()
    mini.goto(x, y)
    mini.pendown()
    mini.color(color)
    mini.begin_fill()
    mini.left(140)
    mini.forward(10 * size)
    mini.circle(-5 * size, 200)
    mini.left(120)
    mini.circle(-5 * size, 200)
    mini.forward(10 * size)
    mini.end_fill()

def sprinkle_hearts(count=30):
    colors = ["pink", "hotpink", "deeppink", "violet", "lightcoral"]
    for _ in range(count):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        color = random.choice(colors)
        size = random.uniform(0.3, 1.0)
        draw_small_heart(x, y, color, size)
        time.sleep(0.03)

def write_message():
    kalp.penup()
    kalp.goto(0, 0)
    kalp.color("white")
    kalp.write(mesaj, align="center", font=("Courier", 16, "bold"))

# === Çizim başlasın ===
draw_big_heart()
write_message()
sprinkle_hearts()

kalp.hideturtle()
screen.mainloop()



