import math

def paint_area_calculator(width:int,height:int,coverage:int):
    number_of_cans = (height * width)/coverage
    round_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")
width = int(input("Please enter the width of the wall: "))
height = int(input("Please enter the height of the wall: "))
coverage = int(input("Please enter de coverage of the wall: "))
paint_area_calculator(width,height,coverage)