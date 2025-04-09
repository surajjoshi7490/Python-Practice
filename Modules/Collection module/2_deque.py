from collections import deque
def using_deque(lists):
    new=deque(lists)
    new.appendleft(0)
    new.append(9)
    return new
results=using_deque([3,4,5,6,7,8])
print(results)