x = int(input())
y = int(input())
z = int(input())
n = int(input())
    



a, b, c, n = [int(raw_input()) for _ in x range(n)]
print ( [ [x,y,z] for x in x range(a + 1) for y in x range(b + 1) for z in x range(c + 1) if x + y + z != n])