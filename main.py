def def_matrix():
    while True:
        try:
            rows = int(input("Digite o número de linhas da matriz: "))
            cols = int(input("Digite o número de colunas da matriz: "))
            matrix = []
            print("Insira os elementos da matriz, um por vez:")
            for i in range(rows):
                row = [] # para cada linha cria uma lista vazia row
                for j in range(cols):
                    element = int(input(f"Elemento ({i+1},{j+1}): "))
                    row.append(element)
                matrix.append(row)
            print("\nMatriz inserida:")
            print_matrix(matrix)  # Chama a função para exibir a matrix
            return matrix
        except ValueError as e:
            print("Erro: Entrada inválida. Por favor, insira os valores corretamente.\n")

def print_matrix(matrix):
    for row in matrix:
        print(row)

def can_multiply(matrix1, matrix2):
    return len(matrix1[0]) == len(matrix2)

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        result_row = []
        for j in range(len(matrix2[0])):
            sum_product = 0
            for k in range(len(matrix2)):
                sum_product += matrix1[i][k] * matrix2[k][j]
            result_row.append(sum_product)
        result.append(result_row)
    return result

def main():
    print("Defina a primeira matriz:")
    matrix1 = def_matrix()

    print("\nDefina a segunda matriz:")
    matrix2 = def_matrix()

    if can_multiply(matrix1, matrix2):
        print("\nResultado da multiplicação das matrizes:")
        result = multiply_matrices(matrix1, matrix2)
        for row in result:
            print(row)
    else:
        print("\nErro: As matrizes não podem ser multiplicadas.")
        print(f"A matriz 1 tem {(matrix1[0])} colunas e a matriz 2 tem {len(matrix2)} linhas.")
        print("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

main()
