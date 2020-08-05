import math
num = 1000#在此输入您需要寻找的数字上限
front = str(num)+'以内的质数\n'
print("step 1")
lists2 = ''
lists1 = [1]*num
sqr = math.sqrt(num-1)
print("step 2")
n = 2
while n < sqr:
    x = 2
    while x*n < num-1:
        lists1[n*x] = 0
        x += 1
    n += 1	
    while lists1[n] != 1:
        n += 1
print("step 3")
for i in range(2,num-1):
    if lists1[i] == 1:
        lists2 += str(i)+'\n'
print('质数查找完毕')
print("txt导出中")
with open("质数.txt","w") as f:
        f.write(front)
        f.write(lists2)
        f.close()
print("txt导出完毕")