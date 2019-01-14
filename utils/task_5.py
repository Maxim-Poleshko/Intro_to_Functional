def ages(memb: list):
    """
    The funtion return three values:Summary age, youngest member, oldest member
    """
    return sum(map(lambda x: x['age'], memb)), min(memb, key=lambda x: x['age']), max(memb, key=lambda x: x['age'])
