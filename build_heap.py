# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    size=len(data)
    left_node = 2*i+1
    right_node = 2*i+2

    for i in range(n//2,-1,-1):
        smallest = i
        if left_node<size and data[left_node]<data[smallest]:
            smallest = left_node
        if right_node<size and data[right_node]<data[smallest]:
            smallest = right_node
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
    letter = input()
    if "F" in letter:
        fileName = input()
        if "a" in fileName:
            return
        with open(f"./test/{fileName}", mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split())) 
    if "I" in letter:
        n = int(input())
        data = list(map(int, input().split())) 

    # input from keyboard
    

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
