def for_loop(n:int) -> int:
    # for 循环
    res=0
    for i in range(1,n+1):
        #range()是左闭右开的
        res+=i
    return res   
    
def while_loop(n:int) ->int:
    res1=0
    i=0
    while i<=n:
        res1+=i
        i=i+1
    return res1        
        
def nested__for_loop(n:int) -> str:
    res=""