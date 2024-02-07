import turtle as t
class CreateRobot(t.Turtle):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.hideturtle()
        w=self.screen.window_width()
        h=self.screen.window_height()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,-(h//2)+50)
        self.setheading(90)
        self.showturtle()
        self.speed(speed='slowest')

    def MoveForward(self,m):
        h=self.screen.window_height()
        w=self.screen.window_width()
        if self.ycor()>=h//2-50 and self.heading()==90: #facing top wall
            return
        if self.ycor()<=-(h//2-50) and self.heading()==270: #facing bottom wall
            return
        if self.xcor()<=-(w//2-50) and self.heading()==180: #facing left wall
            return
        if self.xcor()>=(w//2-50) and self.heading()==0: #facing right wall
            return
        self.forward(m)

    def MoveRight(self,mag):
        self.right(90)
        self.MoveForward(mag)

    def MoveLeft(self,mag):
        self.left(90)
        self.MoveForward(mag)
    
    def MoveBack(self,m):
        h=self.screen.window_height()
        w=self.screen.window_width()
        if self.ycor()>=h//2-50 and self.heading()==270: #facing top wall
            return
        if self.ycor()<=-(h//2-50) and self.heading()==90: #facing bottom wall
            return
        if self.xcor()<=-(w//2-50) and self.heading()==0: #facing left wall
            return
        if self.xcor()>=(w//2-50) and self.heading()==180: #facing right wall
            return
        self.back(m)

    def Reset_position(self):
        h=self.screen.window_height()
        self.goto(0,-(h//2)+50)

