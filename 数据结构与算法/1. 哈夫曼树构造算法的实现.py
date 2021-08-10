"""
给一个列表，里面每个元素代表权重，要求输出一个列表，列表里面每个元素是，一个节点
"""


class HTNode(object):
    """author : kerwin"""
    def __init__(self, val):
        self.data = val
        self.parent = 0
        self.lch = 0
        self.rch = 0

    def __call__(self, *args, **kwargs):
        return [self.data, self.parent, self.lch, self.rch]


def find_min_value_and_index(res, i):
    index1, index2 = 0, 0
    item1, item2 = None, None
    min_1, min_2 = 10**10, 10**10
    for index, item in enumerate(res):
        if index == 0:
            continue
        if index < i and item.parent == 0:
            if item.data < min_1:
                item2 = item1
                min_2 = min_1
                index2 = index1
                item1 = item
                min_1 = item.data
                index1 = index
            elif item.data < min_2:
                item2 = item
                min_2 = item.data
                index2 = index
    return item1, item2, index1, index2


def create_ht_tree(input_list):
    n = len(input_list)
    res = [HTNode(0) for _ in range(2*n)]
    for index, val in enumerate(input_list):
        res[index+1].data = val
    for i in range(n+1, 2*n):
        temp1, temp2, index1, index2 = find_min_value_and_index(res, i)
        temp1.parent, temp2.parent = i, i
        res[i].data = temp1.data + temp2.data
        res[i].lch, res[i].rch = index1, index2
    for i in res:
        print(i())


create_ht_tree([5, 29, 7, 8, 14, 23, 3, 11])
