a, b, c, d, e, f = map(int, input().split())

x = (c*e - b*f)/(a*e - b*d)
y = (-c*d + a*f)/(a*e - b*d)

print(int(x), int(y))