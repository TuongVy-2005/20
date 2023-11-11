a=int(input())
b=int(input())
c=int(input())
if (a+b)>c and (a+c)>b and (b+c)>a:
    if (a==b) and (a==c) and (b==c):
        print ('The triangle is equilateral')
    elif (a==b!=c) or (a==c!=b) or (b==c!=a):
        print('The triangle is isosceles ')
    else:
        print('The triangle is scalene ')