import sys

type = sys.argv[1]

if type == "t2.micro":
    print("its free of cost")
elif type == "t2.medium":
    print("it will charge you 4 dollars a day")
elif type == "t2.xlarge":
    print("it will charge you 6 dollars a day")

else:
    print("please provide a valid input")




