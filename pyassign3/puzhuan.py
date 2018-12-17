import copy
import turtle
m=int(input('墙的宽：'))
n=int(input('墙的高：'))
a=int(input('砖的宽：'))
b=int(input('砖的高：'))
wall=[]#定义一个墙
ans=[]#定义一个铺上的砖块序列
ans_sum=[]#定义一个所有铺法的列表
for i in range(m):
    for j in range(n):
        wall.append((i,j))#以所有的坐标构成要铺的墙
wall_1 = copy.deepcopy(wall)#将墙复制到另一面墙
ans_1=copy.deepcopy(ans)#将砖块序列复制到另一个列表
def check(q,x,y,a,b):
    '''检验在(x,y)可以横着铺一个长a 宽b 的砖块，如果可以输出True 不可以铺则输出False'''
    check_1=True
    if x+a>m or y+b>n:
        return False
    else:
        for i in range(x,x+a):
            for j in range(y,y+b):
                check_1=check_1 and (i,j)in q
        return check_1
def pz(wall_1,ans_1,ans_sum):
    '''铺砖块的递归函数'''
    wall_2 = copy.deepcopy(wall_1)#复制一个墙以便拆下砖块
    ans_2=copy.deepcopy(ans_1)#复制一个铺上的砖的列表以便恢复之前的状态
    if len(wall_1)==0:#如果墙上没有可以填的砖块则结束递归
        ans_sum.append(ans_1)
        return
    else:
        if check(wall_1,wall_1[0][0],wall_1[0][1],a,b)==True:#判断墙是否可以横着铺砖
            zt=()
            for i in range(wall_2[0][0],wall_2[0][0]+a):
                for j in range(wall_2[0][1],wall_2[0][1]+b):
                    wall_1.remove((i,j))
                    zt=zt+(i+j*m,)
            ans_1=ans_1+[zt]
            pz(wall_1, ans_1, ans_sum)
            wall_1=copy.deepcopy(wall_2) #恢复状态
            ans_1=copy.deepcopy(ans_2) #恢复状态
        if check(wall_1,wall_1[0][0],wall_1[0][1],b,a)==True and a!=b: #判断墙是否可以竖着铺砖
            zt=()
            for i in range(wall_2[0][0],wall_2[0][0]+b):
                for j in range(wall_2[0][1],wall_2[0][1]+a):
                    wall_1.remove((i,j))
                    zt=zt+(i+j*m,)
            ans_1=ans_1+[zt]
            pz(wall_1,ans_1,ans_sum)
            wall_1 = copy.deepcopy(wall_2) #恢复状态
            ans_1 = copy.deepcopy(ans_2) #恢复状态
def seeit(pf):
    '''选择一种铺法进行turtle的可视化'''
    Pen = turtle.Turtle()
    for i in pf:
        x1,y1,x2,y2=(i[0]%m) ,i[0]//m,(i[-1]%m)+1,i[-1]//m+1#根据砖块的号码找到它们的坐标
        Pen.up()
        Pen.goto(20*x1,20*y1)
        Pen.down()
        Pen.goto(20*x1,20*y2)
        Pen.goto(20*x2,20*y2)
        Pen.goto(20*x2,20*y1)
        Pen.goto(20*x1,20*y1)
    turtle.done()
def main():
    '''主函数'''
    pz(wall,ans_1,ans_sum)
    print('所有的铺法：',ans_sum)
    print('铺法数量：',len(ans_sum))
    if len(ans_sum)!=0:
        t=int(input('可视化铺法中的第_组：'))
        seeit(ans_sum[t-1])
    else:print('无法铺满')
if __name__ == '__main__':
    main()
