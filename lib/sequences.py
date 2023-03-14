#!/usr/bin/env python3

# def print_fibonacci(length):
#     if length == 0:
#         return []
#     elif length == 1:
#         print([0])
#         return [0]
#     fib = [0, 1]
#     while len(fib) < length:
#         next_fib = fib[-1] + fib[-2]
#         fib.append(next_fib)
#     print(fib)
#     return fib

def print_fibonacci(length):
    fibonacci_list = []
    if length > 0:
        fibonacci_list.append(0)
        if length > 1:
            fibonacci_list.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i -2])
    print(fibonacci_list)