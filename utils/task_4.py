def left_members(member_list: list):
    """
    Left only those members who have letter 'o' in names
    """
    return list(filter(lambda x: "o" in x["name"], member_list))
