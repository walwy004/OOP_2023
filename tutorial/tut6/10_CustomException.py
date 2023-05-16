class InvalidWithdrawal(Exception):
    pass

raise InvalidWithdrawal("You do not have enough funds to withdraw.")