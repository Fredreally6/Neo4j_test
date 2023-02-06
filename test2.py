import pandas as pd
from py2neo import Graph, Relationship, Node, NodeMatcher


graph = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'neo4j')
graph.delete_all()

data = pd.read_csv('data/data.csv')

entity1 = data.iloc[:,0]
type1 = data.iloc[:,1]
entity2 = data.iloc[:,2]
type2 = data.iloc[:,3]
rela = data.iloc[:,4]


label = ['entity1','type','entity2','type','relation']

# Method 1 -- Match the nodes. Merge them if they already exist, otherwise create new ones
node_matcher = NodeMatcher(graph)

node_treatment = Node(label[1], name = 'treatment')
node_test = Node(label[1], name = 'test')
node_problem = Node(label[1], name = 'problem')
graph.create(node_test)
graph.create(node_treatment)
graph.create(node_problem)

for i in range(0, data.shape[0]):

    if(graph.nodes.match(label[0], name=entity1[i]).count() == 0):
        node1 = Node(label[0], name = entity1[i])
        graph.create(node1)
    else:
        node1 = node_matcher.match(label[0]).where(name = entity1[i]).first()

    if(graph.nodes.match(label[2], name=entity2[i]).count() == 0):
        node3 = Node(label[2], name = entity2[i])
        graph.create(node3)
    else:
        node3 = node_matcher.match(label[2]).where(name = entity2[i]).first()

    node2 = node_matcher.match(label[1]).where(name=type1[i]).first()

    node4 = node_matcher.match(label[1]).where(name=type2[i]).first()

    relation1 = Relationship(node1,rela[i],node3)
    relation2 = Relationship(node1,'type',node2)
    relation3 = Relationship(node3,'type',node4)

    graph.create(relation1)
    graph.create(relation2)
    graph.create(relation3)

    
#Method 2 -- Create all nodes and merge the repeated nodes
# for i in range(0, data.shape[0]):

#     node1 = Node(label[0], name = entity1[i])
#     graph.create(node1)
#     node3 = Node(label[2], name = entity2[i])
#     graph.create(node3)

#     node2 = Node(label[1], name = type1[i])
#     graph.create(node2)
#     node4 = Node(label[1], name = type2[i])
#     graph.create(node4)

#     relation1 = Relationship(node1,rela[i],node3)
#     relation2 = Relationship(node1,'type',node2)
#     relation3 = Relationship(node3,'type',node4)

#     graph.create(relation1)
#     graph.create(relation2)
#     graph.create(relation3)

# graph.run('MATCH (n: type) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count>1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
# graph.run('MATCH (n: entity1) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count>1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
# graph.run('MATCH (n: entity2) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count>1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')

