# print even numbers in a list using filter option

a = [1,2,3,4,5,6]
evennumber = list(filter(lambda num : (num%2==0), a))
print('the even numbers is :', evennumber)
 
#using input method and lamda multiply and addition

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = lambda x, y: x + y
multiply = lambda x, y: x * y
addition_result = add(a, b)
multiplication_result = multiply(a, b)

print(f"Addition: {addition_result}")
print(f"Multiplication: {multiplication_result}")

# sorting list using lambda

data = [(1, "apple"),(3, "banana"),(2, "cherry")]
sortdata = sorted(data, key=lambda x:x[0],reverse=True)
print(sortdata)

