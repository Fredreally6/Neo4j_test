from py2neo import Graph, NodeMatcher

graphA = Graph("http://localhost:7474", auth = ('neo4j','password'), name = 'test')
graphB = Graph("http://localhost:7475", name = 'testb')

alpha = [1, 0.8, 0.5, 0.1]

def TwoGraph(a, b, level):
    
    # Match two nodes
    if(a == 'A'):
        nodeA = NodeMatcher(graphA).match("entity1").where(name = 'A').first()
    else:
        nodeA = NodeMatcher(graphA).match("entity2").where(name = a).first()

    if(b == 'B'):
        nodeB = NodeMatcher(graphB).match("entity1").where(name = 'B').first()
    else:
        nodeB = NodeMatcher(graphB).match("entity2").where(name = b).first()


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
                
    print("*****************************")
    print("Comparing "+a+" and "+b+" on level "+str(level))  
    print("Number of Absolutely Same Relation: "+str(abssame_count))
    print(pair_result)
    print(" ")

    length = max(len(result_list_A),len(result_list_B))

    if len(pair_result)==0 or level >= 3:
        if length == 0: 
            return 0
        else: 
            return abssame_count/length
        
    tmp = 0
    for it in pair_result:
        tmp += TwoGraph(it[0], it[1], level+1)

    similarity = (abssame_count + alpha[level+1]*tmp)/length

    # print(similarity)
    return similarity


sim = TwoGraph("A", "B", 0)
print("The similarity between A and B is %.3f" %sim)
