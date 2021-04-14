def Find__ME(list, numToFind):
    
    for i, item in enumerate(list):
        if item == numToFind:
            return True
    return False
xx=int(input("Enter"))
print(Find__ME([4,5,2,71,1,8],xx))
