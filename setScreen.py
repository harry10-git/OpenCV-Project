import turtle as t
class display():
    def __init__(self,screen):
        self.screen=screen
        w=self.screen.window_width()
        h=self.screen.window_height()
        self.allRacks=[]

    def DrawLines(self):
        w=self.screen.window_width()
        h=self.screen.window_height()
        self=t.Turtle()
        self.pensize(0.8)
        self.hideturtle()
        self.pencolor('white')
        coordList=[[-(w//2),h//2-30,0,w],[-(w//2),-(h//2-30),0,w],[-(w//2-30),h//2,270,h],[(w//2-30),(h//2),270,h]]
        for coord in coordList:
            self.penup()
            self.goto(coord[0],coord[1])
            self.setheading(coord[2])
            for _ in range(coord[3]//40):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)

    def makeRacks(self):
        w=self.screen.window_width()
        h=self.screen.window_height()
        #x y stretch color heading
        positions=[[-(w//2-80),h//2-120,8,'yellow',90],[-(w//2-100),h//2-120,8,'yellow',90],[-(w//2-350),-(h//2-180),20,'white',0],[(0),h//2-270,5,'pink',90],[(w//2-250),(h//2-80),22,'light blue',0],[(w//2-250),(h//2-100),22,'light blue',0]]
        for pos in positions:
            r=t.Turtle('square')
            r.penup()
            r.goto(pos[0],pos[1])
            r.setheading(pos[4])
            r.shapesize(stretch_len=pos[2])
            r.color(pos[3])
            self.allRacks.append(r)