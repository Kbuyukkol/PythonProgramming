from day03.abstraction_2 import Shape, Square, Rectangle


shape1: Shape = Square(5)

shape2: Shape = Rectangle(3, 4)


def display_area(shape: Shape):  # parameter's type is restricted to shape objects ONLY
    print(f'the  {shape.name}\' area is {shape.area()} ')


display_area( shape1 )
display_area( shape2)








