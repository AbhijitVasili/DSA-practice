num1 =11
num2 = num1

print("Before changing num1")
print('num1 is : ', num1)
print('num2 is : ', num2)
print("\n num 1 points to ", id(num1))
print("\n num 2 points to ", id(num2))

num2 = 22

print('num1 is : ', num1)
print('num2 is : ', num2)
print("\n num 1 points to ", id(num1))
print("\n num 2 points to ", id(num2))

## Numbers are immutable in python. When we change num2 to 22, 
# it creates a new object in memory and num2 points to that new object. 
# num1 still points to the original object which is 11.

dict1 ={
    'value' : 11
}
dict2 = dict1

print("Before changing dict1")
print('dict1 is : ', dict1)     
print('dict2 is : ', dict2)
print("\n dict 1 points to ", id(dict1))
print("\n dict 2 points to ", id(dict2))

dict2['value'] = 22

print("After changing dict1")
print('dict1 is : ', dict1)
print('dict2 is : ', dict2)
print("\n dict 1 points to ", id(dict1))
print("\n dict 2 points to ", id(dict2))

## Dictionaries are mutable in python. 
# When we change dict2, it changes the original object in memory that both dict1 and dict2 point to.
