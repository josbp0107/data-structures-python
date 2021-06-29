from arrays import Array

"""
Grid type class
Methods:
    1. Initialize
    2. Get height
    3. Get width
    4. Access item
    5. String representation
"""

class ArrayTwoDimension:
    """
    Args:
        rows(int): numbers of rows in the matrix.
        columns(int): numbers of columns in the matrix.
        fill_value(any, optional): Value at each position. Default is None.
    """
    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    
    def get_height(self):
        """ Return length of the rows in the matrix."""
        return len(self.data)
    
    def get_width(self):
        """Return length of the columns in the matrix."""
        return len(self.data[0])
    
    def __getitem__(self,index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + " "
            result += "\n"
        
        return str(result)