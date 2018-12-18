"""tile.py: to fill a wall with bricks

__author__ = "向亦凡"
__pkuid__  = "1800011820"
__email__  = "1800011820@pku.edu.cn"

"""

m = int(input('请输入墙的长度：'))
n = int(input('请输入墙的高度：'))
a = int(input('请输入瓷砖的长度：'))
b = int(input('请输入瓷砖的宽度：'))

qiang = [[0 for i in range(m)]for i in range(n)]
all_ans = []
ans = []
num = 0


def input_test(m,n,a,b):
    
    #初步判断能否铺砖
    
    if (m*n)%(a*b) == 0 :
        return True
    else :
        print('Error：没有合适的铺法')
        assert False


def findblocks():
    #找没有铺砖的空位,i(n) 是第几行，j(m) 是该行中从左往右的第几个；a 是砖的宽，b 是砖的高
    #返回 （i，j）
    
    i = 0
    for i_1 in qiang:
        i += 1
        j = 0
        for j_1 in i_1:
            j += 1
            if (i==n and j==m) and (j_1 == 1):
                return False
            elif j_1 == 0:
                return i,j


def test_puzhuan_lr(i,j,a,b):
    #判断能否横着铺
    if i+b-1 > n or j+a-1 > m:
        return False
    i_1 = i-1
    for i_2 in qiang[i-1:i+b-1] :
        for j_1 in range(j-1,j+a-1):
            if qiang[i_1][j_1] == 0:
                pass
            else:
                return False
        i_1 += 1
    return True

    
def test_puzhuan_ud(i,j,a,b):
    #判断能否竖着铺
    if i+a-1 > n or j+b-1 > m:
        return False
    i_1 = i-1
    for i_2 in qiang[i-1:i+a-1] :
        for j_1 in range(j-1,j+b-1):
            if qiang[i_1][j_1] == 0:
                pass
            else:
                return False
        i_1 += 1
    return True
        
'''********************************************下面是函数正文**************************************************'''     

def tile(m,n,a,b):
    global num,all_ans
    
    #判断是否应该结束递归
    if findblocks() != False:
        i = findblocks()[0]
        j = findblocks()[1]
        
    else :
        all_ans.append(ans.copy()) 
        num += 1
        return True

    
    #横着铺
    if test_puzhuan_lr(i,j,a,b):
        
        #把砖铺上,记录这一块砖的信息
        i_3 = i-1
        blocks = []
        for i_2 in qiang[i-1:i+b-1]:
            for j_2 in range(j-1,j+a-1):
                ablock = [i_3+1,j_2+1]
                qiang[i_3][j_2] = 1
                blocks.append(ablock)
            i_3 += 1
        
        #加入答案
        ans.append(blocks)

        
        #递归
        tile(m,n,a,b)
        
        #拆砖
        i_3 = i-1
        for i_2 in qiang[i-1:i+b-1]:
            for j_2 in range(j-1,j+a-1):
                qiang[i_3][j_2] = 0
            i_3 += 1
        
        #去掉答案
        ans.pop()
        
    else:
        pass
    
    
    #竖着铺
    if test_puzhuan_ud(i,j,a,b):
        
        #把砖铺上,记录这一块砖的信息
        i_3 = i-1
        blocks = []
        for i_2 in qiang[i-1:i+a-1]:
            for j_2 in range(j-1,j+b-1):
                ablock = [i_3+1,j_2+1]
                qiang[i_3][j_2] = 1
                blocks.append(ablock)
            i_3 += 1
        
        #加入总答案
        ans.append(blocks)
        
        #递归
        tile(m,n,a,b)
        
        #拆砖
        i_3 = i-1
        for i_2 in qiang[i-1:i+a-1]:
            for j_2 in range(j-1,j+b-1):
                qiang[i_3][j_2] = 0
            i_3 += 1
        
        #去掉答案
        ans.pop()
        
        
    else:
        pass

    return num

'''********************************************以上是函数正文**************************************************'''     


def standardization(k):
    #抱歉老师和助教，我一开始没有看到输出格式要求，使用坐标输出。故用这个函数将坐标转化为方块的编号
    standard_answer = []
    for i in k:
        order = []
        for j in i:
            seq = j[1]-1+(j[0]-1)*m
            order += [seq]
        standard_answer.append(order.copy()) 
    return standard_answer

def drawbricks(key):
        import turtle
        aturtle = turtle.Turtle()
        aturtle.hideturtle()
        aturtle.penup()
        aturtle.speed(0)
        aturtle.pensize(2)
        #将坐标抽象成矩形的对角线的端点
        for i in key:
            x1,y1,x2,y2 = n,m,0,0
            for j in i:
                if j[0] < x1:
                    x1 = j[0]
                if j[1] < y1:
                    y1 = j[1]

                if j[0] > x2:
                    x2 = j[0]
                if j[1] > y2:
                    y2 = j[1]

            aturtle.setposition(-20*m+40*(y1-1),20*n-40*(x1-1))
            aturtle.color('black','yellow')
            aturtle.pendown()
            aturtle.begin_fill()
            aturtle.goto(-20*m+40*(y2),20*n-40*(x1-1))
            aturtle.goto(-20*m+40*(y2),20*n-40*(x2))
            aturtle.goto(-20*m+40*(y1-1),20*n-40*(x2))
            aturtle.goto(-20*m+40*(y1-1),20*n-40*(x1-1))
            aturtle.end_fill()
            aturtle.penup()


def draw(choose,all_ans):
    #作图
    
    import turtle
    aturtle = turtle.Turtle()
    aturtle.hideturtle()
    aturtle.speed(0)
    aturtle.pensize(0.5)
    
    #画格子
    aturtle.penup()
    for u in range(1,n+2):
        aturtle.setposition(-20*m,20*n-40*(u-1))
        aturtle.pendown()
        aturtle.fd(40*m)
        aturtle.penup()
    
    aturtle.rt(90)
    for h in range(1,m+2):
        aturtle.setposition(-20*m+40*(h-1),20*n)
        aturtle.pendown()
        aturtle.fd(40*n)
        aturtle.penup()
    
    #画砖
    aturtle.pensize(2)
    aturtle.penup()

    drawbricks(choose)
        
        
def main():
    input_test(m,n,a,b)
    
    global all_ans
    
    if a != b:
        tile(m,n,a,b)
        print('所有铺法如下：')
        for i in all_ans:
            print('*',standardization(i))
        print('共计%d种铺法'%num)

        seq = int(input('请在1~%d种铺法中选择一种进行可视化：'%num))
        choose = all_ans[seq-1]

        draw(choose,all_ans)
    
    else :
        #判断特殊情况：当长和宽相等时的情况
        judge = input('是否输出该种方法？（输入Y或N）')
        if judge == 'Y':
            all_ans = [[[i,j]] for i in range(1,n+1) for j in range(1,m+1)]
            draw(all_ans,all_ans)
        
    
if __name__ == '__main__':
    main()


