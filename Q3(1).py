from multiprocessing import log_to_stderr
#
number=str(input("Enter the number : "));
num1=int(number)
list=list(number)
list.reverse()
list=''.join(list)
num=int(list)
print(num)
if (num==num1): 
    print('the number is palindrome')
else:
    print('the number is not palindrome')


