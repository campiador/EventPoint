#Event Extractor by Behnam Heydarshahi
#For tracing, we need to traverese through multiple threads, for that purpose, we have producer events in input
#which means we have to back-traverse.

from event import Event;
for i in range(1, 2):
    f = open('thread1', 'r')

    #line = f.readline()
    for line in f:
        e = Event(line);
        print (e)

        print (line)   #for line in f:
    #    print line
    f.close()

#NEEDSWORK
define findBarrier(thread1, thread2):
    for event1 in thread1
        if(event1.instanceOf(communication) && event1.getPthreadCallType == 5)
            for event2 in thread2
                if(event1.instanceOf(communication) && getPThreadCallType == 5)
                    if (event2.getSyncStruct() == event2.getSyncStruct())
                        #Barrierfound between th1 and th2