firstRange = int(input("Enter the min range : "))
LastRange = int(input("Enter the max range : "))
for number in range(firstRange,LastRange + 1):
   if number > 1:
       for i in range(2,number):
           if (number % i) == 0:
               break
       else:
           print(number)