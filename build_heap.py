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
    # take input from the user
    input_type = input("Enter I for keyboard input, F for file input: ").strip()

    # input from keyboard
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

    # input from file
    elif input_type == "F":
        file_dir = input("Enter file name/path: ")
        with open(f"./tests/{file_dir}") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    else:
        print("Invalid input type")
        return

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made
    print(f"Number of swaps: {len(swaps)}")

    # output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()