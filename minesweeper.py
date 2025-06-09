def minesweeper(grid):
    """
    Given a 2D grid where:
    - "#" represents a mine
    - "-" represents an empty cell

    Returns a new grid where:
    - Each "-" is replaced by the number of adjacent mines
    - Each "#" remains unchanged
    """
    
    # Get number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Define 8 possible directions around a cell (N, NE, E, SE, S, SW, W, NW)
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    # Initialize the result grid
    result = []

    # Loop through every cell in the grid
    for r in range(rows):
        new_row = []  # Temporary list to build each new row
        for c in range(cols):
            # If the current cell is a mine, copy it directly
            if grid[r][c] == "#":
                new_row.append("#")
            else:
                count = 0  # Initialize mine counter
                # Check all 8 directions for adjacent mines
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # Neighbor row and column
                    # Check boundaries and count mine if present
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
                        count += 1
                # Replace "-" with the count of adjacent mines
                new_row.append(str(count))
        # Append the completed row to the result grid
        result.append(new_row)
    
    return result

# Example input grid
grid = [
    ["-", "#", "-", "-", "#"], 
    ["-", "-", "#", "#", "-"], 
    ["#", "-", "-", "-", "#"], 
    ["-", "-", "#", "-", "-"], 
    ["#", "#", "-", "#", "#"]
]

# Run the minesweeper function
result = minesweeper(grid)

# Display the result
for row in result:
    print(row)
