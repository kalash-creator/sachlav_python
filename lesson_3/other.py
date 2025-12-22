from operator import truediv

print(type(True))
print(type(25))
age=input('Enter your age: ')
print(type(age))


number_1=input('Enter your first number: ')
number_2=input('Enter your second number: ')
print(f"{number_1} + {number_2} = {number_1+number_2}")


number_1=int(input('Enter your first number: '))
number_2=int(input('Enter your second number: '))
print(f"{number_1} + {number_2} = {number_1+number_2}")

number_1=float(input('Enter your first number: '))
number_2=float(input('Enter your second number: '))
print(f"{number_1} + {number_2} = {number_1+number_2}")


score1, score2 = input("Enter your first score and your second score: ").split( )
score1 = int(score1)
score2 = int(score2)
print (score1, type(score1), score2, type(score2))

score1, score2, score3 = map(int, input("Enter your 3 scores: ").split( ))
print (f"score1: {score1}, {type(score1)}")
print (f"score2: {score2}, {type(score2)}")
print (f"score3: {score3}, {type(score3)}")