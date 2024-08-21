def list_of_tupples_with_cube(numbers):
    return [(num,num**3) for num in numbers]

numbers = [1,2,3,4,5]

print(f"List of tupples with number and it's cube {list_of_tupples_with_cube(numbers)}")