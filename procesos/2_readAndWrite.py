with open("test1.txt", "r") as f:
    lines = f.readlines()
new_lines = []
for i in range(int(len(lines)/2)):
    new_lines.append(lines[i])
new_lines.append("####Esto va justo en la mitad del txt####\n")
for i in range(int(len(lines)/2)+1,len(lines)+1):
    new_lines.append(lines[i-1])

with open('test1.txt', 'w') as f:
    f.writelines(new_lines)
print (new_lines)
