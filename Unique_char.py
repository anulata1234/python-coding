#Python program to check if a string contains all unique character

string_1 = raw_input("enter a string")
string_1 = list(string_1)           
for i in list(set(string_1)):
	  count_string = list(string_1).count(i)
	  if count_string > 1:
	  print (i, count_string)
