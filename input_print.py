name = input("Please Enter your name:")
text_file = open("user_name.txt", "w")
print(name, file=text_file)
text_file.close()