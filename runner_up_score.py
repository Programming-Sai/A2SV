if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    _max = max(arr)   
    while _max in arr:
        arr.remove(_max)
    print(max(arr))