import time
import  replit  

#addition
def add(x, y):
  return x + y

#subtraction
def subtract(x, y):
  return x - y

#multiplication
def multiply(x, y):
  return x * y

#dividation
def divide(x, y):
  return x / y

while True:
  #print operations
  print("Select! (+) (-) (*) (/)")

  #input
  operation = input("input: ")

  #Check if operation is one of the four operations
  if operation in ('+', '-', '*', '/'):
    num1 = float(input("1st number: "))
    num2 = float(input("2nd number: "))

    if operation == '+':
      print(num1, "+", num2, "=", add(num1, num2))

    if operation == '-':
      print(num1, "-", num2, "=", subtract(num1, num2))

    if operation == '*':
      print(num1, "*", num2, "=", multiply(num1, num2))

    if operation == '/':
      print(num1, "/", num2, "=", divide(num1, num2))
  else:
    print("Input Error")

  #clear screen after 3s to keep things neat n clean
  time.sleep(2)
  print("....")
  time.sleep(2)
  print("Cleaning Things up")
  time.sleep(2)
  replit.clear() #depends on the application you're using
