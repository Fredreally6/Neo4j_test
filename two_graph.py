from py2neo import Graph, Node, Relationship,NodeMatcher, RelationshipMatcher

graphA = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'test')
graphB = Graph("http://localhost:7473", name = 'testb')


def TwoGraph(a, b):

    # Match two nodes in entity1
    nodeA = NodeMatcher(graphA).match("entity1").where(name = a).first()
    nodeB = NodeMatcher(graphB).match("entity1").where(name = b).first()

    # Get two lists of triples with the two nodes
    results_A = graphA.match((nodeA,))
    results_B = graphB.match((nodeB,))
    result_list_A=[]
    result_list_B=[]

    for ra in results_A:
        start_node = ra.start_node['name']
        end_node = ra.end_node['name']
        rela_type = type(ra).__name__
        result_list_A.append((start_node, rela_type, end_node))
    # print(result_list_A)

    for rb in results_B:
        start_node = rb.start_node['name']
        end_node = rb.end_node['name']
        rela_type = type(rb).__name__
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


TwoGraph("A", "B")
