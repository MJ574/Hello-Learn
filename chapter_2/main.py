# from iteration import for_loop
import iteration
b=int(input("请输入一个整数："))
result=iteration.for_loop(b)
result1=iteration.while_loop(b)
print("累计求和是：",result,",",result1)
result3=iteration.nested__for_loop(b)
print("输出字符串：'\n'",result3)
