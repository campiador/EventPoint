#Event Extractor by Behnam Heydarshahi
#For tracing, we need to traverese through multiple threads, for that purpose,
#  we have producer events in input which means we have to back-traverse.
#TODO: Parse flow navigation
#TODO: Read generic number of files, maybe from varargs, maybe calculate yourself
#TODO: Communications-->Edges in graph, do we wanna keep them? Because there
#  are already available in the nodes.
#TODO: Print out the content of the nodes
#Question: Do we need edges among computation events as well?

import networkx as nx;

from communication import Communication
from computation import Computation
from event import Event;
from synchronization import Synchronization

THREAD_COUNT=2

eventGraph=nx.Graph();

def main():
    parse_threads()#saves results in eventGraph
    print("finished parsing")
    # print(eventGraph.nodes())
    # eventGraph.nodes()
    # print(eventGraph.size())
    # print(eventGraph.nodes().__getitem__(1))
    e=Event(1, -1)
    e.eventId='1 - 500'

    e2=Event(1,-1)
    e2.eventId='1 - 1'

    print(eventGraph.number_of_nodes())

    eventGraph.add_edge(e2, e)

    # e = eventGraph.__getitem__(e)
    print(eventGraph.number_of_nodes())
    # eventGraph.remove_node(e)
    print(eventGraph.number_of_nodes())
    # print(eventGraph.nodes().__getitem__(1))
    # eventGraph.add_edge(1,2)
    print(eventGraph.edges())

    # print("number of nodes is {}".format(eventGraph.number_of_nodes()))


def parse_threads():
    for i in range(1, THREAD_COUNT+1):
        f = open('thread%d' % i, 'r')
        print ("openning file %d " % i)
        count=0
        #line = f.readline()
        for line in f:
            # e = Event(line, 0);
            # print (e)
            count+=1
            # print("line {}:".format(count))
            # print (line)   #for line in f:
            createEvent(line)
        #    print line
        f.close()


def createEvent(strEventLine):
    strEventLine=strEventLine.replace(",", " ")
    splittedEventArray=strEventLine.split(" ")
    # print(splittedEventArray)

    if (("$" in strEventLine) or ("*" in strEventLine)):
        print("COMPUTATION EVENT")
        tempCompEv=Computation(splittedEventArray[0], splittedEventArray[1], splittedEventArray[2],
                                        splittedEventArray[3], splittedEventArray[4], splittedEventArray[5],
                                        splittedEventArray[6], splittedEventArray[7], splittedEventArray[8])
        # print(tempCompEv)
        eventGraph.add_node(tempCompEv)
    elif("^" in strEventLine):
        print ("SYNCHRONIZATION EVENT")
        eventGraph.add_node(Synchronization(splittedEventArray[0], splittedEventArray[1], splittedEventArray[3],
                                            splittedEventArray[5]))
    elif ("#" in strEventLine) :
        print("COMMUNICATION EVENT")
        eventGraph.add_node(Communication(splittedEventArray[0], splittedEventArray[1], splittedEventArray[3],
                                          splittedEventArray[4], splittedEventArray[5], splittedEventArray[6]))
    else:
        # FIXME: Separate no-address comps from truly unkown cases.
        print("Unknown event type in line, probably communication with no address")

def subGraphOf(nodes):

    return  eventGraph.subgraph(nodes)


main()


#
# #NEEDSWORK
# define findBarrier(thread1, thread2):
#     for event1 in thread1
#         if(event1.instanceOf(communication) && event1.getPthreadCallType == 5)
#             for event2 in thread2
#                 if(event1.instanceOf(communication) && getPThreadCallType == 5)
#                     if (event2.getSyncStruct() == event2.getSyncStruct())
#                         #Barrierfound between th1 and th2

# TODO: Implement this code
# define addCommunicationEdges():
#     foreach node in eventGraph
#         if node is computation
#             add one edge from producer to this node

# TODO: Graph isomorphism
#
# is_isomorphic(G1, G2[, node_match, edge_match])	Returns True if the graphs G1 and G2 are isomorphic and False otherwise.
# could_be_isomorphic(G1, G2)	Returns False if graphs are definitely not isomorphic.
# fast_could_be_isomorphic(G1, G2)	Returns False if graphs are definitely not isomorphic.
# faster_could_be_isomorphic(G1, G2)	Returns False if graphs are definitely not isomorphic.
# https://networkx.github.io/documentation/latest/reference/algorithms.isomorphism.html