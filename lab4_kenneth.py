# Kenneth nguyen / lab 4 / intro to python
#ticket 1
age = [17, 11, 25, 13, 9]
for x in age:
    if x < 13:
        print(f"{x} - Too young")
    else: 
         print(f"{x} - access granted")
# ages 17, 25, and 13 would be granted access, while ages 11 and 9 would be too young
# it holds the intergers in the list and checks if they are greater or less than 13 

#ticket 2
checking = "yes"

while checking == "yes":
    number = int(input("enter your age: "))
    if number < 13:
        print(f"{number} - Too young")
    else: 
         print(f"{number} - access granted")
    checking = input("would you like to check again?(yes/no): ")
# when the user inputs no it would stop the loop because the conditions for the loop would change.
# the while loop is the right choice because it keeps going until the condition changes when the for loop only loops for a certain number of times

#ticket 3
while True:
    y = input("enter age or type stop: ")
    if y == "stop":
        break
    y = int(y)
    if y >= 13:
        print(f"{y} - access granted")
    else:
         print(f"{y} - too young")
#if you forgot the break command the code wouldnt stop
# the difference between this and ticket 2 is that with this one you choose when it ends

#ticket 4
age = [17, 11, 25, 13, 9]
for x in age:
    if x < 13:
        print(f"{x} - Too young")
    else: 
         print(f"{x} - access granted")

#ticket 5
granted = 0
signups = [22, 10, 15, 8, 19, 13]
amount = len(signups)
for signups, age in enumerate(signups, start=1):
    if age < 13:
      index = (f"{age} - too young")
    else:
        granted = granted + 1 
        index = (f"{age} - access granted")
    print(f"signup #{signups}: {index}")
print(f"approved: {granted} out of {amount}")
# it would say 4 out of 6 approved
# I used for loops, if/else, lists, and variables