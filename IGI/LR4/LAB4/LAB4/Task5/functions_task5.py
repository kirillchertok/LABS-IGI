import numpy as np

class MatrixOperations:
    """
    Class for performing operations on matrices using NumPy.
    """
    def __init__(self, n, m):
        """
        Initializes the MatrixOperations class with the dimensions of the matrix.

        :param n: The number of rows in the matrix.
        :type n: int
        :param m: The number of columns in the matrix.
        :type m: int
        """
        self.n = n
        self.m = m
        self.matrix = self._generate_integer_matrix()

    def _generate_integer_matrix(self):
        """
        Generates an integer matrix A[n, m] using a random number generator.

        :return: A randomly generated integer matrix.
        :rtype: numpy.ndarray
        """
        return np.random.randint(0, 100, size=(self.n, self.m))

    def sort_matrix_by_last_column(self):
        """
        Sorts the matrix by the elements of the last column in descending order.

        :return: The sorted matrix.
        :rtype: numpy.ndarray
        """
        return self.matrix[np.argsort(self.matrix[:, -1])[::-1]]

    def calculate_mean_last_column(self):
        """
        Calculates the mean value of the elements in the last column of the matrix.

        :return: The mean value of the elements in the last column.
        :rtype: float
        """
        return np.mean(self.matrix[:, -1])

    def calculate_mean_last_column_manually(self):
        """
        Calculates the mean value of the elements in the last column of the matrix manually.

        :return: The mean value of the elements in the last column.
        :rtype: float
        """
        total = 0
        for row in self.matrix:
            total += row[-1]
        return total / len(self.matrix)