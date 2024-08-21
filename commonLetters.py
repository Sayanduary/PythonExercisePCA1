def commonLetters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)

    commonSet = set1.intersection(set2)

    return commonSet


string1 = "Hello"
string2 = "World"

print(f"Common Letters are {commonLetters(string1,string2)}")
