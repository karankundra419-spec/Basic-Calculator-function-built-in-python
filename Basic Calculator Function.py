# Calculator Function
def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def average(num1,num2):
    return (num1 + num2)/2

# User Input

print("Enter your opertion: \n" \
    "1 for addition \n" \
    "2 for substraction \n"\
    "3 for multiply \n"\
    "4 for divide \n"\
    "5 for average \n")

select = int(input("Select your operation from 1,2,3,4,5: "))

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

#Condtion

if select == 1:
    print(num1, "+", num2, "=" ,\
           addition(num1,num2))
    
elif select == 2:
    print(num1, "-", num2, "=" ,\
           subtraction(num1,num2))
    
elif select == 3:
    print(num1, "*", num2, "=" ,\
           multiply(num1,num2))

elif select == 4:
    print(num1, "/", num2, "=" ,\
           divide(num1,num2))

elif select == 5:
    print("(",num1, "+", num2,")" ,"/", "2","=" ,\
           average(num1,num2))

else:
    print('Invalid operation!')
