def set_operations(a, b):
    _a = set(a)
    _b = set(b)

    return (_a & _b, _a | _b, _a - _b, _b - _a)


def char_dict(str):
    return {i:str.count(i) for i in str}


def compare_dicts(d1, d2):
    for k in d1:
        if not k in d2:
            return False
        if d1[k] != d2[k]:
            return False
    return True


def build_xml_element(tag, content, **parameters):
    result = f"<{tag}"
    for i in parameters:    
        result += f" {i}=\"{parameters[i]}\""
    
    result += f">{content}<\\{tag}>"

    return result


def validate_dict(rules, d):
    # s = dict(map(lambda rule: (rule[0], (rule[1:])),rules))
    s = {rule[0]:[r[1:] for r in rules if r[0] == rule[0]] for rule in rules}
    # print(s)

    for key in d:
        if key in s:
            val = d[key]
            # rul = s[key]
            for rul in s[key]:  # s[key] = list of rules for key
                if not (val.startswith(rul[0]) and val.count(rul[1]) > 0 and val.endswith(rul[2])):
                    return False
        else:
            return False
    return True


def list_unique_dups(l):
    s = set(l)
    return (len(s), len(l) - len(s))


def set_ops_var(*sets):
    d = {}
    for s1 in sets:
        for s2 in sets:
            if s2 != s1:
                if f"{s2} | {s1}" not in d:
                    d[f"{s1} | {s2}"] = s1 | s2
                    d[f"{s1} & {s2}"] = s1 & s2
                d[f"{s1} - {s2}"] = s1 - s2

    return d


def loop(d):
    el = d["start"]
    l = []

    while el not in l:
        l.append(el)
        el = d[el]

    return l


def my_function(*args, **keyword_args):
    args = set(args)
    keyword_args = set(keyword_args.values())
    return len(args & keyword_args)


print("ex1:  ", set_operations([1,2,4,3], [3,5,4,6]))
print("ex2:  ", char_dict("Ana has apples."))
print("ex3:  ", compare_dicts({"1":"sad",2:128, "j":[1,23,"g"]}, {"1":"sad",2:128, "j":[1,23,"g"]}))
print("ex4:  ", build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
print("ex5:  ", validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key2", "star", "ok", "inter")}, 
                              {"key1": "come inside, it's too cold out", "key3": "start middleok winter"}))
print("ex6:  ", list_unique_dups([1,2,3,3,3,4,5]))
print("ex7:  ", set_ops_var({1,2}, {2, 3}))
print("ex8:  ", loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
print("ex9:  ", my_function(1, 2, 3, x=1, y=2, z=3, w=5))