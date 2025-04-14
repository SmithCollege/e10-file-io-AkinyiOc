# ------------------------------------------------------
#  This program will let you play around with File IO
# ------------------------------------------------------

# # simple opening of a file
# my_file = open("test_file.txt")

# # you can read all of the contents at once
# contents = my_file.read()

# #remember to close the file!
# my_file.close()

# print(contents)

# f_write = open("file2.txt", "w")
# f_write.write ("Now the file has some contents!!!")
# f_write.close()

# f_write = open("file2.txt", "a")
# f_write.write ("\nXXX THISIS NEW XXX")
# f_write.close()

# f_read = open("file2.txt", "r")
# contents = f_read.read()
# f_read.close()
# print(contents)



# # simple opening of a file
# my_file = open("test_file.txt")
# # you can read all of the contents at once
# contents = my_file.seek(22)
# print(contents)
# contents = my_file.read(34)
# print(contents)
# #remember to close the file!
# my_file.close()

my_file = open('test_file.txt')
lines = my_file.readlines()
print(lines[3], end="")
my_file.close()
