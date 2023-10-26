def recur2iterion(n:int)->int:
    res=0
    stack=list()
    for i in range(n,-1,-1):
        stack.append(i)
    while stack:
        res+=stack.pop()
    return res