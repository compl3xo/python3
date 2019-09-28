from colorama import init, Fore, Back, Style
print(Style.BRIGHT + Fore.RED + "{ In order to use this script,\nyou need to add the name of\nyour database file in the code.}")

choice = input(Style.BRIGHT + Fore.GREEN + "Do you understand [y/n]: ")
if choice == 'y':
    pass    
    
elif choice == 'n':
    print(Style.BRIGHT + Fore.RED + "[X] To use this, you HAVE to change the name inside the source code. [X]")
    exit()
else:
    print("Please enter yes or no.")
