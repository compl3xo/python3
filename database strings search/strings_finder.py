import agreement
print("----------------------------------")
print("[---] Database string finder [---]")
print("[---] Author: Compl3x        [---]")
print("----------------------------------")

fopen = open('yourfilehere.txt',mode='r+')
fread = fopen.readlines()
x = input("[X] Make sure you know what the file contains [X]\nEnter IP, email, username, password: ")
for line in fread:
    if x in line:
        print(line)
