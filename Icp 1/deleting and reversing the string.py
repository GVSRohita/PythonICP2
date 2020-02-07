#To get the input for the user
val = input("Enter a word : ");
#To print the user input for reference
print("You have just entered:", val);
#Deleting the last two charachters from the given word
#val = val[:-2] for removing last charachtesrs
val = val[2:]
#Reversing the word
val = val[::-1];
#To print the user required output
print("\n Reversed String =", val);