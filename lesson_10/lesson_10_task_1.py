class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return str(self.matrix_list)

    def __add__(self, other):
        new_list = []
        for i, val in enumerate(self.matrix_list):
            self.matrix_list.extend([0, ] * (len(other.matrix_list) - len(self.matrix_list)))
            other.matrix_list.extend([0, ] * (len(self.matrix_list) - len(other.matrix_list)))
            result = list(map(sum, zip(val, other.matrix_list[i])))
            new_list.append(result)
        return Matrix(new_list)


mat_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix1 = Matrix(mat_1)

mat_2 = [[1, 2, 12], [5, 6, 7], [4, 5, 6]]
new_matrix2 = Matrix(mat_2)

mat_3 = [[1, 2, 10], [77, 22, 14], [5, 7, 1]]
new_matrix3 = Matrix(mat_3)

mat_4 = [[1, 2, 10], [77, 22, 14], [5, 7, 1]]
new_matrix4 = Matrix(mat_4)

new_matrix5= new_matrix1 + new_matrix2 + new_matrix3 + new_matrix4
print(new_matrix5)
