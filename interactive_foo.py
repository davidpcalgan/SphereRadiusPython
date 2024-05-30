import sphere_volume

esc_character = "end"
text = ""

while(text != esc_character):
    text = input("Enter the radius of your sphere, or type \"" + esc_character + "\": ")
    if (text != esc_character):
        try:
            text_value = float(text)
        except ValueError as e:
            print ("    The radius must be a number")
        else:
            if(text_value >= 0):
                print("    A sphere of radius " + text + " has volume " + str(sphere_volume.foo(text_value)))
            else:
                print("    A sphere's radius must be positive")
