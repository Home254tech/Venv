from django.test import TestCase

# Create your tests here.


#we had a simple logic game, today lets have an advanced tweeked game in python
import random  
def game():
    try:      
        score= 100
        print("""chose your range below: small range means high chances of winning. input ranges below: 
              (e.g 1 and 5 means selectrandom numbers betwen 1 and 4""")
        
        x= int(input("Enter your first Number to select range: "))
        y= int(input("Enter your second Number to select grange: "))

        number=random.randrange(x,y)
        print(number)
        # class game():

        name= input("Enter your Name to start game: ")

        print(f""" Hello {name}!!!, Welcome to our guess number game. You have 100 total score to 
            begin with each play will cost 10 score if you loose.""")
        
        guess= int(input("Enter any number  here. 'This is a bonus guess': "))
        while number != guess:   
            guess= int(input("Enter your guess here: "))
            if guess < number:
                score=score-10
                print("Low number", score)
                # break
                # the loop will never stop

            if score<=0:
                print("You lose score diminished")
                break
            elif guess> number:
                score=score-10
                print("High number", score)

        else:
            score=score+10
            print(name,"You won!!, Your score is ", score)

    except Exception as e:
        print("Only digits, you inserted ", e)
        game()
# game()
# if request.method=='POST':
#         x=request.POST['f_number']
#         y=request.POST['s_number']
#         name=request.POST['name']
#         guess=request.POST['guess']

#         x= int(input("Enter your first Number to select range: "))
#         y= int(input("Enter your second Number to select grange: "))
#         name= input("Enter your Name to start game: ")
#         guess= int(input("Enter any number  here. 'This is a bonus guess': "))

#         if x ! blank
