from pico2d import *
import math
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')
grass.draw_now(400,30)
character.draw_now(400,90)
x=0
y=90
theta=360
while(0<theta):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x+400,y+25)
    theta=theta-1
    x=x-2*math.cos(theta/360*2*math.pi)
    y=y-2*math.sin(theta/360*2*math.pi)
    delay(0.01)


    
close_canvas()
