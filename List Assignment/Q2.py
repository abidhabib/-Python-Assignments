my_list2= [23,44,55,21,43,42,98,99]
while True:
    x=int(input("Press 1 For Sorted List\nPress 2 For Reverse List\n'0' For Quit Program\n"))
    if x==1:
        my_list2.sort()
        print(my_list2)
    elif x==2:
        my_list2.reverse()
        print(my_list2)
    elif x==0:
        quit()
