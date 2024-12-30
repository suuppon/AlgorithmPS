def swap(tree, index_1, index_2):
    tmp = index_2
    index_2 = index_1
    index_1 = tmp

def heapify(tree, root_index, tree_size):

    left_child_index = 2 * root_index
    right_child_index = 2 * root_index + 1

    largest = root_index

    if 0 < left_child_index < tree_size and tree[largest] < left_child_index:
        largest = left_child_index

    if 0 < right_child_index < tree_size and tree[largest] < right_child_index:
        largest = right_child_index

    if largest != root_index:
        swap(tree, root_index, largest)
        heapify(tree, largest, tree_size)

def heapsort(tree):
    tree_size = len(tree)
    for index in range(tree_size-1, 0, -1):
        heapify(tree, index, tree_size)
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)
    
    return tree

def main():
    arr = list()
    n = int(input())
    for _ in range(n):
        num = int(input())
        arr.append(num)
    
    return heapsort(arr)

if __name__ == "__main__":
    for item in main():
        print(item)