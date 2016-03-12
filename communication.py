from event import Event
class Communication(Event):

    def __init__(self, eventNumber, threadId, producer_thread, producer_event, address_range_start, address_range_end):
        Event.__init__(self, eventNumber, threadId)
        self.producer_thread = producer_thread
        self.producer_event = producer_event
        self.address_range_start = address_range_start
        self.address_range_end = address_range_end

    def getProducerThread(self):
        return self.producer_thread

    def getProducerEvent(self):
        return self.producer_event

    def getAddressRangeStart(self):
        return self.address_range_start

    def getAddressRangeEnd(self):
        return self.address_range_end
