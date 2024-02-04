def sum_(a, b, filename = 'sem.txt'):
    result = a + b
    with open(filename, 'w') as file:
        file.write(str(result)+ '\n')
        