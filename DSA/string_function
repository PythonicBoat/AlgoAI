string = input("Enter the string on which you want to perform operations : ")
print("-------------------------------------------------------------------------------")
print("Below are some actions that the program can perform on the string ->")
print("1. Calculate the length of the string")
print("2. Calculate the number of times a particular character appears")
print("3. Print the string in lowercase letters")
print("4. Print the string in uppercase letters")
print("5. Reverse the string")
print("6. Check if string is palindrome")
print("7. Check if a particular letter or word is present or not")
print("8. Find the index value of a particular letter or word")
print("9. Replace a word or letter with a word or letter")
print("-------------------------------------------------------------------------------")
while True:
    option = input("Enter the S. No. of the action that you want to be performed(write 'EXIT' to end program) : ")
    print("-------------------------------------------------------------------------------")
    if option == "1":
        print("The length of the string is", len(string))

    if option == "2":
        char_freq = input("Enter the character : ")
        count_1 = 0
        for char in string:
            if char == char_freq:
                count_1 = count_1 + 1
        print(char_freq + " appeared", count_1, "times.")

    if option == "3":
        print(string.lower())

    if option == "4":
        print(string.upper())

    if option == "5":
        string_length1 = len(string)
        reversed_string = string[string_length1 - 1::-1]
        print(reversed_string)

    if option == "6":
        string_length = len(string)
        reversed_string1 = string[string_length - 1::-1]
        if string == reversed_string1:
            print(string + " is a palindrome.")
        else:
            print(string + " is not a palindrome.")

    if option == "7":
        check = input("Enter the letter or word to be checked : ")
        a = str(check in string)
        if a == "True":
            print(check + " is present in the string.")
        else:
            print(check + " is not present in the string.")

    if option == "8":
        value = input("Enter the letter or word whose index value is to be found : ")
        print("The index value of " + value + " is", string.find(value))

    if option == "9":
        to_be_replaced = input("Enter the word or letter to be replaced : ")
        replaced = input("Enter the word or letter you want to replace it with : ")
        new_string = string.replace(to_be_replaced, replaced)
        print(new_string)

    if option == "EXIT":
        break
