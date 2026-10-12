

def Add(a,b):
    c=a+b
    print(c)

Add(5,4)

print("Hello World!")

age=int(input("Enter Your Age: "))

if (age>18):
    print("Driveee")
else:
    print("Cannot Drive!")

numbers = [2,4,5,6,7]
numbers.append(8) 
numbers.remove(5)
numbers.insert(2,3)
numbers.pop(3)
numbers.sort()
numbers.clear()


for i in numbers:
    print(i)



print(numbers)


tuples
numbers=(4,5,6,7,6,7,8)
print(numbers)
print(numbers[0])

numbers = (5, 8, 5, 10, 7)
print(len(numbers))
print(numbers.count(5))
print(numbers.index(10))
print(numbers + (20, 30))
print(8 in numbers)
print(min(numbers), max(numbers))


for i in range(10):
    print(i)

lists=["Shubh","Ishanhvi","Chhavi","Agrima","Shriya","Nandini"]

for i in lists:
    print(i)


for ch in "Shubh":
    print(ch)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)


def even_check(num):
    if(num%2==0):
        return "Even"

S=even_check(4)
print(S)

add=lambda a,b:a+b
print(add(4,5))

square= lambda x:x*x
print(square(5))

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))


numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))

numbers = [5, 10, 15, 20]
result = map(lambda x: x + 5, numbers)
print(list(result))

