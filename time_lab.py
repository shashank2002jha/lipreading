import csv
from curses.ascii import isdigit
import os
# from pickle import TRUE
# h = open("C:\\Users\\s27jh\\OneDrive\\Desktop\\r.txt", "r")
# content = h.readlines()


import re
with open("C:\\Users\\s27jh\\OneDrive\\Desktop\\r.txt") as f:
	# print(re.findall('\d*?\.\d+', f.read()))
	n = (re.findall('\d*?\.\d+', f.read()))


out = []
for item in n:
    out.append(float(item))
print(out, end=" ")
print(type(out))
for i in out:
	i = i*1000
	print(i)
	# print(type(i))

# for i in  n:
# 	print(i)
# 	print(type(i))



# # print(content)
# a = 0
# for line in content:
# 	words = line.split()
# 	for i in words:
# 		if i.isfloat() == True:
# 			print(i)
# 		else:
# 			print("no")
# ============================================================================
# new_list = []
# for row in data:
#   split_row = row.split(',')
#   if len(split_row) > 1:
#     new_list.append(float(split_row[1]))
# ============================================================================
# with open("C:\\Users\\s27jh\\OneDrive\\Desktop\\r.txt", "r") as file1:
#     f_list = [float(i) for line in file1 for i in line.split(',') if i.strip()]
# print(f_list)
# -----------------------------------------------------------------
        # Checking for the digit in
        # the string
    # if line.isdigit() == True:
             
    #        line = line*1000
            

# # creating a variable and storing the text
# # that we want to add
# replace_text = "replaced"

# # Opening our text file in read only
# # mode using the open() function
# with open(r'SampleFile.txt', 'r') as file:

# 	# Reading the content of the file
# 	# using the read() function and storing
# 	# them in a new variable
# 	data = file.read()

# 	# Searching and replacing the text
# 	# using the replace() function
# 	data = data.replace(search_text, replace_text)

# # Opening our text file in write only
# # mode to write the replaced content
# with open(r'SampleFile.txt', 'w') as file:

# 	# Writing the replaced data in our
# 	# text file
# 	file.write(data)

# # Printing Text replaced
# print("Text replaced")
