import random

def lotterynumbers(): # Generate a random 6-digit lottery number
  picks = [] #empty list
  for numbers in range(6): # seven digits will be posted
    picks.append(random.randint(0, 9))
  for cycle in picks:
    print(str(cycle), end="")
  return cycle # return values 

print('\tLottery Pick Numbers')
print('-------------------------------------')
print('Below is your random lottery picks.')
print(lotterynumbers())
