import pandas as pd
from py2neo import Graph, Node, Relationship

test_graph = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'neo4j')

# tn1 = Node("Person", name = "Sam")
# tn2 = Node("Person", name = "Jack")
# relation1 = Relationship(tn1,"firend",tn2)
test_graph.delete_all()

data = pd.read_csv('data/data.csv')

x = data.head(0)
y = data.columns[0]
z = data.columns
person = data.iloc[:,0]
city = data.iloc[:,1]
job = data.iloc[:,2]

label = []
for i in range(0,data.shape[1]):
    label.append(data.columns[i])
print(label)

for i in range(0, 3):
    # print(person[i] + " locates " + city[i] + " and works as " + job[i])
    node1 = Node(label[0], name = data.iloc[:,0][i])
    # if(test_graph.nodes.match('Person',name = data.iloc[:,0][i]).count() == 0):
    test_graph.create(node1)

    node2 = Node(label[1], name = data.iloc[:,1][i])
    # if(test_graph.nodes.match('City',name = data.iloc[:,1][i]).count() == 0):
    test_graph.create(node2)

    node3 = Node(label[2], name = data.iloc[:,2][i])
    # if(test_graph.nodes.match('Job',name = data.iloc[:,2][i]).count() == 0):
    test_graph.create(node3)
    
    relation1 = Relationship(node1,'locates in',node2)
    relation2 = Relationship(node1,'works as', node3)
    
    test_graph.create(relation1)
    test_graph.create(relation2)

test_graph.run('MATCH (n: City) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count>1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
test_graph.run('MATCH (n: Job) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count>1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')

# test_graph.delete_all()