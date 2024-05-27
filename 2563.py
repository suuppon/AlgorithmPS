def update_paper_with_dots(dots, paper):
    for dot in dots:
        x, y = dot[0]-1, dot[1]-1  # Adjusting index to 0-based
        for i in range(10):
            for j in range(10):
                if x+i <100 and y+j <100:
                    paper[x+i][y+j] = 1


def calculate_total_marked(paper):
    """Calculates the total marked cells."""
    return sum(sum(row) for row in paper)

def main():
    n = int(input())
    dots = []
    for _ in range(n):
        point = list(map(int, input().split()))
        dots.append(point)
    
    paper = [[0 for _ in range(100)] for _ in range(100)]
    update_paper_with_dots(dots, paper)
    total_marked = calculate_total_marked(paper)
    print(total_marked)

if __name__ == "__main__":
    main()
