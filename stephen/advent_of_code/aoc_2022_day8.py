matrix = []
for line in open('input_8.txt', 'r'):
    row = []
    line = line.strip()
    for ch in line:
        row.append(int(ch))
    matrix.append(row)


def count_neighbours(matrix):
    seen = set()
    count = 0
    for i, cur_row in enumerate(matrix):
        row_max = 0
        for col_index, col in enumerate(cur_row):
            if (i, col_index) in seen:
                row_max = max(row_max, col)
                continue
            if col_index == 0 or col > row_max:
                count += 1
                seen.add((i, col_index))
            row_max = max(row_max, col)

    for i, cur_row in enumerate(matrix):
        row_max = 0
        for col_index in range(len(cur_row)-1, -1, -1):
            if (i, col_index) in seen:
                row_max = max(row_max, cur_row[col_index])
                continue
            if col_index == len(cur_row)-1 or cur_row[col_index] > row_max:
                count += 1
                seen.add((i, col_index))
            row_max = max(row_max, cur_row[col_index])


    for col_index in range(len(matrix[0])):
        col_max = 0
        for row_index in range(len(matrix)):
            if (row_index, col_index) in seen:
                col_max = max(col_max, matrix[row_index][col_index])
                continue
            if row_index == 0 or matrix[row_index][col_index] > col_max:
                count += 1 
                seen.add((row_index, col_index))
            col_max = max(col_max, matrix[row_index][col_index])
    
    for col_index in range(len(matrix[0])):
        col_max = 0
        for row_index in range(len(matrix)-1, -1, -1):
            if (row_index, col_index) in seen:
                col_max = max(col_max, matrix[row_index][col_index])
                continue
            if row_index == len(matrix) - 1 or matrix[row_index][col_index] > col_max:  
                count += 1
                seen.add((row_index, col_index))
            col_max = max(col_max, matrix[row_index][col_index])
   
    for c in seen:
        if 0 not in c:
            print(c)
    return count


print(count_neighbours(matrix)) # 20

