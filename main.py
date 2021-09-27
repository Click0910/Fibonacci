def fibonacci_function(n):
    if n == 0:
        fibonacci_list = [0]
        return fibonacci_list

    elif n == 1:
        fibonacci_list = [0, 1]
        return fibonacci_list

    elif n > 1:
        fibonacci_list = [0, 1]
        for i in range(0, (n-1)):
            sum = fibonacci_list[len(fibonacci_list)-1] + fibonacci_list[len(fibonacci_list)-2]
            fibonacci_list.append(sum)
        return fibonacci_list


num = int(input("Insert a number to make the fibonacci calculate: "))
fibonacci_series = fibonacci_function(num)
print(fibonacci_series)
