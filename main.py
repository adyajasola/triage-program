
import turtle
import random

global delay
global k

k = 0
name = []
age = []
disease = ""
Doctor = ""
global time 
time = 0
global isNotSelected
sorted_list = []
time = 0


def calldocA():
  global time 
  global isNotSelected
  time =0
  turtle.ontimer(final,t= time*1000)
  isNotSelected = False
  
  s.clear()

def calldocB():
  global time 
  global isNotSelected
  time =30
  turtle.ontimer(final,t= time*1000)
  isNotSelected = False
  
  s.clear()

def calldocC():
  global time 
  global isNotSelected
  time =60
  turtle.ontimer(final,t= time*1000)
  isNotSelected = False
  
  s.clear()

def calldocD():
  global time 
  global isNotSelected
  time =90
  turtle.ontimer(final,t= time*1000)
  isNotSelected = False
  
  s.clear()

def calldocE():
  global time 
  global isNotSelected
  time =150
  turtle.ontimer(final,t= time*1000)
  isNotSelected = False

  s.clear()

def calldocF():
  global time 
  global isNotSelected
  time =120
  isNotSelected = False
  turtle.ontimer(final,t= time*1000)
  s.clear()

def final():
  
  s.clearscreen()
  s.bgcolor("white")
  
  doctorA = turtle.Turtle()
  turtle.addshape("DA.gif")
  doctorA.shape('DA.gif')
  doctorA.penup()
  doctorA.goto(-190, -180)


  dialogue1 =turtle.Turtle()
  dialogue1.shape("dialogue.gif")
  dialogue1.penup()
  dialogue1.goto(50,150)
  dialogue1.showturtle()
  
  text1 = turtle.Turtle()
  text1.hideturtle()
  text1.penup()
  text1.goto(50,170)
  if k>0:
    text1.write(input_name+"! "+str(k) +" is an impressive Score.", False, align ="center", font = ("Calibri" , 11, "bold"))
  text1.goto(50,150)
  text1.write("I am Dr. Smith, and I am your doctor today.", False, align ="center", font = ("Calibri" , 11, "bold"))
  text1.goto(50,130)
  text1.write("Thank You for waiting so paitently.", False, align ="center", font = ("Calibri" , 11, "bold"))

              
            
  




######## SCREEN 1 ###########

s = turtle.getscreen()  #set up the screen
s.bgcolor("skyblue")
s.title("THE EMERGENCY TRIAGE")

s.listen()

text = turtle.Turtle()
text.hideturtle()
text.penup()

text.goto(0, 150)
text.color('red')
text.write("WELCOME TO THE EMERGENCY TRIAGE", False,
           align='center',
           font=('Calibri', 18, 'bold'))

text.goto(0, -150)
text.color('black')
text.write("Click to Enter the ER",
           False,
           align='center',
           font=('Calibri', 14, 'bold'))

hospital = turtle.Turtle()
turtle.addshape("hospital.gif")
hospital.shape("hospital.gif")
hospital.penup()
hospital.goto(0, 0)


def delayfunct(x, y):
  global delay
  delay = False


delay = True
while delay:
  hospital.onclick(delayfunct)

###### SCREEN 2########
s.clearscreen()
s.bgpic("bg.gif")


nurse = turtle.Turtle()
turtle.addshape("nurse.gif")
nurse.shape("nurse.gif")
nurse.penup()
nurse.goto(-190, -180)

dialogue = turtle.Turtle()
turtle.addshape("dialogue.gif")
dialogue.shape('dialogue.gif')
dialogue.penup()
dialogue.goto(120, 90)

text2 = turtle.Turtle()
text2.penup()
text2.hideturtle()
text2.goto(120, 130)
text2.color("black")
text2.write("Hello! This is the emergeny triage.",
            False,
            align="center",
            font=("Calibri", 11, "bold"))
text2.goto(120, 110)
text2.write("I am nurse IVY.", False,
            align="center",
            font=("Calibri", 11, "bold"))
text2.goto(120, 90)
text2.write("Please enter your name in the terminal.",
            False,
            align="center",
            font=("Calibri", 11, "bold"))
text2.goto(120, 70)
text2.write("The Doctor will see you soon!",
            False,
            align="center",
            font=("Calibri", 11, "bold"))



input_name = input("Enter your name: ")
input_name = input_name + " "
name.append(input_name)
text2.clear()

dialogue.hideturtle()
nurse.speed(1)
nurse.goto(-300,-300)
dialogue.goto(-30,-20)
dialogue.showturtle()

