"""prime numbers upto using"""


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
    # return {value: key if isinstance(key, str) else value for key, value in a.items()}
    return {
        (value if isinstance(key, str) else key): (
            key if isinstance(value, int) else value
        )
        for key, value in a.items()
    }


def rec(val):
    """recurssion"""
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
    n_main = {i: array.count(i) for i in array}
    # for i in array:
    #     main[i] = main.get(i, 0) + 1
    print("new main", n_main)
    return main


def list_of_lists(data):
    """list_of_lists"""
    array = set(rec(data))
    start = sorted([i for i in array if isinstance(i, int)])
    end = sorted([i for i in array if isinstance(i, str)], key=len)
    return start + end


def fib(a):
    """fib"""
    m = 1
    li = []
    n = 0
    for _ in range(0, a + 1):
        m, n = n, m + n
        li.append(m)
    return li


def fib_squares(a, k):
    """fib_squares"""
    li = [i**2 if i in fib(k) else i for i in range(a, k + 1)]
    return li


def set_complement(*args, verbose=True):
    """set_comlement"""
    # ans = [ [j for j in args[i] if j not in args[i+1] ] for i in range(len(args)-1)]
    #ans = [[j for j in range(len(str(i))) if args[i][j] not in args[((i*-1)-1)]] for i in range(len(args))]
    a = [set(i) for i in args]
    ans = [list(a[i] - a[j]) for i in range(len(str(a))) for j in range(i + 1, len(a))]

    if verbose:
        for i in args:
            ans.append(i)
        return ans
    return ans

def set_intersection(*args, verbose=True):
    """set_int"""
    a = [set(i) for i in args]
    ans = [list(a[i] & a[j]) for i in range(len(str(a))) for j in range(i + 1, len(a))]
    if verbose:
        for i in args:
            ans.append(i)
        return ans
    return ans


def check_equal(dict1, dict2):
    """incomplete """
    if isinstance(dict1, dict2):
        return -1
    

def dict_compare(*args):
    """incomplete had a logical error"""
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            # check = check_equal(args[i], args[j])
       
            return -1



def dict_from_lists(list1, list2):
    """set_int"""
    if len(list1) < len(list2):
        limit = list2
    else:
        limit = list1
    """extra code , this condition can be put in dict comprihension if required"""
    data = {list1[i]: list2[i] if list2[i] else " " for i in range(len(limit))}
    return data


def my_secret(message):
    """set_int"""
    if len(message) > 81:
        message = message[:81]
    mess = message.replace(" ","")
    secret_message = ""
    secret_message += "\n".join(mess[i : i + 7] for i in range(0, len(mess), 7))
    # secret_message += f'{mess[i:i+7] for i in range(0,len(mess),7)} '
    # li = [mess[i:i+7]  for i in range(0,len(mess),7) ]
    return secret_message


def cal(data, val):
    """Generate all possible words for a given phone number"""
    avl = [data[int(i)] for i in val if int(i) in data]
    ans = []
    for m in range(len(avl)):
        s_sum = ""
        for i in range(1, len(avl[m])):
            for j in range(len(avl)):
                s_sum += avl[j][i]
            ans.append(avl[m][i] + s_sum)
    return ans


def phone_words(ph1, ph2):
    """Generate phone words for given phone numbers"""
    data = {
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PRS",
        8: "TUV",
        9: "WXY",
    }

    output = {
        val: cal(data, val) if "1" not in val and "0" not in val else []
        for val in [ph1, ph2]
    }
    return output

"""need to work on the code """


if __name__ == "__main__":
    b = {"one": 1, "two": 2, 3: "three"}
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
    print(set_complement([2, 5, 6], [6, 9, 1], [5, 8, 9]))
    print(set_intersection([2, 5, 6], [6, 9, 1], [5, 8, 9]))
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    print(dict_from_lists(list1, list2))
    print(
        my_secret(
            "If man was meant to stay on the ground god would have given us roots"
        )
    )
    print(phone_words("1234567", "2345678"))
