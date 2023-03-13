list1=[[]]
    for i in range(len(lists)+1):
        for j in range(i):
            list1.append(lists[j:i])
    return list1
        