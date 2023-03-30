class BaseClass:
    def callMe(self):
        print("Calling method on Base Class")


class LeftSubclass(BaseClass):
    def callMe(self):
        print("Calling method on Left Subclass")
        super().callMe()


class RightSubclass(BaseClass):
    def callMe(self):
        print("Calling method on Right Subclass")
        super().callMe()


class Subclass(LeftSubclass, RightSubclass):
    def callMe(self):
        print("Calling method on Subclass")
        super().callMe()

s = Subclass()
s.callMe()

print(Subclass.mro())