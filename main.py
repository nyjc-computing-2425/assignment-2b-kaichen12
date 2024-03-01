num = input('Enter a number (decimal only): ')
# type your code here
num1 = num.strip(' ')
num2 = num1.lstrip('0')
decimalpos = num2.find('.')
dp = len(num2[decimalpos+1:])



# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
