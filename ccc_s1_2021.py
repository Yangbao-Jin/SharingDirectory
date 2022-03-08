n = int(input())
area = 0

h = input().split()
w = input().split()

for i in range(n):
    print(i)
    area += (int(h[i]) + int(h[i + 1]))/2 * int(w[i])
print(area)