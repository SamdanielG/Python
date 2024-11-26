try:
    num=int(input("Enter a number:"))
    result=100 / num
    print("Result:",result)
except ZeroDivisionError:
    print("Invalid input place enter a valid number.")
else:    
    print("No exception occurred.")
finally:
    print("This block always runs.")    