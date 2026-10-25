def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif obj_type is float and object != object:  # Check for NaN
        print(f"Cheese: {object} {obj_type}")
    elif obj_type is bool and object is False:
        print(f"Fake: {object} {obj_type}")
    elif obj_type is int and object == 0:
        print(f"Zero: {object} {obj_type}")
    elif obj_type is str and object == "":
        print(f"Empty: {object} {obj_type}")
    else:
        print("Type not found")
        return 1
    return 0