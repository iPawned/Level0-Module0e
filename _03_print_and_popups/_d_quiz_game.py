from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
question1 = simpledialog.askstring(title='Question 1', prompt='What color is the sky?')
if question1 == 'blue':
    messagebox.showinfo(message='Correct!')
    score = score + 1
else:
    messagebox.showinfo(message='Incorrect')
    score = score - 1

question2 = simpledialog.askstring(title='Question 2', prompt='What is the square root of 25?')
if question2 == '5':
    messagebox.showinfo(message='Correct!')
    score = score + 1
else:
    messagebox.showinfo(message='Incorrect')
    score = score - 1

question3 = simpledialog.askstring(title='Question 3', prompt='Write down the first 100 digits of pi (including 3.14)')
if question3 == '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067':
    messagebox.showinfo(message='Correct!')
    score = score + 1
else:
    messagebox.showinfo(message='Incorrect')
    score = score - 1

question4 = simpledialog.askstring(title='Question 4', prompt='If a ball has an initial height of 10 feet, an initial velocity of 10 meters per second, and an angle of launch of 0 degrees (flat), ignoring air resistance, how far (in feet) would the ball travel before hitting the ground?')
if question4 == '25.87 feet':
    messagebox.showinfo(message='Correct!')
    score = score + 1
else:
    messagebox.showinfo(message='Incorrect')
    score = score - 1

question5 = simpledialog.askstring(title='Question 5', prompt='Calculate the transverse speed of sound in magnesium (m/s).')
if question5 == '3060.3':
    messagebox.showinfo(message='Correct!')
    score = score + 1
else:
    messagebox.showinfo(message='Incorrect')
    score = score - 1

question6 = simpledialog.askstring(title='Question 6', prompt='Create a simple equation that unifies general relativity with quantum mechanics.')
messagebox.showinfo(message='Incorrect')

question7 = simpledialog.askstring(title='Question 7', prompt='Find out who asked.')
if question7 == 'I asked':
    messagebox.showinfo(message='Correct!')
    score = score + 1
else:
    messagebox.showinfo(message='Incorrect')
    score = score - 1
    messagebox.showinfo(message='You failed. Better luck next time!')
    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
print(score)
window.mainloop()
