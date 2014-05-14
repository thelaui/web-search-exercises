import sys

in_file_name = sys.argv[1]

content = open(in_file_name).read()

print sum(bytearray(content))
