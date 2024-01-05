"""prime numbers upto using"""

def fib(b):
    """fib"""
    m = 1
    li = []
    n = 0
    for _ in range(0, b + 1):
        m, n = n, m + n
        li.append(m)
    return li


def nested_prime(n):
    """nested prime"""
    li = [
        i
        for i in range(2, n + 1)
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1))
    ]
    return li


def old_school_reverse(n):
    """old_school_reverse"""
    li = [n[-i] for i in range(1, len(n) + 1)]
    return " ".join(li).replace(" ", "")


def dict_a_noodle(a):
    """dict_a_noodle"""
    new_dict = {
        value: key if isinstance(key, str) else value for key, value in a.items()
    }
    return new_dict


def rec(val):
    """val"""
    li = []
    for i in val:
        if isinstance(i, list):
            li.extend(rec(i))
        elif not isinstance(i, dict):
            li.append(i)
    return li


def dict_of_lists(data):
    """dict_of_lists"""
    array = rec(data)
    main = {}
    for i in array:
        main[i] = main.get(i, 0) + 1
    return main


def list_of_lists(data):
    """list_of_lists"""
    array = set(rec(data))
    start = sorted([i for i in array if isinstance(i, int)])
    end = sorted([i for i in array if isinstance(i, str)], key=len)
    return start + end




def fib_squares(a, b):
    """fib_squares"""
    li = [i**2 if i in fib(b) else i for i in range(a, b + 1)]
    return li




if __name__ == "__main__":
    b= {"one": 1, "two": 2, 3: "three"}
    print(nested_prime(10))
    print(old_school_reverse("hiamkunal"))
    print(dict_a_noodle(b))
    print(fib_squares(2, 5))
    data_new = [
        [[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]],
        [5, 2, 1],
        1,
    ]
    print(dict_of_lists(data_new))
    print(list_of_lists(data_new))
