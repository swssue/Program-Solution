from collections import deque
def solution(queue1, queue2):
    answer = 0
    temp1 = deque(queue1)
    temp2 = deque(queue2)
    total_len = len(temp1) + len(temp2)
    
    x = sum(queue1)
    y = sum(queue2)

    while x != y:
        if 2*(total_len) < answer:
            return -1
        
        
        
        if x < y:
            a = temp2.popleft()
            temp1.append(a)
            x +=a
            y -=a 
            answer+=1
        else:
            b = temp1.popleft()
            temp2.append(b)
            x -= b
            y += b
            answer+=1

    return answer