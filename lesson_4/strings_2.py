last_name= "Kalashnikov"
print("ka" in last_name)
print(len(last_name))
print(len(""))
print(last_name[0])
print(last_name[1])
print(last_name[2])
print(last_name[3])

print(last_name[len(last_name)-1])
print(last_name[0:4+1])
print(last_name[::-1])
print(last_name[-1:-6:-1])
print(last_name[-1:-8:-2])

name_len=len(last_name)
print(last_name[:name_len-1])

print(last_name.index("n"))
print(last_name.find("a"))


students= "Ivanov, Sidorov, Petrov"
students=students.split(",")
print(students)
print(len(students))
print(type(students))
print(students[2])
list_of_students=",".join(students)
print(list_of_students)
print(type(list_of_students))
print("students are: "+list_of_students)
