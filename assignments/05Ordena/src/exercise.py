def main():
    return()

a = int(input("Insert a number: "))
b = int(input("Insert a number: "))
c = int(input("Insert a number: "))

if a<b and a<c:
    if b<c:
        first, second, third = a,b,c
    else:
        first, second, third = a,c,b
elif b<a and b<c:
    if a<c:
        first, second, third = b,a,c
    else:
        first, second, third = b,c,a
else:
    if a<b:
        first, second, third = c,a,b
    else:
        first, second, third = c,b,a

print("First: ", first)
print("Second: ", second)
print("Third: ", third)
