# def gen_edge(RULE_REQUIRED: dict, REC_MET: dict, I: list):
#     res = []
#     for i in I:
#         for group in REC_MET:
#             if group in RULE_REQUIRED.values():
#                 if RULE_REQUIRED.get(i, None) != group:
#                     continue
#             for m in REC_MET[group]:
#                 res.append({
#                     "i": i,
#                     'm': m,
#                     "g": group
#                 })
#     return res
# W = [
#     [35, 43, 25],
#     [40, 34, 19],
#     [20, 28, 14],
#     [30, 51, 22],
#     [50, 61, 7],
#     [60, 49, 27],
#     [45, 34, 17],
#     [30, 44, 22],
#     [33, 35, 20],
#     [44, 25, 16],
#     [27, 31, 12],
#     [39, 32, 21]
# ]

import tkinter as tk

def gen_mdr(edges_by_g, rule_len_i, G, x=None):
    if x is None:
        x = []

    if len(G) == 0:
        return [x]
    res = []
    for edge in edges_by_g[G[0]]:
        if rule_len_i[edge["i"]] == 0:
            continue
        new_rule_len_i = rule_len_i.copy()
        if edge["i"] in new_rule_len_i:
            new_rule_len_i[edge["i"]] -= 1
        new_G = G[1:]
        new_x = x + [edge]
        res.extend(gen_mdr(edges_by_g, new_rule_len_i, new_G, new_x))

    return res


def min_w_in_x(x, num_w):
    w_n = []
    for i in x:
        w_n.append(i["w"][num_w - 1])
    return min(w_n)


def sum_w_in_x(x, num_w):
    w_n = 0
    for i in x:
        w_n += i["w"][num_w - 1]
    return w_n

def max_in_x(x, num_w):
    w_n = []
    for i in x:
        w_n.append(i["w"][num_w - 1])
    return max(w_n)

def create_vof(mdr, w_func):
    res = [[] for _ in range(len(w_func))]
    for x in mdr:
        for index, func in enumerate(w_func):
            res[index].append(func(x, index + 1))
    return res


def print_clear_vof(vof):
    print("\n@@PRINTING VOF")
    print("X:\t\tf1\t\tf2\t\tf3")
    for x_index in range(len(vof[0])):
        pr_str = f"{x_index + 1}:"
        for f_index in range(len(vof)):
            pr_str += f"\t\t{vof[f_index][x_index]}"
        print(pr_str)


def print_clear_mdr(mdr):
    print("\n@@PRINTING MDR")
    for index, x in enumerate(mdr):
        pr_str = f"{index + 1} = " + "{" + ", ".join(map(str, sorted([e["num"] for e in x]))) + "}"
        print(pr_str)


def find_pm(vof, f_priority):
    print(f"!!!PM FIND!!!")
    using_indexes = None
    for i in f_priority:
        this_f = vof[i - 1]

        if using_indexes:
            max_val = max([this_f[index] for index in using_indexes])
        else:
            max_val = max(this_f)

        if this_f.count(max_val) == 1:
            for j in range(len(this_f)):
                if this_f[j] == max_val and (not using_indexes or j in using_indexes):
                    print(f"Using F{i} => {[j]}")
                    print(f"!!!PM FOUND!!!")
                    return [j + 1]

        using_indexes = [i+1 for i, value in enumerate(this_f) if
                         value == max_val and (not using_indexes or i in using_indexes)]
        print(f"Using F{i} => {using_indexes}")

    print(f"!!!PM FOUND!!!")
    return [i for i in using_indexes]

def update_w_func():
    global W_FUNC
    W_FUNC = []

    # Обновляем W_FUNC на основе выбора пользователя в выпадающих списках
    selections = [option1.get(), option2.get(), option3.get()]
    for selection in selections:
        if selection == "MINMAX":
            W_FUNC.append(min_w_in_x)
        elif selection == "MAXSUM":
            W_FUNC.append(sum_w_in_x)

    print(f"Updated W_FUNC: {W_FUNC}")
    root.quit()  # Закрываем окно после выбора



if __name__ == "__main__":
    # REC_MET = {"g1": ["m1", "m3"], "g2": ["m4"], "g3": ["m2", "m6"], "g4": ["m5"], "g5": ["m4"]}
    # RULE_REQUIRED = {"i1": "g5", "i2": "g2"}
    G = ["g1", "g2", "g3", "g4", "g5"]
    M = ["m1", "m2", "m3", "m4", "m5", "m6"]
    I = ["i1", "i2"]
    RULE_LEN_I = {"i1": 3, "i2": 2}

    root = tk.Tk()
    root.title("Select W_FUNC Functions")

    root.geometry("400x200")

    options = ["MINMAX", "MAXSUM"]

    option1 = tk.StringVar(value=options[0])
    option2 = tk.StringVar(value=options[0])
    option3 = tk.StringVar(value=options[0])

    tk.Label(root, text="Select function for W_FUNC[0]:").pack(anchor=tk.W)
    tk.OptionMenu(root, option1, *options).pack(anchor=tk.W)
    tk.Label(root, text="Select function for W_FUNC[1]:").pack(anchor=tk.W)
    tk.OptionMenu(root, option2, *options).pack(anchor=tk.W)
    tk.Label(root, text="Select function for W_FUNC[2]:").pack(anchor=tk.W)
    tk.OptionMenu(root, option3, *options).pack(anchor=tk.W)
    tk.Button(root, text="Confirm", command=update_w_func).pack()

    root.mainloop()

    F_PRIORITY = [1, 2, 3]
    EDGES = [{'i': 'i1', 'm': 'm1', 'g': 'g1', 'w': [35, 43, 25], "num": 1},
             {'i': 'i1', 'm': 'm3', 'g': 'g1', 'w': [40, 34, 19], "num": 2},
             {'i': 'i1', 'm': 'm2', 'g': 'g3', 'w': [20, 28, 14], "num": 3},
             {'i': 'i1', 'm': 'm6', 'g': 'g3', 'w': [30, 51, 22], "num": 4},
             {'i': 'i1', 'm': 'm5', 'g': 'g4', 'w': [50, 61, 7], "num": 5},
             {'i': 'i1', 'm': 'm4', 'g': 'g5', 'w': [60, 49, 27], "num": 6},
             {'i': 'i2', 'm': 'm1', 'g': 'g1', 'w': [45, 34, 17], "num": 7},
             {'i': 'i2', 'm': 'm3', 'g': 'g1', 'w': [30, 44, 22], "num": 8},
             {'i': 'i2', 'm': 'm4', 'g': 'g2', 'w': [33, 35, 20], "num": 9},
             {'i': 'i2', 'm': 'm2', 'g': 'g3', 'w': [44, 25, 16], "num": 10},
             {'i': 'i2', 'm': 'm6', 'g': 'g3', 'w': [27, 31, 12], "num": 11},
             {'i': 'i2', 'm': 'm5', 'g': 'g4', 'w': [39, 32, 21], "num": 12}]

    EDGES_BY_G = {g: [] for g in G}
    for edge in EDGES:
        EDGES_BY_G[edge['g']].append(edge)

    MDR = gen_mdr(EDGES_BY_G, RULE_LEN_I, G)
    VOF = create_vof(MDR, W_FUNC)
    PM = find_pm(VOF, F_PRIORITY)
    #
    print_clear_mdr(MDR)
    print_clear_vof(VOF)
    print("\n@@PRINTING PM")
    print(PM)
