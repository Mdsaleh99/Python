# def colindrome(string):
#     col_length = len(string)
#     col_half = int(col_length/2)

#     if (col_length%2 != 0):
#         print(string, "is not colindrome")
#     else:
#         colName1_Half = string[:col_half]
#         colName2_Half = string[col_half:]
#         col2Half_Rev = colName2_Half[::-1]
#         if( colName1_Half == col2Half_Rev):
#             print(string, "is colindrome")
#         else:
#             print(string, "is not colindrome")

# col_name = input("Enter a string: ")
# colindrome(col_name)




# # palindrome

# pal = input("Enter a string: ")
# if(pal == pal[::-1]):
#     print("palindrome")
# else:
#     print("Not palindrome")



# prime Number

# i = 1

# while(i <= 100):
#     flag = 1
#     for j in range(2, i):
#         if(i%j ==0):
#             flag = 0
#             break
#     if(flag == 1):
#         print(i, "is a Prime Number")

#     i += 1