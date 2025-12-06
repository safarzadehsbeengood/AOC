from aocd import get_data
import math

test = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

data_source = test
data_source = get_data(day=6, year=2025)

data = [line.split() for line in data_source.splitlines()]

# pt 1
nums = [list(map(int, line)) for line in data if line[0].isnumeric()]
ops = data[len(nums)]

transposed = [list(row) for row in zip(*nums)]

res = 0

for problem, op in zip(transposed, ops):
    if op == "+":
        res += sum(problem)
    elif op == "*":
        res += math.prod(problem)

print(res)

# pt 2
mat = data_source.splitlines()[:len(nums)]
row_width = len(mat[0])
col_height = len(nums)

def get_col_number(grid, j):
    num = ''
    for i in range(col_height):
        num += grid[i][j]
    if num.strip() == '': return -1
    return int(num.strip())

def do_problem(problem, op):
    # print(op.join(map(str, problem)), end=" -> ")
    if op == "+":
        return sum(problem)
    elif op == "*":
        return math.prod(problem)

op_idx = len(ops)-1
problem = []
res = 0
for j in range(row_width-1, -1, -1):
    # print("getting", j, end=": ")
    num = get_col_number(mat, j)
    # print(num)
    op = ops[op_idx]
    if num >= 0:
        problem.append(num)
    if num < 0 or j == 0:
        res += do_problem(problem, op)
        op_idx -= 1
        problem = []
        continue

print(res) 
        
