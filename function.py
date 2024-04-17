def prints_four():
    print("this is")
    print("an apple")


prints_four()
prints_four()
prints_four()
prints_four()


def name(input):
    print("Your name is " + input)


name("Mauricio")



def name_printer(user_name):
    print(user_name)
 

name = input("Please enter your name.")
name_printer(name)


length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))
 
 
def prism_vol(l, w, h):
    return l * w * h
 
 
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")