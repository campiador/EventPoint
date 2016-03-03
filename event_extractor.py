#Event Extractor by Behnam Heydarshahi
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
