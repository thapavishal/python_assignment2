def cameltosnake_case(str):
    result = [str[0].lower()]
    for i in str[1:]:
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            result.append('_')
            result.append(i.lower())
        else:
            result.append(i)

    return ''.join(result)


input_str = "ThisIsACamelCase"
print(cameltosnake_case(input_str))
