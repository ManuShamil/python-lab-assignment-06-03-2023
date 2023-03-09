# Question 4
# Write a python program that prints Pascal’s triangle


import sys

class PascalsTriangle:
    def __init__(self, n):
        self.n = n
        self.triangle = [[1]]
        self.generate()

    def generate(self):
        for i in range(1, self.n):
            curr = [1]
            j = 1
            prev = self.triangle[i - 1]
            while j < i:
                curr.append(prev[j - 1] + prev[j])
                j += 1
            curr.append(1)
            self.triangle.append(curr)

    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in row]) for row in self.triangle])


if __name__ == '__main__':
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    input_itr = iter(input_lines)

    n = int(next(input_itr))
    print(f"Enter the number of rows: {n}")

    triangle = PascalsTriangle(n)
    print( str(triangle) )