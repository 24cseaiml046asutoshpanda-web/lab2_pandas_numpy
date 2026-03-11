def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def multiply(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*matrix2)] for row1 in matrix1]

def inverse_2x2(matrix1):
    det = matrix1[0][0] * matrix1[1][1] - matrix1[0][1] * matrix1[1][0]
    return [[matrix1[1][1] / det, -matrix1[0][1] / det], [-matrix1[1][0] / det, matrix1[0][0] / det]]

def multiverite_regresion(x,y):
    XT = transpose(x)
    XT_X = multiply(XT,x)
    XT_X_inv = inverse_2x2(XT_X)
    XT_Y = multiply(XT,y)
    return multiply(XT_X_inv,XT_Y)

# MAIN PROGRAM 

n = int(input("Enter the number of data points: "))
m = int(input("Enter the number of independent variables: "))
x = []
y = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(float(input(f"Enter value for x{i+1}y{j+1}: ")))
    x.append(row)
    y.append(float(input(f"Enter value for y{i+1}: ")))

coefficients = multiverite_regresion(x,y)
print("Coefficients:", coefficients)