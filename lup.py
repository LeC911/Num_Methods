import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.a_matrix = matrix
        self.a_size = len(matrix)
        self.__LUP()

    def __LUP(self):
        c_matrix = self.a_matrix
        p_matrix = self.__create_identity_matrix()
        for i in range(self.a_size):
            pivot_value = 0
            pivot = -1
            for row in range(i, self.a_size):
                if abs(c_matrix[row][i] > pivot_value):
                    pivot_value = abs(c_matrix[row][i])
                    pivot = row

            # if pivot_value == 0:
            #     print("Матрица вырождена")
            #     return

            p_matrix = self.__swap_rows(p_matrix, pivot, i)
            c_matrix = self.__swap_rows(c_matrix, pivot, i)

            for j in range(i + 1, self.a_size):
                c_matrix[j][i] /= c_matrix[i][i]
                for k in range(i + 1, self.a_size):
                    c_matrix[j][k] -= c_matrix[j][i] * c_matrix[i][k]

        print(c_matrix)
        print(p_matrix)

    def __create_identity_matrix(self):
        identity_matrix = np.eye(self.a_size, dtype=int)
        return identity_matrix

    def __swap_rows(self, matrix, i, j):
        matrix[[i, j]] = matrix[[j, i]]
        return matrix


A = Matrix(np.array([[1, 2, 0],
              [3, 4, 4],
              [5, 6, 3]], dtype=float))

