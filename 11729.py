def Hanoi_Tower(n, start, end):
    if n == 1:
        return [start, end]
    
    List = []

    List.extend(Hanoi_Tower(n-1, 1, 2))
    List.extend((1, 3))
    List.extend(Hanoi_Tower(n-1, 2, 3))
    return List

print(Hanoi_Tower(3, 1, 3))