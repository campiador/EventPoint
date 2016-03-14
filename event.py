# TODO: make object hashable, then print graph
#TODO: Graph edges
#TODO: Read generic number of files, maybe from varargs, maybe calculate yourself

class Event(object):

    def __init__(self, eventNumber, threadId):
        self.eventNumber = eventNumber
        self.threadId = threadId

    def getEventNumber(self):
        return self.eventNumber

    def getThreadId(self):
        return self.threadId

    def __str__(self):
        return "Event number is %s" % (self.eventNumber)