# from iteration import for_loop
import iteration
import recursion
b=int(input("请输入一个整数："))
# 迭代
result1=iteration.for_loop(b)
result2=iteration.while_loop(b)
print("累计求和是：",result1,",",result2)
result3=iteration.nested__for_loop(b)
print("输出字符串：'\n'",result3)
# 递归
result4=recursion.recur(b)#普通递归
print("累计求和值：",result4)
result5=recursion.tail_recur(b,0)  #尾递归
print("累计求和值（尾递归）",result5)