my_list=[3,4,5,10,7]
x=int(input(("Press 1 for Addition of listItems\nPress 2 for Multiplication of list Items\nPress 0 to exit program\n")))
if x==1:
    Sum=sum(my_list)
    print(Sum)
elif x == 2:
    mul=1
    for i in my_list:
        mul*=i
    print(mul)
else:
    quit()