class SimpleCounter:
    count = 0

    def increase(self):
        SimpleCounter.count = SimpleCounter.count + 1

    @classmethod
    def print_count(cls):
        print("Count = " + str(SimpleCounter.count))


c1 = SimpleCounter()
c1.increase()
c2 = SimpleCounter()
c2.increase()
SimpleCounter.print_count()
