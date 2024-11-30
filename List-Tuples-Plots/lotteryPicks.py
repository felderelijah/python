import random

def lotterynumbers(): # Generate a random 6-digit lottery number
  picks = [] #empty list
  for numbers in range(7): # seven digits will be posted
    picks += str(random.randint(0, 9))
    # integers will be converted into a string in order to be posted
  return picks # return values 


print('\tLottery Pick Numbers')
print('-------------------------------------')
print('Below is your random lottery picks.')
print(lotterynumbers())
