# python3


def build_heap(data):
    swaps = []
    smallest = i
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    size=len(data)
    left = 2*i+1
    right = 2*i+2

    for i in range(n//2,-1,-1):
        if left<size and data[left]<data[smallest]:
            smallest = left
        if right<size and data[right]<data[smallest]:
            smallest = right
        if i != smallest:
            swaps.append((i,smallest))
            (data[i],data[smallest])=(data[smallest],data[i])
            i = smallest
        else:
            break
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