text2.goto(-50,15)
text2.write(input_name[:input_name.index(" ")], False,
          align="center",
          font=("Calibri", 11, "bold"))
text2.goto(-50,0)
text2.write("Which category symptoms do you have?",False,
          align="center",
          font=("Calibri", 11, "bold"))
text2.goto(-40,-15)
text2.write("Based on the category you will be alloted time.",False,
          align="center",
          font=("Calibri", 10, "bold"))
text2.goto(-50,-30)
text2.write("In This waiting period you will play -",False,
          align="center",
          font=("Calibri", 11, "bold"))
text2.goto(-45,-45)
text2.write("'Kill The Germ'",False,
          align="center",
          font=("Calibri", 11, "bold"))
for i in range(10550000):
  i+=1
nurse.hideturtle()
dialogue.hideturtle()
text2.clear()


############ SCREEN 3#######################




s.bgcolor("#994444")
s.bgpic("nopic")
text2.color("white")
text2.goto(0,210)
text2.write("Answer In the Terminal",False,
          align="center",
          font=("Calibri", 18, "bold"))

cat1 =  turtle.Turtle()
turtle.addshape("cat1.gif")
cat1.shape('cat1.gif')
cat1.penup()
cat1.goto(-200, 100)

cat2 = turtle.Turtle()
turtle.addshape("cat2.gif")
cat2.shape('cat2.gif')
cat2.penup()
cat2.goto(0, 100)

cat3 = turtle.Turtle()
turtle.addshape("cat3.gif")
cat3.shape('cat3.gif')
cat3.penup()
cat3.goto(200, 100)

cat4= turtle.Turtle()
turtle.addshape("cat4.gif")
cat4.shape('cat4.gif')
cat4.penup()
cat4.goto(-200, -120)

cat5= turtle.Turtle()
turtle.addshape("cat5.gif")
cat5.shape('cat5.gif')
cat5.penup()
cat5.goto(0, -120)

cat6= turtle.Turtle()
turtle.addshape("cat6.gif")
cat6.shape('cat6.gif')
cat6.penup()
cat6.goto(200, -120)

isNotSelected = True
while isNotSelected:
  
  category = input("Enter the category: ")
  category = category[-1]
  if category =="1":
    calldocA()
  elif category =="2":
    calldocB()
  elif category =="3":
    calldocC()
  elif category =="4":
    calldocD()
  elif category =="5":
    calldocE()
  elif category == "6":
    calldocF()
  else:
    print("Invalid Response. Choose from 1-6")





####################### TRIAGE GAME ######################

#def game():
def up():
  doctor.setheading(90)
  doctor.forward(10)
  

def down():
  doctor.setheading(270)
  doctor.forward(10)
  
def throw():
  pos = str(doctor.position())
  x = float(pos[1:pos.index(",")])
  y = float(pos[pos.index(",")+1:-1])
  lazer.goto(x+270,y-10)
  lazer.showturtle()
  check()

def check():
  global k
  if (germ.xcor()- 30 <100 ):
    if (abs(max(germ.ycor(),lazer.ycor()))- abs(min(germ.ycor(),lazer.ycor())) <30):
      text.clear()
      germ.hideturtle()
      germ.goto(random.randint(0,100),random.randint(-200,200))
      germ.showturtle()
      k=k+1
      text.write("Score: "+str(k), False, align='center', font=('Calibri', 18, 'bold'))

  
def hidt():
  lazer.hideturtle()
  
if int(category) >1:
  s = turtle.Screen()
  
  turtle.bgcolor("black")
  doctor = turtle.Turtle()
  turtle.addshape("doctorgame.gif")
  doctor.shape("doctorgame.gif")
  doctor.penup()
  doctor.hideturtle()
  lazer = turtle.Turtle()
  turtle.addshape("lazer.gif")
  lazer.shape("lazer.gif") 
  lazer.hideturtle()
  germ = turtle.Turtle()
  turtle.addshape("germ.gif")
  germ.shape("germ.gif")
  germ.penup()
  germ.hideturtle()
  
  doctor.showturtle()
  doctor.goto(-300,0)
  
  
  
  
  germ.goto(random.randint(0,100),random.randint(-200,200))
  germ.showturtle()
  
  
  
  s.listen()
  s.onkey(up,"Up")
  s.onkey(down,"Down")
  s.onkeypress(throw,"Return")
  s.onkeyrelease(hidt,"Return")
  
  
  
  text = turtle.Turtle()
  text.hideturtle()
  text.penup()
  text.color("red")
  text.goto(250,250)






#game()

turtle.mainloop()
  
