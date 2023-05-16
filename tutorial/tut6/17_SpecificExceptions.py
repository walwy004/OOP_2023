class OnlyEvenNumbers(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added.")
        if integer % 2:
            raise ValueError("Only even numbers can be added.")

evenNumberList = OnlyEvenNumbers()
# evenNumberList.append("A string")

evenNumberList.append(3)