
from py2neo import Graph, Subgraph
from py2neo import Node, Relationship, Path

test_graph = Graph("http://localhost:7474",auth=("neo4j","123456789"),name='neo4j')
test_graph.delete_all()

node_1 = Node('英雄',name = '张无忌')
node_2 = Node('英雄',name = '杨逍',武力值='100')
node_3 = Node('派别',name = '明教')

test_graph.create(node_1)
test_graph.create(node_2)
test_graph.create(node_3)
print(node_1)
print(node_1)

node_1_to_node_2 = Relationship(node_1,'教主',node_2)
node_3_to_node_1 = Relationship(node_1,'统领',node_3)
node_2_to_node_2 = Relationship(node_2,'师出',node_3)

test_graph.create(node_1_to_node_2)
test_graph.create(node_3_to_node_1)
test_graph.create(node_2_to_node_2)

from py2neo import Path
# 建一个路径：比如按照该路径查询，或者遍历的结果保存为路径
node_4,node_5,node_6 = Node(name='阿大'),Node(name='阿二'),Node(name='阿三')
path_1 = Path(node_4,'小弟',node_5,Relationship(node_6, "小弟", node_5),node_6)
test_graph.create(path_1)

print(path_1)