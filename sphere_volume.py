#Volume of a sphere calculator
#V = (4 / 3 * pi) * r^3 ~= (4.188790) * r^3
def foo(radius):
    if(radius >= 0): #foo is valid for non-negative values only
        return radius * radius * radius * 4.188790
    else:
        raise ValueError ("Radius must be a non-negative number.")
