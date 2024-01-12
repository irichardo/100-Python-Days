def integerOrFloat(number, type):
    match type:
        case "integer":
            return int(number)
        case "float":
            return float(number)
