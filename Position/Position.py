class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def UPosition(self, rowSteps, colSteps):
        self.row += rowSteps
        self.column += colSteps

    def URow(self, steps):
        self.row += steps

    def UCol(self, steps):
        self.column += steps

    def fetchRow(self):
        return self.row

    def FetchCol(self):
        return self.column

    def __str__(self):
        return "Row: " + str(self.row) + " Column: " + str(self.column)