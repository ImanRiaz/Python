print("Welcome to Mini Calculator!")
first=float(input("Enter your first number: "))
operator=input("Which operation do you want to perform? (+,-,*,/,%): ")
second=float(input("Enter your second number: "))

result=None

if operator == "+":
    result=first+second
elif operator == "-":
    result=first-second
elif operator == "*":
    result=first*second
elif operator == "/":
    if second!=0:
      result=first/second
    else:
      print("Division by 0 is not allowed.")
elif operator == "%":
     if second!=0:
      result=first%second
     else:
      print("Division by 0 is not allowed.")
else:
    print("Invalid operation.")
#float(result)
print(result)