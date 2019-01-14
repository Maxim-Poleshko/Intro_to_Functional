def add_load(member_list: list):
    """
    Each member will be exclude of group after reaching the age of 200 years"
    """
    member_list = list(filter(lambda x: x["age"] < 200, member_list))
    return list(map(lambda x: {'age': x['age'], 'name': x['name'], 'load': x["age"] * 0.5}, member_list))
