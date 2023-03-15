# python3

def sift_down(data, i, swaps):
    
    
    left = 2 * i + 1
    right = 2 * i + 2

    
    min_index = i
    if left <= len(data) - 1 and data[left] < data[min_index]:
        min_index = left
    if right <= len(data) - 1 and data[right] < data[min_index]:
        min_index = right


    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        

        sift_down(data, min_index, swaps)


def build_heap(data):
    swaps = []
    

    for i in reversed(range(len(data) // 2)):
        sift_down(data, i, swaps)

    return swaps


def main():
    input_type = input("Enter input type (F for file, otherwise keyboard input): ")
    if input_type.lower() == 'f':
        input_filename = input("Enter input file name: ")
        with open(input_filename, 'r') as f:
            input_data = f.read().split('\n')
    else:
        input_data = [input(), input()]

    n = int(input_data[0])
    data = list(map(int, input_data[1].split()))
    assert len(data) == n

   
    swaps = build_heap(data)



    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
