# 1,000,000 sample points 
# randomely thrown at a square dart board with a circle inscribed in it.
# The circle has a radius of 1 unit (r=1).
# The square has a side length of 2 units (s=2).
# what is the probability of a dart landing inside the circle?

import random


def throw_dart():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    return x,y

def check_if_in_the_circle(x,y,radius):
    check=(x**2)+(y**2)<=(radius**2)
    return check

def monte_carlo_(dart_throws):
    count_of_throws_inside_circle=0
    radius=1

    for i in range(dart_throws):
        x,y=throw_dart()
        if check_if_in_the_circle(x,y,radius):
            count_of_throws_inside_circle+=1
    return count_of_throws_inside_circle/dart_throws

def main():
    no_of_throws=1000000
    print(monte_carlo_(no_of_throws))

if __name__=="__main__":
    main()

    

    




   


