
# import calendar
# cal = calendar.month(2025,3)
# print("Here is the calendar:")
# print(f"\033[3m\033[34m{cal}")





#today topic error handling 
#zero division error 
#index error 
#key error  


# num=2
# num2=0

# try:
#     result = [num/num2]
#     print (result)
# except ZeroDivisionError:
#     print("zero division error")
# except IndexError:
#     print("please valid index ")
# except IndentationError:
#     print("please indentation ")

# Local and Gobal varibles 
num_x=5
print("num_x outside function",num_x)

def hello():
    print("num_x inside function",num_x)
    print("how are you?")
hello()
print("num_xinside function",num_x)