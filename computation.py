from event import Event
class Computation(Event):

    def __init__(self, eventNumber, threadId, integer_op_count, fp_op_count, memory_read_count, memory_write_count, writeRead,
                 unique_address_start, unique_address_end):
        Event.__init__(self, eventNumber, threadId)

        self.integer_op_count=integer_op_count
        self.fp_op_count = fp_op_count
        self.memory_read_count = memory_read_count
        self.memory_write_count = memory_write_count

        self.isWrite = (writeRead == "$")
        self.unique_address_start = unique_address_start
        self.unique_address_end = unique_address_end

    def getIntOpCount(self):
        return self.integer_op_count

    def getFpOpCount(self):
        return self.fp_op_count

    def getMemReadCount(self):
        return self.memory_read_count

    def getMemWriteCount(self):
        return self.memory_write_count

    def getUniqueAdStart(self):
        return self.unique_address_start

    def getUniqueAdEnd(self):
        return self.unique_address_end

    def isWriteEvent(self):
        return self.isWrite