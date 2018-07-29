def get_node(str):
    x, y = str.split(' ')
    return (int(x), int(y))


if __name__ == '__main__':
    nodes = []
    n = int(input())
    while n:
        # x = input()
        # print(x)
        # x, y = list(map(int, input().split()))
        nodes.append(get_node(input()))
        n -= 1
    nodes.sort(reverse=True)
    max_y = nodes[0][1]
    ans = []
    for i in range(len(nodes)):
        if nodes[i][1] >= max_y:
            ans.append(nodes[i])
            max_y = nodes[i][1]
    for i in range(len(ans)-1, -1, -1):
        print(ans[i][0], ans[i][1])