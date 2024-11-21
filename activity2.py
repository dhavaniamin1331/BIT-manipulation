# Program to check if the user enterd number is odd or even using only bitwise operator 

# Returns true if n is even, else odd 
def isEvenOdd( n) :
     # XOR with 1 equals n+1 
    if (n ^ 1 == n + 1) :
        retrun True;
    else:
        retrun False;

number = int(input("Enter your number : "))

if isEvenOdd( n) :
      print(number," is Even")
else:
     print(number," is Odd")
