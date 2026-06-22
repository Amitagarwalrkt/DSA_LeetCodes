class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        current_row = 0
        direction = -1  # will flip to 1 on first step

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
            current_row += direction

        return ''.join(rows)