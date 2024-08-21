def checkNum(n):
    if(n>1 and n%2==0):
        print("This is Positive and a even Number");
    elif(n<0 and n%2==0):
        print("This is Negetive and a even Number");
    elif(n>1 and n%2!=0):
        print("This is positive and a odd Number");
    elif(n<0 and n%2!=0):
        print("This is Negetive and a odd Number");

checkNum(11)