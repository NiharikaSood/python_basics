# inserting string within a string
string1 = " I like %s" % "python"
print(string1)

temp = "educative"
string2 = " I like %s" %temp
print(string2)

string3 = " I like %s and %s" %("python", temp)
print(string3)


# inserting integer within a string
my_string = " %i + %i = %i" %(1,2,3)
print(my_string)


# inserting floats within a string
string4 = " %f " %(1.11)
print(string4)

string5 = " %.2f " %(1.11)
print(string5)

string6 = " %.2f " %(1.117)
print(string6)