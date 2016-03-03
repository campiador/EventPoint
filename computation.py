from event import Event
class Computation(Event):

    def __init__(self, number, integer_op_count, fp_op_count, memory_read_count, memory_write_count,
                 unique_address_written, unique_address_read):
        Event.__init__(self, number)
        self.integer_op_count = integer_op_count
        self.fp_op_count = fp_op_count
        self.memory_read_count = memory_read_count
        self.memory_write_count = memory_write_count

        self.unique_address_written = unique_address_written
        self.unique_address_read = unique_address_read

    def getIntOpCount(self):
        return self.integer_op_count

    def getFpOpCount(self):
        return self.fp_op_count

    def getMemReadCount(self):
        return self.memory_read_count

    def getMemWriteCount(self):
        return self.memory_write_count

    def getUniqueAdWritten(self):
        return self.unique_address_written

    def getUniqueAdRead(self):
        return self.unique_address_read
    