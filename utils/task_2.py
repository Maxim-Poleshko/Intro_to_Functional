def up_name(member_list: list):
    """
    For each member make his name uppercase
    """
    return list({'age': memb['age'], 'name':memb['name'].upper()} for memb in member_list)
