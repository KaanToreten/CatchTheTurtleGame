import turtle
import random

# Ekranı ayarla
wn = turtle.Screen()
wn.title("Catch the Turtle")
wn.bgcolor("lightblue")

# Kaplumbağa oluştur
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.shapesize(2, 2)
player.penup()
player.speed(0)

# Skor ve sayaç
score = 0
timer = 0
difficulty = ""
FONT = ("Arial", 30, "normal")

# Skor yazıcısı
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("blue")
score_writer.penup()
top_height = wn.window_height() / 2
y = top_height - top_height / 10
score_writer.setposition(0, y)
score_writer.write(arg='Score: 0', move=False, align='center', font=FONT)

# Sayaç yazıcısı
timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.setposition(0, y - 30)

# Zorluk seviyesi yazıcısı
difficulty_writer = turtle.Turtle()
difficulty_writer.hideturtle()
difficulty_writer.penup()
difficulty_writer.goto(0, 0)
difficulty_writer.write("Choose the level: Easy(e), Medium (m), Hard (h)", move=False, align='center', font=FONT)

# Skoru artırma işlevi
def increase_score(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Score: {score}", move=False, align='center', font=FONT)
    move_turtle()

# Kaplumbağayı hareket ettir
def move_turtle():
    new_x = random.randint(-200, 200)
    new_y = random.randint(-200, 200)
    player.goto(new_x, new_y)

# Zamanlayıcı işlevi
def countdown():
    global timer
    timer -= 1
    timer_writer.clear()
    timer_writer.write(f"Zaman: {timer}", move=False, align='center', font=FONT)
    if timer > 0:
        wn.ontimer(countdown, 1000)
    else:
        player.hideturtle()
        score_writer.goto(0, 0)
        score_writer.write("Game over!", move=False, align='center', font=FONT)

# Kaplumbağaya tıklama olayı
player.onclick(increase_score)

# Zorluk seviyesini ayarlama
def set_difficulty(diff):
    global timer, difficulty
    difficulty = diff
    if difficulty == "Easy":
        timer = 30
        player.speed(3)
    elif difficulty == "Medium":
        timer = 20
        player.speed(5)
    elif difficulty == "Hard":
        timer = 10
        player.speed(8)
    difficulty_writer.clear()
    timer_writer.write(f"Time: {timer}", move=False, align='center', font=FONT)
    move_turtle()
    wn.ontimer(countdown, 1000)

# Zorluk seviyesini seçme
def set_easy():
    set_difficulty("Easy")

def set_medium():
    set_difficulty("Medium")

def set_hard():
    set_difficulty("Hard")

# Zorluk seviyesini seçme tuşları
wn.onkey(set_easy, "e")
wn.onkey(set_medium, "m")
wn.onkey(set_hard, "h")

# Tuş dinleyicisini başlat
wn.listen()
wn.mainloop()
