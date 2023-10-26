def recur(n:int)-> int:
    # python的特点是喜欢用冒号
    if n==1:
        return 1
    res=recur(n-1)
    return n+res

# 递归函数的特点是会不断的深层次调用自己，这是“递”，递的过程会传入更小或更简化的参数，直到遇到终止条件
# 归是将每一递归层级的结果返回到上一层。向上归，向下递 res是层与层之间的过渡

def tail_recur(n:int,res:int)-> int:
    if n==0:
        return res
    return tail_recur(n-1,res+n)
# 尾递归：求和操作只在递的过程中进行，归的过程只需要层层返回
