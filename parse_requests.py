OPERATORS = ["AND", "OR", "NOT"]

def parse_query(query: str) -> dict[str, list: str]:
    result = {}
    tokens = query.split()
    i = 1
    while i < len(tokens):
        if i+1 >= len(tokens):
            break
        if tokens[i].upper() in OPERATORS:
            if tokens[i+1].upper() in OPERATORS:
                return {}
            operator = tokens[i].upper()
            if i == 1:
                result[operator] = [tokens[i-1], tokens[i+1]]
            elif operator not in result:
                result[operator] = tokens[i+1]
            else:
                result[operator].append(tokens[i+1])
            i+=2
        else:
            result[operator].append(tokens[i])
            i+=1
    return result

if __name__ == "__main__":
    request = "yesterday and graph and pyton or java not RUST"
    result = parse_query(request)
    print(result)