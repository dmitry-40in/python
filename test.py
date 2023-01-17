field = ['X', 2,3, 4,'X', 6, 7, 8, 'X']
wins_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def win_check(a, b):
    for i in b:
        if a[i[0]] == a[i[1]] == a[i[2]]:
            print(a[i[0]], a[i[1]], a[i[2]])
            check = True
            break
        else:
            print(a[i[0]], a[i[1]], a[i[2]])
            check = False
    return check

def win_check(a, b):
    for i in b:
        if a[i[0]] == a[i[1]] == a[i[2]]:
            print(a[i[0]], a[i[1]], a[i[2]])
            return True
            #break
        else:
            print(a[i[0]], a[i[1]], a[i[2]])
            return False
    #return check        

print(win_check(field, wins_index))