def Find__ME(list, numtofind):
    
    for i, item in enumerate(list):
        if item == numtofind:
            return True
    return False

print(Find__ME([4,5,2,7,1,8],71))
