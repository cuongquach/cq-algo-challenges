import sys

# Get input from console
list_input = []
no_of_lines = sys.stdin.readline().strip()
for i in range(int(no_of_lines)):
    line = sys.stdin.readline().strip()
    list_input.append(tuple(line.split(' ')))

# Get list first li and list second ri
ls = []
rs = []
for item in list_input:
    ls.append(int(item[0].strip()))
    rs.append(int(item[1].strip()))

# Sort li and sort reverse ri
# Then get tuple result that can cover range
ls.sort()
rs.sort(reverse=True)
result = (ls[0], rs[0])

# Default index
index = -1
index_incr = 0

for item in list_input:
    index_incr += 1
    if int(result[0]) == int(item[0].strip()) and int(result[1]) == int(item[1].strip()):
        index = index_incr

print(str(index))
