####find the greatest number from 4 numbers 


# a=34
# b=89
# c=9
# d=2
# if a>b:
#     if a>c:
#         if a>d:
#             print (a)
# else:
#     if b>c:
#         if b>d:
#             print(b)
#     else :
#         if c>d:
#             print(c)
#         else:
#             print(d)
        

# m=int(input("enter the no starting from to add "))

# n=int(input("enter the no till sum"))
# add=0
# while m<=n:
#     add+=m
#     m+=1
# print(add)


# ####calcutor 
# a=int(input("enter the first number"))
# opr=input("enter the operator")
# b=int(input("enter the second number"))

# if opr=="+":
#     print(a+b)
# elif opr=="-":
#     print(a-b)
# elif opr=="*":
#     print(a*b)
# elif opr=="/":
#     print(a/b)
# elif opr=="//":
#     print(a//b)
# elif opr=="**":
#     print(a**b)
# else :
#     print("no operator is found ERROR")



##### import time

# clock=str(time.strftime("%H:%M:%S"))

# if ((clock>="24:00:00")and (clock<="12:00:00")):
#     print("Good Morining User")
# elif((clock>="12:00:00")and (clock<="17:00:00")):
#     print("good Afternoon user ")
# else:
#     print("good night")


# Print the multiplication table of 7 using range().

# for i in range(7,71,7):
#     print(i,end=" ")


# Print the squares of numbers from 1 to 10 using range().

# for i in range (1,11):
#     print(i**2,end=" ")


# Print all numbers between 50 and 100 that are divisible by 5 using range().
 
# for i in range(50,101,5):
#     if(i%5==0):
#         print(i,end=" ")


# Generate numbers from 100 to 1 in steps of 10 using range().

# for i in range (100,0,-10):
#     print (i)

    
# total = 0   # variable to store sum

# for i in range(1, 21):   # numbers 1 to 20
#     total = total + i    # add i to total (or total += i)

# print("Sum of first 20 natural numbers =", total)



# Print a list of all prime numbers between 1 and 50 using range()


# for i in range(2, 51):   # numbers from 2 to 50
#     for j in range(2, i):   # check numbers smaller than i
#         if i % j == 0:   # if divisible, not prime
#             break
#     else:   # this else belongs to the for-loop, not if
#         print(i)




# Use range() to print a pattern like this:

# row=5
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

row=6
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(i ,end=" ")
    print()







