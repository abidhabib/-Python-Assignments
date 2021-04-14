def Find__ME(list, numtofind):
    
    for i, num in enumerate(list):
        if num == numtofind:
            return True
    return False

print(Find__ME([4,5,2,7,1,8],71))
