'''
3D Matrix
Definition:
A 3D matrix is an array set that contains three dimensions (x, y, z). 
Each element of z is a page, whereas accessed by the key (z) and then printable by iterating through that page's x and y axes.
Each element in the matrix can be initialized with any Object, such as a string, integer, or even another array.
Nested objects in such arrays can be accessed by using multiple keys, such as matrix[z][x][y], to retrieve the desired element.
'''

# Example of a 3D Matrix in Python
def matrixOf(x, y, z):
    # Initialize a 3D matrix with zeros
    matrix = [[[0 for _ in range(y)] for _ in range(x)] for _ in range(z)]
    return matrix

def getElement(matrix, z, x, y):
    # Access an element in the 3D matrix
    return matrix[z][x][y]

def setElement(matrix, z, x, y, value):
    # Set an object in the 3D matrix
    matrix[z][x][y] = value
    
def containsElement(matrix, value):
    # Check if the value exists in the 3D matrix
    for z in range(len(matrix)):
        for x in range(len(matrix[z])):
            for y in range(len(matrix[z][x])):
                if matrix[z][x][y] == value:
                    return True
    return False

def printMatrix(matrix):
    # Print the 3D matrix
    for z in range(len(matrix)):
        print(f"Page {z}:")
        for x in range(len(matrix[z])):
            print(matrix[z][x])
        print()  # Add a newline for better readability

def main():
    matrix = matrixOf(3, 3, 2)  # Create a 3D matrix with dimensions 3x3x2
    setElement(matrix, 0, 0, 0, 1)  # Set element at (z=0, x=0, y=0) to 1
    setElement(matrix, 0, 1, 1, 2)  # Set element at (z=0, x=1, y=1) to 2
    setElement(matrix, 1, 2, 2, 3)  # Set element at (z=1, x=2, y=2) to 3
    printMatrix(matrix)  # Print the 3D matrix
    print(getElement(matrix, 0, 1, 1))  # Get element at (z=0, x=1, y=1)
    print(containsElement(matrix, 2))  # Check if value 2 exists in the matrix
    print(containsElement(matrix, 4))  # Check if value 4 exists in the matrix
    
if __name__ == "__main__":    
    main()