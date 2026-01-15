from typing import List

def traverse_matrix(matrix: List[List[int]]) -> None:
    """
    Traverse and print a 2D Array (Matrix).
    
    Time Complexity: O(n * m)
    -------------------------
    Where n is the number of rows and m is the number of columns.
    We visit every element exactly once.
    """
    
    # 1. Handle edge case: Empty matrix
    if not matrix:
        print("Matrix is empty!")
        return

    # 2. Get dimensions
    rows = len(matrix)
    cols = len(matrix[0]) # Assuming it's a rectangular matrix

    print(f"Matrix Dimensions: {rows}x{cols}\n")

    # 3. Nested Loop for traversal
    # Outer loop iterates through rows (i)
    for i in range(rows):
        # Inner loop iterates through columns (j)
        for j in range(cols):
            # Access element at [row][col]
            print(matrix[i][j], end='\t') # \t for tab space (cleaner)
        
        # New line after finishing each row
        print() 

# --- Main Execution ---
if __name__ == "__main__":
    # Example 3x3 Matrix
    data_2d = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

    print("--- 2D Array Traversal ---")
    traverse_matrix(data_2d)