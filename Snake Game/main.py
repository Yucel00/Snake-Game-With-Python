import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
score=Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()


    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<15:
            game_is_on=False
            score.game_over()












screen.exitonclick()
