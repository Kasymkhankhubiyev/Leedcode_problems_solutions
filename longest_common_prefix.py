def get_list():
    strs = ['flower', 'flow', 'flight']
    # strs = ['car', 'dog', 'lamp']
    # strs = ['key', 'kentucky', 'ken']

    return strs

def longest_common_prefix(strs):

    prefix = ''

    lengths = [len(i) for i in strs]
    print(lengths)
    print(lengths.index(min(sorted(lengths))))

    for i in range(len(strs[lengths.index(min(sorted(lengths)))])):
        state = True
        for j in range(len(strs)):
            for k in range(j, len(strs), 1):
                if strs[j][i] != strs[k][i]:
                    state = False
                    break
            if state == False:
                break
        if state == False:
            break
        else:
            prefix += strs[lengths.index(min(sorted(lengths)))][i]

    print(prefix)