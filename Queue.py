from collections import deque
queue = deque()
queue.append("A")
queue.append("B")
#queue.popleft()  # returns "A"
print(queue)
rear_item=queue[-1]
print("rear_item:", rear_item)
print("front_item:", queue[0])