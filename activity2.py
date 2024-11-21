# Program to check if the user enterd number is odd or even using only bitwise operator 

# Returns true if n is even, else odd 
def isEvenOdd( number) :
     # XOR with 1 equals n+1 
    if (number ^ 1 == number + 1) :
        return True;
    else:
        return False;

number = int(input("Enter your number : "))

if isEvenOdd( number) :
      print(number," is Even")
else:
     print(number," is Odd")
