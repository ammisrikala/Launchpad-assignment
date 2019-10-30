from datetime import datetime
name = input('enter name \n')
age = int(input('enter age \n'))
answer= int((100-age) + datetime.now().year)
print ('Hey %s !.  You will turn 100 years old in %s.' % (name, answer))