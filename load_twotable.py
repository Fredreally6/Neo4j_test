import pandas as pd
from py2neo import Graph, Node, Relationship,NodeMatcher

graphA = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'test')
graphB = Graph("http://localhost:7473", name = 'testb')

graphA.delete_all()
graphB.delete_all()

data = pd.read_csv('data/data1.csv')

entity1 = data.iloc[:,0]
rela = data.iloc[:,1]
entity2 = data.iloc[:,2]

label = [] 
for i in range(0,data.shape[1]):
    label.append(data.columns[i])


for i in range(0, data.shape[0]):
    if entity1[i]=='A':
        graph_new = graphA
    else:
        graph_new = graphB

    node_matcher = NodeMatcher(graph_new)

    if(graph_new.nodes.match(label[0], name=entity1[i]).count() == 0):
        node1 = Node(label[0], name = entity1[i])
        graph_new.create(node1)
    else:
        node1 = node_matcher.match(label[0]).where(name = entity1[i]).first()

    if(graph_new.nodes.match(label[2], name=entity2[i]).count() == 0):
        node2 = Node(label[2], name = entity2[i])
        graph_new.create(node2)
    else:
        node2 = node_matcher.match(label[2]).where(name = entity2[i]).first()
    
    relation1 = Relationship(node1,rela[i],node2)
    
    graph_new.create(relation1)