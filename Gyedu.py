from collections import deque

patient_name = input("Enter patient name:    ")
condition = input("Enter condition of patient:    ")
risk = input("Enter risk level(low, mid, high):    ")

patient2_name = input("Enter patient name:    ")
condition2 = input("Enter condition of patient:    ")
risk = input("Enter risk level(low, mid, high):    ")

patient_name3 = input("Enter patient name:    ")
condition3 = input("Enter condition of patient:    ")
risk = input("Enter risk level(low, mid, high):    ")

if risk == "high":
    from collections import deque
    queue = deque()
    queue.append("1." + patient_name)
    queue.append("2." + patient2_name)
    print(queue)
    rear_item=queue[-1]
    print("rear_item:", rear_item)
    print("front_item:", queue[0])
#queue.popleft()  # returns "A
