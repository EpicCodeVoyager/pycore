x_list = [1, 2, 3, 5, 6]
x_dict = {1: 'some', 2: 'phone', 3: 'loan'}

y_list = [2 * x for x in x_list]
z_list = map(lambda x: 2*x + 3, x_list)
print(list(z_list))

for i in range(10):
    print(i)

for i in range(2, 11):
    print(i)

all_100 = [x for x in range(1, 101)]
print(all_100)
