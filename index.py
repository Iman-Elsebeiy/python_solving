import random
random_number = random.randint(1000, 9999)
#inter 4 digits
user_number =input("Enter a 4-digit pin: ");
# if len(user_number) != 4 or not user_number.isdigit():
#     print("Invalid input. Please enter exactly 4 digits.")

# elif int(user_number) == random_number:
#         print("Access Granted")
# else:
#         print("Access Denied, the correct pin is:", random_number)
while len(user_number) != 4 or not user_number.isdigit():
         print("Invalid input. Please enter exactly 4 digits.")
         user_number =input("Enter a 4-digit pin: ")

if int(user_number) == random_number:
           print("Access Granted")
else:
          print("Access Denied, the correct pin is:", random_number)       
    

