from Vehicle import Vehicle
from Bus import Bus
from Engine import Engine

vehicle = Vehicle(4, 4, "ZE1D4")
bus = Bus(8, 2, "B0TW", 40)
print("Engine details of vehicle. " + vehicle.showEngineDetails())
print("Engine details of bus. " + bus.showEngineDetails())