def countVowels(string):
    vowels = 'aeiouAEIOU'
    count =0
    for char in string:
        if char in vowels:
            count+=1
    return count

string = input("Enter Strings: ")

vowelCount=countVowels(string)
print(f"The number of vowels in the string is {vowelCount}")