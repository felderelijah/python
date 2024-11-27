# user input
charge = float(input('Enter the charge for the food: '))
print(f'Subtotal: ${charge}')

# tip and tax
GRATUITY = 18/100
SALES_TAX = 17/100

tip = charge * GRATUITY
state = charge * SALES_TAX
final = charge + tip + state

print(f'\nGratuity: ${tip:.2f}\nTax: ${state:.2f}')
print(f'\nTotal: ${final:.2f}')
