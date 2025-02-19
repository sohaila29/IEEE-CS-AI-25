def get_numbers():
    while True:
        try:
            numbers = input("Enter list of numbers (separated by commas or sppaces): ").strip()

            if not numbers:
                raise ValueError("list can't be empty!")

            numbers = numbers.replace(" ", ",")
            numbers_list =[number.strip() for number in numbers.split(",")]

            if not all(number.isdigit() for number in numbers_list):
                raise ValueError("input valid integers separated by commas")
            
            numbers_list =[int(i) for i in numbers_list]
            print("valid list: ", numbers_list)
            return numbers_list
        
        except ValueError as e:
            print(f"invalid input: {e}. please try again!")
#-----------------------------------------------------------------------------------
def find_min(numbers):
    min_num = numbers[0]
    for i in numbers[1:]:
        if i < min_num:
            min_num = i
    return min_num
#-----------------------------------------------------------------------------------
def find_max(numbers):
    max_num = numbers[0]
    for i in numbers[1:]:
        if i > max_num:
            max_num = i
    return max_num
#-----------------------------------------------------------------------------------
def find_length(numbers):
    n = 0
    for i in numbers:
        n +=1
    return n
#-----------------------------------------------------------------------------------
def find_mean(numbers):
    sum_list = 0
    for i in numbers:
        sum_list += i
    return sum_list/find_length(numbers)
#-----------------------------------------------------------------------------------
def find_mode(numbers):
    occurrence ={}
    for i in numbers:
        if i in occurrence:
            occurrence[i] +=1
        else:
            occurrence[i]= 1

    max_occur = 0
    mode = []
    for i in occurrence:
        if occurrence[i]>max_occur:
            max_occur = occurrence[i]
            mode = [i]
        elif occurrence[i]== max_occur:
            mode.append(i)
    return mode     
#-----------------------------------------------------------------------------------
def find_median(numbers):
    sorted_nums = sorted(numbers)
    median = (find_length(numbers) + 1)//2
    if find_length(numbers) % 2 == 0:
        return (sorted_nums[median-1] + sorted_nums[median]) / 2
    else:
        return sorted_nums[median-1]
#-----------------------------------------------------------------------------------
def find_range(numbers):
    return find_max(numbers) - find_min(numbers)
#-----------------------------------------------------------------------------------
def find_variance(numbers):
    mean = find_mean(numbers)
    square_sum = sum((i - mean) ** 2 for i in numbers)
    return square_sum / (find_length(numbers)-1)
#-----------------------------------------------------------------------------------
def find_STD(numbers):
    return find_variance(numbers) ** 0.5
#-----------------------------------------------------------------------------------
def find_Quariles(numbers):
    sorted_nums = sorted(numbers)
    middle = find_length(numbers) // 2
    
    lower_half = sorted_nums[:middle]
    upper_half = sorted_nums[middle + (find_length(numbers)%2):]

    Q1 = find_median(lower_half)
    Q2 = find_median(sorted_nums)
    Q3 = find_median(upper_half)
    return (Q1, Q2, Q3)
#-----------------------------------------------------------------------------------
def find_IQR(numbers):
    quarts = find_Quariles(numbers)
    IQR = quarts[2] - quarts[0]
    return IQR
#-----------------------------------------------------------------------------------
numbers = get_numbers()
print("MIN:", find_min(numbers))
print("Max:", find_max(numbers))
print("Mean:", round(find_mean(numbers), 1))
print("Mode:", find_mode(numbers))
print("Median:", find_median(numbers))
print("Range:", find_range(numbers))
print("Variance:", round(find_variance(numbers), 2))
print("Standard Deviation:", round(find_STD(numbers), 5))
print("Quartiles:", find_Quariles(numbers))
print("Interquartile Range (IQR):", find_IQR(numbers))




    
