import os
text_file= open("Greetings2.txt", "w")
#print("fuck you", file= files)
#files.close()
print("Good morning my people", "Good afternoon my people", "Good night my people", sep=os.linesep, file=text_file)
text_file.close()