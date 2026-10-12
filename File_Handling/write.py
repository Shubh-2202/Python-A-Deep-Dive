with open("Practice.txt", "w" ,encoding="utf-8") as file:
    file.write("Hello File\n")
    file.write("This is my first File Writig\n")
    file.write("This world is a Maya and God is the eternal Truth!\n")

# Writes Text Afterwards using Append as "a"

with open("practice.txt", "a", encoding="utf-8") as file:
    file.write("This line was added later.\n")