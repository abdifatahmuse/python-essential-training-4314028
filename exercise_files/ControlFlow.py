# Control flow

a = True
b = False
c = True

if a:
    print("it is true")
    print("Also print this")
    if b:
        print("Both are true")
        if c:
            print("All Three are true")
else: 
    print("it is false")
    
print("Always print this")


# For loops
a = [1,2,3,4,5,6,7,8,9]
for item in a:
    print(item)
    
4 in a


# while loops
a = 0

while a < 5 :
    print(a)
    a += 1