from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
game_speed = 0.15
last_speedup_score = 0

while game_is_on:
    screen.update()
    if score.score >= last_speedup_score + 5:
        game_speed -= 0.02
        last_speedup_score = score.score
    time.sleep(game_speed)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        score.update_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()

screen.exitonclick()