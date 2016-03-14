# TODO: make object hashable, then print graph
#TODO: Graph edges

class Event(object):

    def __init__(self, eventNumber, threadId):
        self.eventNumber = eventNumber
        self.threadId = threadId
        self.eventId='%s - %s' %(threadId, eventNumber)

    def getEventNumber(self):
        return self.eventNumber

    def getThreadId(self):
        return self.threadId

    def getEventId(self):
        return self.eventId

    def __str__(self):
        return "Event id is %s" % (self.getEventId())

# Making events hashable for graph
    def __key(self):
        return (self.eventId)

    def __eq__(x, y):
        return x.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())