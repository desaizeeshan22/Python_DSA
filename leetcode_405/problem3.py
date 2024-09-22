def numberOfSubmatrices(grid):
    freq = [[] for _ in range(len(grid) + 1)]
    for i in range(len(grid) + 1):
        for j in range(len(grid[0]) + 1):
            freq[i].append([0, 0])
    cnt_x = 0
    cnt_y = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                cnt_x += 1
            if grid[i][j] == 'Y':
                cnt_y += 1
            freq[i + 1][j + 1] = [cnt_x, cnt_y]

    res = 0
    for i in range(1, len(freq)):
        for j in range(1, len(freq[0])):
            if j < len(freq[0]) - 1 and i != 1:
                temp_x = freq[i][j][0] - freq[1][j + 1][0] + freq[1][j][0]
                temp_y = freq[i][j][1] - freq[1][j + 1][1] + freq[1][j][1]
            else:
                temp_x = freq[i][j][0]
                temp_y = freq[i][j][1]
            if temp_x >= 1 and temp_x == temp_y:
                res += 1
    return res


print(numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]))
