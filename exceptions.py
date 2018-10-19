inputs = [1, 56, 'street', 5.601, True]

for j in range(len(inputs)):
    try:
        i = int(inputs[j])
    except ValueError as err:
        print('Parse error: {0}'.format(err))
    else:
        print('Integer: {0}'.format(i))

# i is still in scope here
print(i)