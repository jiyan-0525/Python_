
def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if obj_type is list:
        print(f"List: {object}")
    elif obj_type is tuple:
        print(f"Tuple: {object}")
    elif obj_type is set:
        print(f"Set: {object}")
    elif obj_type is dict:
        print(f"Dict: {object}")
    elif obj_type is str:
        if object == "Brian":
            print(f"Brian is in the kitchen: {object}")
        elif object == "TOto":
            print(f"TOto is in the kitchen: {object}")
        else:
            print("Type not found")
    else:
        print("Type not found")
    return 42
