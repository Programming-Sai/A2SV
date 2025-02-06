if __name__ == '__main__':
    N = int(input())
    _list = []
    for i in range(N):
        cmd = list(map(str, input().split()))
        if cmd[0] == 'insert':
            _list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(_list)
        elif cmd[0] == 'remove':
            _list.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            _list.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            _list.sort()
        elif cmd[0] == 'pop':
            _list.pop()
        elif cmd[0] == 'reverse':
            _list.reverse()

