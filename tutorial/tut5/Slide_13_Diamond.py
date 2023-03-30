class BaseClass:
    def callMe(self):
        print("Calling method on Base Class")


class LeftSubclass(BaseClass):
    def callMe(self):
        print("Calling method on Left Subclass")
        BaseClass.callMe(self)


class RightSubclass(BaseClass):
    def callMe(self):
        print("Calling method on Right Subclass")
        BaseClass.callMe(self)


class Subclass(LeftSubclass, RightSubclass):
    def callMe(self):
        print("Calling method on Subclass")
        LeftSubclass.callMe(self)
        RightSubclass.callMe(self)

s = Subclass()
s.callMe()