from collections import deque
class Digraph_algorithm():
    def __init__(self):
        self.graph={'start':{'a':2,'b':5},'a':{'b':8,'c':7},'b':{'d':4,'c':2},\
               'c':{'end':1},'d':{'c':6,'end':3}}
        self.lowest_cost = float('inf')  # 先设到达终点花费无穷大
        self.cost = {'a': 2, 'b': 5, 'end': float('inf')}  # 初始化cost和parent
        self.parents = {'a': 'start', 'b': 'start'}
        self.processed = []
    def find_lowest_node(self):
        lowest_cost_node = None
        lowest_cost=float('inf')
        for node in self.cost.keys():
            cost = self.cost[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost_node = node
        return lowest_cost_node

    def find_lowest_cost_path(self):
        node = self.find_lowest_node()
        while node is not None:  #当当前还有节点未处理
            cost= self.cost[node]
            neighbors=self.graph.get(node)
            for k in neighbors.keys():
                new_cost=cost+ neighbors.get(k)
                if (self.cost.get(k)==None) or self.cost.get(k) > new_cost:
                    self.cost[k] = new_cost
                    self.parents[k]=node
            self.processed.append(node)
            node=self.find_lowest_node()
            if node== 'end':
                break
        return self.cost.get('end')

ob=Digraph_algorithm()
print(ob.find_lowest_cost_path()) #8


