def checkGrade(percentage):
    
    
    if(percentage>90 and percentage<100):
        print("A")
    elif(percentage>80 and percentage<90):
        print("B")
    elif(percentage>60 and percentage<80):
        print("C")
    elif(percentage>50 and percentage<60):
        print("D")
    elif(percentage>40 and percentage<50):
        print("E");
    elif(percentage<40):
        print("Failed")

sub1=int(input("Enter the marks of 1st Subject: "))
sub2=int(input("Enter the marks of 2nd Subject: "))
sub3=int(input("Enter the marks of 3rd Subject: "))
sub4=int(input("Enter the marks of 4th Subject: "))
sub5=int(input("Enter the marks of 5th Subject: "))
percentage=((sub1+sub2+sub3+sub4+sub5)/500.0)*100
print(f'Your percentage is {percentage} % ')
checkGrade(percentage)
