class Event(object):

    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def __str__(self):
        return "Event number is %s" % (self.number)