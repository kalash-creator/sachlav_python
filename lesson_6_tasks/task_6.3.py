my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
my_list_2=list(filter(lambda x: x%2!=0, my_list))
my_list_3=list(map(lambda x: x**3, my_list_2))
print(my_list_3)
