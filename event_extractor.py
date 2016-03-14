#Event Extractor by Behnam Heydarshahi
#For tracing, we need to traverese through multiple threads, for that purpose, we have producer events in input
#which means we have to back-traverse.
#TODO: Parse flow navigation
#TODO: Read generic number of files, maybe from varargs, maybe calculate yourself
#TODO: Communications-->Edges in graph, do we wanna keep them? Because there
#  are already available in the nodes.
#TODO: Print out the content of the nodes

import networkx as nx;

from communication import Communication
from computation import Computation
from event import Event;
from synchronization import Synchronization

eventGraph=nx.Graph();


def main():

    for i in range(1, 2):
        f = open('thread2', 'r')

        count=0
        #line = f.readline()
        for line in f:
            e = Event(line, 0);
            # print (e)
            count+=1

            # print("line {}:".format(count))
            # print (line)   #for line in f:
            createEvent(line)

        #    print line
        f.close()

    print(eventGraph.nodes())

def createEvent(strEventLine):
    strEventLine=strEventLine.replace(",", " ")
    splittedEventArray=strEventLine.split(" ")
    # print(splittedEventArray)

    if (("$" in strEventLine) or ("*" in strEventLine)):
        print("COMPUTATION EVENT")
        eventGraph.add_node(Computation(splittedEventArray[0], splittedEventArray[1], splittedEventArray[2],
                                        splittedEventArray[3], splittedEventArray[4], splittedEventArray[5],
                                        splittedEventArray[6], splittedEventArray[7], splittedEventArray[8]))
    elif("^" in strEventLine):
        print ("SYNCHRONIZATION EVENT")
        eventGraph.add_node(Synchronization(splittedEventArray[0], splittedEventArray[1], splittedEventArray[3],
                                            splittedEventArray[5]))
    elif ("#" in strEventLine):
        print("COMMUNICATION EVENT")
        eventGraph.add_node(Communication(splittedEventArray[0], splittedEventArray[1], splittedEventArray[3],
                                          splittedEventArray[4], splittedEventArray[5], splittedEventArray[6]))
    else:
        print("Unknown event type in line")
        

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