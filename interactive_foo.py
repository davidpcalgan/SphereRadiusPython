import sphere_volume

#The string that must be entered to exit the loop
ESC_STRING = "end"

#Blank variable to be filled by user input
text = ""

while(text != ESC_STRING): #loop for multiple calculations, loops until user inputs escape string

    #User input
    text = input("Enter the radius of your sphere, or type \"" + ESC_STRING + "\": ")
    
    if (text != ESC_STRING): #Check for escape string
        try:
            text_value = float(text)
        except ValueError as e: #Check for non-number
            print ("    The radius must be a number")
        else:
            if(text_value < 0): #Check for negative number
                print("    A sphere's radius must be positive")
            else:               #Must be a positive number, calculate foo
                print("    A sphere of radius " + text + " has volume " + str(sphere_volume.foo(text_value)))
