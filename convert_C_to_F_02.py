# FILE NAME - convert_C_to_F_02.py
# NAME: Connor Beer
# DATE: March 1, 2026
# BRIEF DESCRIPTION:  Converts temperatures between Fahrenheit and Celsius

########## ENTER YER CODE BELOW THIS LINE ##########

def main():
  temperature_converter()

def temperature_converter():
  print('===== Temperature Converter =====')
  print()
  print('  1. Convert from Celsius to Fahrenheit')
  print('  2. Convert from Fahrenheit to Celsius')
  print()
  choice = float(input('Please choose from the above menu: '))

  if choice == 1:
    Celsius = float(input('Enter a temperature to convert: '))
    converted = Celsius * 9/5 + 32
    print()
    print(f'{Celsius} degrees Celsius is {converted} degrees Fahrenheit.')
  else:
    Fahrenheit = float(input('Enter a temperature to convert: '))
    converted = (Fahrenheit - 32 ) * 5/9
    print()
    print(f'{Fahrenheit} degrees Fahrenheit is {converted} degrees Celsius.')

main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          REFLECTION QUESTIONS
########################################

'''
1. What is one lesson you learned in this lab?
how to take an older piece of code and turn it itno something new
'''