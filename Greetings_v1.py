lines = """
Good Morning My people
Good Afternoon My People
Good Night My People
"""
text_file = open("Greetings.txt", "w")
print(lines, file = text_file)
text_file.close