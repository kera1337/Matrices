
def generate_matrix1(rows, cols):
    matrix1 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elemant = int(input(f"Enter element [{i},{j}]: "))
            row.append(elemant)
        matrix1.append(row)

    print("MATRIX A:")

    for row in matrix1:
        print(row)

    return matrix1           

def generate_matrix2(rows, cols):
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elemant = int(input(f"Enter element [{i},{j}]: "))
            row.append(elemant)
        matrix2.append(row)

    print("MATRIX B:")

    for row in matrix2:
        print(row)

    return matrix2
   

def generate_matrix_c(matrix1, matrix2):

    num_of_rowsA = len(matrix1)
    num_of_colsA = len(matrix1[0])
    num_of_rowsb = len(matrix2)
    num_of_colsb = len(matrix2[0])

    if num_of_colsA != num_of_rowsb:
        print("Matrix multiplication is not possible")
        return None

    c = []
    c = [[0 for _ in range(num_of_colsb)] for _ in range(num_of_rowsA)]

    for i in range(num_of_rowsA):
        for j in range(num_of_rowsb):
            for k in range(num_of_colsA):
                c[i][j] += a[i][k] * b[k][j]

    print("MATRIX C:")

    for row in c:
        print(row)

    return c
        


while True:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of collumns: "))

    a = generate_matrix1(rows, cols)
    b = generate_matrix2(rows, cols)
    c = generate_matrix_c(a, b)

    if c is not None:
        print("Your are finished")
    else:
        print("try again")



    

