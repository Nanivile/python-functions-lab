from collections import Counter

# Exercise 1:

def sum_to(n):
    new_num = 0
    for num in range(n+1):
        new_num += num
    return new_num

print(sum_to(6))

# Exercise 2:

def largest(arr):
    large = 0
    for num in arr:
        if num > large:
            large = num
    return large

nums = [1, 2 ,4 ,3 ,0]
more_nums = [10, 4, 2, 231, 91, 54]
print(largest(nums))
print(largest(more_nums))

# Exercise 3:

def occurences(string, occ):
    count = 0
    for element in range(len(string)):
        if occ[:len(occ)] == string[element:element+len(occ)]:
            count += 1
    return count

print(occurences('nnnicenin', 'n'))
print(occurences('nnniceniniinni', 'ni'))
    
# Exercise 4:

def product(*args):
    product = args[0]
    print(args)
    for num in args:
        product *= num
    return product

print(product(1, 4, 5, 6))

# Bonus Challenge:

def steps_to_zero(n):
    n = int(n)
    count = 0
    while n > 0:
        if (n % 2) != 0:
            n = n - 1
            count += 1
        else:
            n /= 2
            count += 1
    return count

print(steps_to_zero(16))