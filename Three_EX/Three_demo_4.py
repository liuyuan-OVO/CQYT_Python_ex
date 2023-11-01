def fibonacci():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

Fibonacci = fibonacci()
for num in Fibonacci:
    print(num)