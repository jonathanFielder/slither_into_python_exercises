import sys

total = 0

i = 1
while i < len(sys.argv):
    total += int(sys.argv[i])
    i += 1
print(total)
