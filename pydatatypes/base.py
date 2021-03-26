from array import array
'''
File contains initialization/declaration 
of different inbuilt data types
in python 3.6+, which are commonly utilised.  
'''
x_int = 1
y_float = 1.0
z_string = "HelloWorld"
# List/Set with different types.
general_list = [1, 2.0, "3", "red", "object"]
general_set = set([1, 2, 3, "red", 1, "blue"])

# Initializing set:
general_set_2 = {1, 2, 3, "blue", "3"}

#tuples
general_tuple = (1, 2, 3, 5, 6, "qery")
general_tuple = (1, 3)

print(f"tuple:{general_tuple}")

# Printing with format string.
print(f"{general_set}")
print("{}".format(general_list))

# Python array
'''
Type code   C Type             Minimum size in bytes 
        'b'         signed integer     1 
        'B'         unsigned integer   1 
        'u'         Unicode character  2 (see note) 
        'h'         signed integer     2 
        'H'         unsigned integer   2 
        'i'         signed integer     2 
        'I'         unsigned integer   2 
        'l'         signed integer     4 
        'L'         unsigned integer   4 
        'q'         signed integer     8 (see note) 
        'Q'         unsigned integer   8 (see note) 
        'f'         floating point     4 
        'd'         floating point     8 
'''

int_arr = array('b', [1, 2, 3, 4, 7, 9])
print(f"{int_arr}")

# Casting array to set and list
int_set = set(int_arr)
int_list = list(int_arr)
print(f"set: {int_set}")
print(f"list: {int_list}")

# Dictionary
dictionary1 = dict()
dictionary1['key1'] = "value1"
dictionary1['key2'] = "value2"
dictionary1['key3'] = "value3"

# Single line initialization
dictionary2 = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"}
print(f"dictionary1{dictionary1}\ndictionary2{dictionary2}")
