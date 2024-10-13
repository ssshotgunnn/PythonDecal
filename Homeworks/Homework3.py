# Oski Stole Your Power
def computePower(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / computePower(x, -y)
    else:
        return x * computePower(x, y - 1)

# What Should I Wear?
def temperatureRange(readings):
    return (min(readings), max(readings))

readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))

# Check if Its the Weekend
def isWeekend(day):
    return day == 6 or day == 7

day = 6  
print(isWeekend(day))  

# Fuel Efficiency 
def fuel_efficiency(distance, fuel):
    return distance / fuel

distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))

# Secret Code 
def decodeNumbers(n):
    last_digit = n % 10
    n //= 10
    num_digits = 0
    temp = n
    while temp > 0:
        temp //= 10
        num_digits += 1
    new_number = last_digit * (10 ** num_digits) + n
    return new_number

n = 12345
print(decodeNumbers(n)) 

# For Loop
def find_min_with_for_loops(nums):
    minvalue = nums[0]
    for i in nums:
        if i < minvalue:
            minvalue = i
    return minvalue

def find_max_with_for_loops(nums):
    maxvalue = nums[0]
    for i in nums:
        if i > maxvalue:
            maxvalue = i
    return maxvalue

nums = [2024, 98, 131, 2, 3, 72]
print(find_max_with_for_loops(nums))
print(find_min_with_for_loops(nums))

# While Loop
def find_min_with_while_loop(nums):
    i = 0
    while i < len(nums):
        minvalue = nums[0]
        if i < minvalue:
            minvalue = i
        return minvalue
    i += 1

def find_max_with_while_loops(nums):
    i = 0
    while i < len(nums):
        maxvalue = nums[0]
        if i > maxvalue:
            maxvalue = i
        return maxvalue
    i += 1

nums = [2024, 98, 131, 2, 3, 72]
print(find_max_with_while_loops(nums))
print(find_min_with_while_loop(nums))

#Sorry I tried my best but the second one is not working and I am not sure why!!!

#Counting Vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for chars in text:
        if chars.isalpha:
            if chars in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))

#Calculate Digital Root
def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10  
        num //= 10         
    return total

num = 2468
print(digital_root(num))   