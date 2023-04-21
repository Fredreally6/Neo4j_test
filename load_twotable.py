import pandas as pd
from py2neo import Graph, Node, Relationship,NodeMatcher

graphA = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'test')
graphB = Graph("http://localhost:7475", name = 'testb')

graphA.delete_all()
graphB.delete_all()

dataA = pd.read_csv('data/dataA.csv')
dataB = pd.read_csv('data/dataB.csv')

entity1_A = dataA.iloc[:,0]
rela_A = dataA.iloc[:,1]
entity2_A = dataA.iloc[:,2]

entity1_B = dataB.iloc[:,0]
rela_B = dataB.iloc[:,1]
entity2_B = dataB.iloc[:,2]

label = [] 
for i in range(0,dataA.shape[1]):
    label.append(dataA.columns[i])

node_matcher_A = NodeMatcher(graphA)
node_matcher_B = NodeMatcher(graphB)

nodeA = Node(label[0], name = 'A')
nodeB = Node(label[0], name = 'B')

graphA.create(nodeA)
graphB.create(nodeB)

for i in range(0, dataA.shape[0]):

    if(entity1_A[i]=='A'):
        node1 = node_matcher_A.match(label[0]).where(name = 'A').first()
    elif(graphA.nodes.match(label[2], name=entity1_A[i]).count() != 0):
        node1 = node_matcher_A.match(label[2]).where(name = entity1_A[i]).first()
    else:
        node1 = Node(label[0], name = entity1_A[i])
        graphA.create(node1)
    
    if(graphA.nodes.match(label[2], name=entity2_A[i]).count() == 0):
        node2 = Node(label[2], name = entity2_A[i])
        graphA.create(node2)
    else:
        node2 = node_matcher_A.match(label[2]).where(name = entity2_A[i]).first()
    
    relation1 = Relationship(node1,rela_A[i],node2)
    
    graphA.create(relation1)

for i in range(0, dataB.shape[0]):

    if(entity1_B[i]=='B'):
        node1 = node_matcher_B.match(label[0]).where(name = 'B').first()
    elif(graphB.nodes.match(label[2], name=entity1_B[i]).count() != 0):
        node1 = node_matcher_B.match(label[2]).where(name = entity1_B[i]).first()
    else:
        node1 = Node(label[0], name = entity1_B[i])
        graphB.create(node1)
    
    if(graphB.nodes.match(label[2], name=entity2_B[i]).count() == 0):
        node2 = Node(label[2], name = entity2_B[i])
        graphB.create(node2)
    else:
        node2 = node_matcher_B.match(label[2]).where(name = entity2_B[i]).first()
    
    relation1 = Relationship(node1,rela_B[i],node2)
    
    graphB.create(relation1)