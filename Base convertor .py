'''a = int(input("Enter binary number:"))
def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
  

if __name__ == '__main__': 
    dec_val = a
    DecimalToBinary(dec_val)
    '''
'''def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
number = int(input("Enter any decimal number: "))

decimalToBinary(number)'''
x= 123
s=" "
while True:
    if x>0:
        s = s+str(x%2)
        x=x//2
    else:
        break
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
print(reverse(s))
