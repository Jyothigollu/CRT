n = int(input("Enter number of elements: "))
l = [int(input("Enter element: ")) for _ in range(n)]

# Use two pointers to modify the list in place
write_index = 0

# Move all non-zero elements to the front
for i in range(n):
    if l[i] != 0:
        l[write_index] = l[i]
        write_index += 1

# Fill the remaining positions with zeros
for i in range(write_index, n):
    l[i] = 0

print(l)
