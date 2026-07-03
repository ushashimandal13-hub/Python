#palindrome list
list1= [1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if list1 == copy_list1:
    print("The list is palindrome")
else:
    print("The list is not palindrome")