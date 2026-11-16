prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
i = 0
try:
	user_input = int(input("how numbers of the fibonacci algorithm do yo want to see: "))
except ValueError:
	print("invalid input")
while i < user_input:
    i += 1
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo