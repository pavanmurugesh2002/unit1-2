print('enter your name the height, length and width of your desired pool')
name = int(input()) #square and rectangle
height = int(input())
length = int(input())
width = int(input())
volume = (length * width * height * 7.5)
print(name, volume)


print('enter your name height diameter radius of your desired pool')
name1 = int(input()) #cylinder
height = int(input())
diameter = int(input())
radius = diameter/2
import math
from math import pi
print (name1,((pi*radius**2)*h*5.875))



print('first enter all four of your names the your respective gpas')
student1 = int(input()) # Average GPA
student2 = int(input())
student3 = int(input())
student4 = int(input())
gpa1 = int(input())
gpa2 = int(input())
gpa3 = int(input())
gpa4 = int(input())
print(student1,student2,student3,student4,(gpa1 + gpa2 + gpa3 + gpa4)/4)


print('digit by digit enter a two digit number that you want swapped')
tens = int(input()) # Swapping digits of two digit numbers
ones = int(input())
print(tens,ones)
print(ones,tens)


year = int(input()) # print century giver year
import math 
from math import floor
century = floor(year/100) + 1
print(century)




print('enter an a, b, and h value respectively')
a = int(input()) #snail
b = int(input())
h = int(input())
movement = (a - b)
print(h/movement)

k = int(input())
 day = ((k%7) + 4)
 print(day)
