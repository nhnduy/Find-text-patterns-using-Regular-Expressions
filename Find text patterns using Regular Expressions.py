import re

with open("Twelve Days of Chrismas example.txt", "r") as file:
    file_reader = file.read()
    
    #r for raw string
    #\d for digits + for one or more digits
    #\s for space
    #\w for "word" character + for one or more "word" characters
    xmasRegex = re.compile(r"\d+\s\w+")
    
    all_objects = xmasRegex.findall(file_reader)

print(all_objects)