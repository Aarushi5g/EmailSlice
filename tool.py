email = input("Enter your email ID: ")
split_list = email.split("@")
print(f"Your username is: {split_list[0]}")
print(f"Domain part of the email is: {split_list[1]}")
