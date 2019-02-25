'''
堆疊(stack)是先進後出(FILO First In Last Out)的資料結構，意思是，先進去的資料最後出來。


佇列(queue)是先進先出(FIFO First In First Out)的資料結構，意思是，先進去的資料先出來。


[2,3,1,9,22,31,8,7,45,9]
'''
from ktool.kstack import kstack
from ktool.kqueue import kqueue

s = kstack()
s1 = kstack()
q = kqueue()
q1 = kqueue()

queue = (2,3,1,9,8,22,7,45,9)
stack =(2,3,1,9,8,22,7,45,9)


for i in range(len(queue)):
    if q.size() == 0:
        q.push(queue[i])
    else:
        if queue[i] >= q.back():
            q.push(queue[i])
        else:
            if queue[i] <= q.front():
                q1.push(queue[i])
                qsize = q.size()
                for i in range(qsize):
                    q1.push(queue[i])
                    q.pop()
                size = q1.size()
                for i in range(size):
                    q.push(q1.queue[i])
                for i in range(size):
                    q1.pop()
            else:
                for j in range(q.size()):
                    if queue[i] >= q.front():
                        q1.push(q.queue[0])
                        q.pop()
                q1.push(queue[i])
                for i in range(q.size()):
                    q1.push(q.queue[0])
                    q.pop()
                for i in range(q1.size()):
                    q.push(q1.queue[i])
                for i in range(q1.size()):
                    q1.pop()


print('q', q.queue)


for i in range(len(stack)):
    if s.size() == 0:
        s.push(stack[i])
    else:
        if stack[i] >= s.top():
            s.push(stack[i])
        else:
            size = s.size()
            for j in range(size):
                if stack[i] <= s.top():
                    s1.push(s.top())
                    s.pop()
            s.push(stack[i])
            size_temp = s1.size()
            for j in range(size_temp):
                s.push(s1.top())
                s1.pop()


print('s', s.stack)










