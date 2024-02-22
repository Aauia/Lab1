# Example 1
def generate_square_numbers(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
squares = generate_square_numbers(n)
print(*list(squares))

# Example 2
def generate_even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
even_nums = generate_even_numbers(n)
print(','.join(map(str, list(even_nums))))

# Example 3
def generate_numbers_divisible_by_three_and_four(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
divisible_nums = generate_numbers_divisible_by_three_and_four(n)
print(*list(divisible_nums))

# Example 4
def generate_square_numbers_in_range(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input())
b = int(input())
squares_range = generate_square_numbers_in_range(a, b)
for value in squares_range:
    print(value)

# Example 5
def countdown_from(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
countdown_gen = countdown_from(n)
print(*list(countdown_gen))
