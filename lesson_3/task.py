# s=5
# print(s ** 2)
# print(pow(s,2))


# a=float(input('Enter number: '))
# b=float(input('Enter another number: '))
# print(a*b)
# print(2*(a+b))
#
# a=float(input('Enter a temperature value in Fahrenheit: '))
# print(((a-32)*5)/9)
#
# a,b,c,d=map(float,input("enter 4 numbers: ").split())
# print((a+b+c+d)/4)
#
# a,b,c,d, e=map(int,input("enter 5 numbers: ").split())
# print(max(a,b,c,d,e))
#
# a=int(input("Enter number: "))
# print((a-1),a, (a+1), sep='<')

a,b,c=map(float,input("enter 3 numbers: ").split())
print(max((a+b+c), (a*b*c), ((a+b)*c),a*(b+c),(a*b+c), (a+b*c)))

x,y,z=map(int,input('Enter prices: ').split())
print(3*x+ (3+2)*y+ (3+2+7)*z)
