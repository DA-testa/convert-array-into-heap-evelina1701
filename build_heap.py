# python3
# Evelīna Geikina 221RDB068

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    size=len(data)
    ##

    for k in range(size//2,-1,-1):
        small = k #tiek inicializēta mazākā sakne
        while True:
            l_node = 2*k+1 #kreisais node
            r_node = 2*k+2 #labais node
            
            if l_node<=size-1: #tiek pārbaudīts, vai eksistē kreisais node
                if data[l_node]<data[small]: #ja kreisais node eksistē, tad tas tiek salīdzināts ar sakni
                    small = l_node #ja kreisais node ir mazāks par sakni, tad kā mazāko sakni inicializē kreiso node
            if r_node<=size-1: #tiek pārbaudīts, vai eksistē labais node
                if data[r_node]<data[small]: #ja labais node eksistē, tad tas tiek salīdzināts ar sakni
                    small = r_node #ja labais node ir mazāks par sakni, tad kā mazāko sakni inicializē labo node
            if k != small: #tiek nomainīta sakne, ja node ir mazāks par iepriekšējo sakni
                swaps.append((k,small)) #tiek saglabāti node indeksi, kuri tika apmainīti vietām
                (data[k],data[small])=(data[small],data[k])
                k = small #inicializē jaunu mazāko sakni
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
        with open("./tests/"+fileName, mode="r") as file:
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
