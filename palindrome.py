list=[1,2,1]
list_copy=list.copy()
list_copy.reverse()
if(list_copy==list):
    print("Palindrome")
else:
    print("Not Palindrome")