def main():
    return()

num_1 = int(input("Insert a number: "))
num_2 = int(input("Insert a number: "))
num_3 = int(input("Insert a number: "))

if (num_1 >= num_2) and (num_1 >= num_3):
   status = num_1
elif (num_2 >= num_1) and (num_2 >= num_3):
   status = num_2
else:
   status = num_3

print("The largest number is", status)
