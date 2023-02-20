def apiSort(arg):
    return {"sort": arg}

def apiFilter(arg,value):
    return {f"filter[{arg}]": value}

def apiRange(arg, value1, value2):
    return {f"range[{arg}]": f"{value1},{value2}"}
