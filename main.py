import turtle as t
import robot
import setScreen
import imageGeneration


def moveRobot(dir,mag):
    if dir=='Left':
        rob.MoveLeft(mag)
        return
    if dir=='Right':
        rob.MoveRight(mag)
        return
    if dir=='Up':
        rob.MoveForward(mag)
        return
    if dir=='Down':
        rob.MoveBack(mag)
        return



screen=t.Screen()
screen.title('warehouse')
screen.setup(width=900,height=600)
screen.bgcolor('black')
h=screen.window_height()
w=screen.window_width()
screen.tracer(0)
display=setScreen.display(screen)
display.DrawLines()
display.makeRacks()
rob=robot.CreateRobot(screen)
screen.tracer(1)

obj=imageGeneration.temp()
turtle_msg=obj.getInstruction()
for instruction in turtle_msg:
    moveRobot(instruction[0],instruction[1]*10)
screen.exitonclick()