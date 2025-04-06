class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array to store each row as a string
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and distribute characters in rows
        for char in s:
            rows[current_row] += char
            # Change direction if we are at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down based on the flag
            current_row += 1 if going_down else -1
        
        # Combine the rows into one string
        return ''.join(rows)


# Test cases
def test_zigzag_conversion():
    solution = Solution()
    
    # Test case 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print(f"Test 1 - Expected: 'PAHNAPLSIIGYIR', Output: {solution.convert(s1, numRows1)}")
    
    # Test case 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print(f"Test 2 - Expected: 'PINALSIGYAHRPI', Output: {solution.convert(s2, numRows2)}")
    
    # Test case 3
    s3 = "A"
    numRows3 = 1
    print(f"Test 3 - Expected: 'A', Output: {solution.convert(s3, numRows3)}")
    
    # Test case 4 - Edge case where numRows >= len(s)
    s4 = "HELLO"
    numRows4 = 5
    print(f"Test 4 - Expected: 'HELLO', Output: {solution.convert(s4, numRows4)}")
    
    # Test case 5 - Edge case where numRows = 1
    s5 = "ABCDEF"
    numRows5 = 1
    print(f"Test 5 - Expected: 'ABCDEF', Output: {solution.convert(s5, numRows5)}")

# Run the test cases
test_zigzag_conversion()
