print("FIBONACCI NUMBERS")
count = 2

def fibonacci(num1, num2):
    global count
    if count >= 12:
        return

    new_num = num1 + num2
    count += 1
    print(new_num)

    num1 = num2
    num2 = new_num

    fibonacci(num1, num2)

while True:
    nums = input("enter two numbers which you want to see the fibonacci numbers of(separate number by ','): ")
    if ',' not in nums:
        print("enter two numbers and separate them with a comma")
        continue

    nums = nums.split(',')
    if len(nums) != 2:
         print("Enter extactly two number and seperate them by comma.")
         continue
    try:
            num1 = int(nums[0])
            num2 = int(nums[1])
    except ValueError:
        print("Enter a valid number")
        continue

    print(num1)
    print(num2)
    fibonacci(num1, num2)
    
    break
