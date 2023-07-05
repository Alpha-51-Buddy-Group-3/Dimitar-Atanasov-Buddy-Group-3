# N = input().split()

# RowCol = []

# for i in N:
#     i = int(i)
#     RowCol.append(i)

# matrix = []

# for i in range(RowCol[0]):
#     row = []
#     for j in range(RowCol[1]):
#         row.append(2**(i + j))
#     matrix.append(row)

# for inner in matrix:
#     print(inner)

# result = []

# for i in range(RowCol[0]):
#     result.append(matrix[i][i])

# print(RowCol)

# print("Diagonal elements:", result)


# a = 4  # Replace 'a' with the desired value for the number of rows
# b = 4  # Replace 'b' with the desired value for the number of columns

# for row in range(a):
#     for col in range(b):
#         cornerHit = (row == 0 and col == 0) or (row == 0 and col == b - 1) or \
#                     (row == a - 1 and col == b - 1) or (row == a - 1 and col == 0)

#         hitWall = (row == 0 and (col > 0 and col < b - 1)) or \
#                   (col == 0 and (row > 0 and row < a - 1)) or \
#                   (row == a - 1 and (col > 0 and col < b - 1)) or \
#                   (col == b - 1 and (row > 0 and row < a - 1))

#         # Your desired actions based on the conditions go here
#         # For example:
#         if cornerHit:
#             print(f"Corner hit at row {row}, col {col}")
#         if hitWall:
#             print(f"Wall hit at row {row}, col {col}")


# def diagonal_walk(sizex, sizey, show_steps):
#     posx = 0
#     posy = 0
#     sum = 1
#     deltay = 1
#     deltax = 1
#     sizex -= 1  # valid cols are: 0 - sizex-1
#     sizey -= 1  # valid rows are: 0 - sizey-1
#     if show_steps:
#         print("At: 0/0:1")

#     def power_of_two(x):
#         return 2 ** x

#     while not ((posx == 0 or posx >= sizex) and (posy == 0 or posy >= sizey)):
#         posx += deltax
#         posy += deltay
#         sum += power_of_two(posx) * power_of_two(posy)
#         if show_steps:
#             print(f"At: {posy}/{posx}:{power_of_two(posx) * power_of_two(posy)}")

#         # wallhit left or right
#         if posx == 0 or posx >= sizex:
#             deltax = -deltax
#         # wallhit top or bottom
#         if posy == 0 or posy >= sizey:
#             deltay = -deltay

#     return sum

# # Main function


# def main():
#     sum_result = diagonal_walk(3, 4, True)
#     print("result is:", sum_result)


# if __name__ == "__main__":
#     main()

# def diagPath(M):
#     r,c   = 0,0  # current position
#     dr,dc = 1,1  # vertical/horizontal increments
#     while True:  
#         yield M[r][c]                       # return values on path
#         br = r + dr not in range(len(M))    # bounce vertical
#         bc = c + dc not in range(len(M[0])) # bounce horizontal
#         if br and bc : break                # stop on double back
#         dr,dc = dr*(-1)**br, dc*(-1)**bc    # change directions as needed
#         r,c   = r+dr,  c+dc                 # next position
        
# matrix = [[1, 2, 4, 8],
#           [2, 4, 8, 16],
#           [4, 8, 16, 32]]
  
# print(sum(diagPath(matrix)))

# # # Get the values for N and M from the user on one line with space between them
N, M = map(int, input().split())

# initial position and directions
i, j = 0, 0
dir_v, dir_h = 1, 1

# adding the starting element of the path
path = [2 ** (i + j)]

while True:
    # if we can perform a step without going out of the matrix - doing it
    while i + dir_v < N and i + dir_v >= 0 and j + dir_h < M and j + dir_h >= 0:
        i += dir_v
        j += dir_h
        #print(i, j)
        path.append(2 ** (i + j))

    # finish conditions
    if (i, j) in [(0, 0), (N - 1, 0), (0, M - 1), (N - 1, M - 1)]:
        break

    # deciding which way to turn
    if j != M - 1 and j != 0:
        dir_v *= -1
    else:
        dir_h *= -1

    #print("directions:", dir_h, dir_v)

print(sum(path))

# good solution

# Dimitar
print('Hello world')
print('Hello Telerik')


# Donko
print("Zdraveyte, kolegi!")

#Todor
print("test")