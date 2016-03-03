from event import Event
class Communication(Event):

    def __init__(self, number, producer_thread, producer_event, address_range):
        Event.__init__(self, number)
        self.producer_thread = producer_thread
        self.producer_event = producer_event
        self.address_range = address_range

    def getProducerThread(self):
        return self.producer_thread

    def getProducerEvent(self):
        return self.producer_event

    def getAddressRange(self):
        return self.address_range