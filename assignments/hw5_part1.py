'''
Homework Assignment 5
Part 1
'''


def create_FOF(friends):

    fof = {}

    for name, friend_list in friends.items():
        fof_list = []
        for friend in friend_list:
            if friend in friends:
                fof_list.extend(friends[friend])

        # drop duplicates
        fof_list = list(set(fof_list))
        # remove key from list
        if name in fof_list:
            fof_list.remove(name)
        # remove direct friends
        for direct_friend in friend_list:
            if direct_friend in fof_list:
                fof_list.remove(direct_friend)

        fof[name] = fof_list

    return fof


friends = {
    "Lesley": ["Helen", "Jesus", "Menna"],
    "Jacob": ["Ojas", "Martin", "Eli"],
    "Shreyas": ["Ojas", "Jesus", "Martin", "Eli"],
    "Ojas": ["Jacob", "Shreyas", "Jesus"],
    "Jesus": ["Lesley", "Eli", "Keala"]
}

fof = create_FOF(friends)

for k, v in fof.items():
    print(k, v)
