def isSubstringPresent(main_string, sub_string):
    return sub_string in main_string


main_string = "Hey I am Sayan Duary"
sub_string = "Sayan"

if isSubstringPresent(main_string, sub_string):
    print(f"The Substring ' {sub_string}' is present in the Main String")
else:
    print(f"The Substring '{sub_string}' is not present in the Main String")
