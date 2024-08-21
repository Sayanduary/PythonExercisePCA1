def removeOddIndexes(string):
    return string[::2]

string = input("Enter String: ")

modifiedString=removeOddIndexes(string)
print(f"after removing odd indexes from the string = {modifiedString}")