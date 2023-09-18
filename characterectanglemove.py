from pico2d import *
import math

open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')
grass.draw_now(400,30)
character.draw_now(400,90)
x=0
y=90
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+2
    delay(0.01)
while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y+2
    delay(0.01)
while(0 < x):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,600)
    x=x-2
    delay(0.01)
while(90<y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y-2
    delay(0.01)


# fill here

close_canvas()
