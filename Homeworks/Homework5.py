#The Odd Ones Out
import numpy as np
def onlyOdd(arr):
    odd_rows = arr % 2 == 1
    return arr[np.all(odd_rows, axis=1)]
arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
onlyOdd(arr)
result = onlyOdd(arr)
print(result)

#2.1
import numpy as np
def checkerboard():
    return np.zeros((8, 8), dtype = int)
matrix = checkerboard()
print(matrix)

#2.2
import numpy as np
def checkerboard():
    matrix = np.zeros((8, 8), dtype = int)
    matrix[0::2] = np.array([[1, 0, 1, 0, 1, 0, 1, 0]] * 4)
    return matrix
matrix = checkerboard()
print(matrix)

#2.3
import numpy as np
def checkerboard():
    matrix = np.zeros((8, 8), dtype = int)
    matrix[0::2] = np.array([[1, 0, 1, 0, 1, 0, 1, 0]] * 4)
    matrix[1::2] = np.array([[0, 1, 0, 1, 0, 1, 0, 1]] * 4)
    return matrix
matrix = checkerboard()
print(matrix)

#2.4
import numpy as np
def reverse_checkerboard():
    matrix = np.ones((8, 8), dtype = int)
    matrix[0::2] = np.array([[0, 1, 0, 1, 0, 1, 0, 1]])
    matrix[1::2] = np.array([[1, 0, 1, 0, 1, 0, 1, 0]])
    return matrix
matrix = reverse_checkerboard()
print(matrix)

#2.5
import numpy as np
def expansion(universe, spaces):
    space_string = ' ' * spaces
    return np.array([space_string.join(word) for word in universe])
universe = np.array(['galaxy', 'clusters'])
result_1 = expansion(universe, 1)
result_2 = expansion(universe, 2)
print(result_1)
print(result_2)

#2.6
import numpy as np
def secondLargest(arr):
    second_largest = np.array([np.partition(col, -2)[-2] for col in arr])
    return second_largest
np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
result = secondLargest(planets)
print(result)

