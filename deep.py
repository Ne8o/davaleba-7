#the Great Question of Life

'''
answer = str(input("the Great Question of Life :"))
if answer == "42":
    print("yes")
elif answer == "Forty Two":
    print("yes")
elif answer == "Forty-Two":
    print("yes")
else :
    print("no")
'''
#best way
answer = str(input("the Great Question of Life :"))
if answer == "42" or "Forty Two" or "Forty-Two":
    print("Yes")
else :
    print("No")