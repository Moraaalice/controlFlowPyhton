#Write a function that takes a list of integers as input and prints the sum of all 
# the even numbers in the list
def sum_of_numbers(nums):
    sum = 0
    for n in nums:
        if n%2==0:
            sum+=n
            print(sum)
nums = [12,45,6,9,16,20,43,67]            
sum_of_numbers(nums) 

#Write a function that uses while, if and continue statements to print all the 
# even numbers between 0 and 50. 
def even_numbers():
    x = 0
    while x < 50:
        x+=1
        if x%2!=0:
            continue
        print(x)
even_numbers() 
#Write a function that takes any two integers as input, and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3. 
def any_two_integers(num1,num2):
    sum = 0
    for i in range (num1,num2):
        if i %3==0:
            sum+=i
            print(sum)
any_two_integers()              
                       
#Write a function that takes an integer argument and prints "Prime" if the number is prime,
# and "Not prime" if the number is not prime.
def check_prime(num):
    check = False
    if num == 1:
        print("${num} is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if num%i==0:
                check = True
                
                
    if check:
        print("Is not a prime number")
    else:
        print("Is a prime number")               


    


      
                  
    