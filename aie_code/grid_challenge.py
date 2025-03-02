def gridChallenge(grid):
    if grid == []:
        return "NO"

    sorted_row = []
    for row in grid:
        sorted_row.append(sorted(row))
    # จะเรียงลำดับก่อน
    for col in range(len(sorted_row[0])):
        for row in range(1, len(sorted_row)):
            if sorted_row[row - 1][col] > sorted_row[row][col]:
                return "NO"

    return "YES"
