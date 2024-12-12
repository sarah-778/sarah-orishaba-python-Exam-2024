def sum_of_odd_num():
    integers = [4, 7, 2, 9, 12, 15]
    sum_odd = 0
    for num in integers:
        if num % 2 != 0:
            sum_odd += num
    print(f"The sum of all odd numbers is: {sum_odd}")
sum_of_odd_num() 
    
