def main():
    print("Welcome to the Program")
    theName = getName()
    print(f"Hello World my name is {theName}")
    theAge = getAge()
    print(f"Hello World my name is {theName}and I am {theAge} years old")

def GetName():
    nameInput = input ("What is your name? ")
    return(nameInput)

def GetAge():
    ageInput = input ("How old are you")
    return(ageInput)
