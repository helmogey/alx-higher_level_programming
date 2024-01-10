def search_replace(my_list, search, replace):
    if search < len(my_list) and search >= 0:
        out = []
        for i in range(len(my_list)):
            if my_list[i] == search:
                out.append(replace)
            else:
                out.append(my_list[i])
        return out
