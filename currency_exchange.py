def exchange_money(budget, exchange_rate):
    """
    This function returns the value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget/exchange_rate


def get_change(budget, exchanging_value):
    """
    This function returns the amount of money that is left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    This function returns the total value of bills of a certain denomination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return int(denomination * number_of_bills)


def get_number_of_bills(budget, denomination):
    """
    This function returns the number of bills of a certain denomination.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_leftover_of_bills(budget, denomination):
    """
    This function returns the amount that is left over, 
    after the exchange of the budget in to bills of certain denomination.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    
    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function takes in to account the exchange fee and adds it with the exchange rate (net_exchange_rate).
    It then finds the number of bills that can be of the given denomination.
    It then returns the maximum amount that can be exchanged.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    net_exchange_rate = exchange_rate * (1 + (spread/100)) 
    number_of_bills = int(budget/(net_exchange_rate * denomination))
    return number_of_bills * denomination
