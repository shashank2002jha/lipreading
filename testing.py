import os

def convert_time(file):
  file1 = open(file, 'r')
  Lines = file1.readlines()   # it will read the content of file in form of a list (in a single line with backslash denoting next line)
  count = 0
  output = []               #created an empty list
  for line in Lines:
      count += 1
      ll = line.split(' ')    #it will split the string in list based on criteria present in the ()
      ll[0] = str(int(float(ll[0]) * 30000)) + " "
      ll[1] = str(int(float(ll[1]) * 30000)) + " "
      output = output + ll
  output_file = file.replace("In_folder", "out_folder")
  file2 = open(output_file, 'w')
  file2.writelines(output)
  file2.close()

input_folder = "C:\\Users\\s27jh\\OneDrive\\Desktop\\s2_51_moi_ruti_khalu.lab"
# for x in os.listdir(input_folder):            #it will include all files and directories present within input folder
#   if x.endswith(".lab"):
#     In_file = os.path.join(input_folder, x)   #it will join s2_.... and .lab
#     convert_time(In_file)
convert_time(input_folder)