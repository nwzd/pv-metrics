def is_null_or_empty(value):
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    return False
    
def is_not_null_nor_empty(value):
    return not is_null_or_empty(value)


def trim_and_lower_case(value):
    return value.strip().lower()