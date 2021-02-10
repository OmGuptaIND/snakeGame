from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
EDGE = 290
sp = 0.1
while game_on:
    screen.update()
    time.sleep(sp)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > EDGE or snake.head.xcor() < -EDGE or snake.head.ycor() > EDGE or snake.head.ycor() < -EDGE:
        game_on = False
        score.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
