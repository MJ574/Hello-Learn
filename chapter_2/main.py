# from iteration import for_loop
import iteration
import recursion
from recur2iter import recur2iterion 
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
# 递归树，递归的要素是要有终止条件和每层的递归公式
result6=recursion.fib(b)
print("斐波那契数列的第n个值是:",result6)
# 递归和迭代的转换
result7=recur2iterion(b)
print("输出转换结果：",result7)
