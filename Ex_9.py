def generator(n):
    length = n
    while length >= 0:
        yield length
        length -= 1

new_generator = generator(5)

for values in new_generator:
    print(values)