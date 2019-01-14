def sort_m(memb: list):
    """
    Sort members by length of their names. If length of names is equal than sort by age.
    """
    return sorted(memb, key=lambda x: (len(x['name']), x['age']))
