from py2neo import Graph, Node, Relationship,NodeMatcher, RelationshipMatcher

graph = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'neo4j')

node_matcher = NodeMatcher(graph)
relation_matcher = RelationshipMatcher(graph)

def Onetable(a, b):
    # Match two nodes in entity1
    nodeA = node_matcher.match("entity1").where(name = a).first()
    nodeB = node_matcher.match("entity1").where(name = b).first()

    # Get two lists of triples with the two nodes
    results_A = graph.match((nodeA,))
    results_B = graph.match((nodeB,))
    result_list_A=[]
    result_list_B=[]

    for r in results_A:
        start_node = r.start_node['name']
        end_node = r.end_node['name']
        rela_type = type(r).__name__
        result_list_A.append((start_node, rela_type, end_node))
    # print(result_list_A)

    for r in results_B:
        start_node = r.start_node['name']
        end_node = r.end_node['name']
        rela_type = type(r).__name__
        result_list_B.append((start_node, rela_type, end_node))
    # print(result_list_B)

    # Compare with two lists to find the relations
    abssame_count = 0
    pair_result = []
    for i in result_list_A:
        for j in result_list_B:
            if i[1]==j[1]:
                if i[2]==j[2]:
                    abssame_count += 1
                else:
                    pair_result.append((i[2], j[2]))
                
    print(abssame_count)
    print(pair_result)


Onetable("A", "B")