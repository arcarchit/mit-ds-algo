

def build_tree(x,y, split):
    ans = {} # It will have attributes like left, right

    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)

    if len(x)<=2:
        ans = {'is_leaf':True, 'no_nodes':len(x), 'data_x':x, 'data_y':y}
        return ans

    if split=='x':
        split_val = (xmin + xmax) / 2.0
        left_index = [i for i in range(len(x)) if x[i]<=split_val]

        ans = {'is_leaf': False, 'no_nodes': len(x), 'data_x': x, 'data_y': y}
        ans['split'] = split
        ans['split_value'] = split_val
        ans['xmin'], ans['xmax'], ans['ymin'], ans['ymax'] = xmin, xmax, ymin, ymax

        new_split = 'y'
        x1, y1 = [x[j] for j in left_index], [y[j] for j in left_index]
        ans['left'] = build_tree(x1, y1, new_split)
        ans['right'] = build_tree([i for i in x if i not in x1], [i for i in y if i not in y1], new_split)

    else:
        split_val = (ymin+ymax)/2.0
        left_index = [i for i in range(len(x)) if y[i] <= split_val]

        ans = {'is_leaf': False, 'no_nodes': len(x), 'data_x': x, 'data_y': y}
        ans['split'] = split
        ans['split_value'] = split_val
        ans['xmin'], ans['xmax'], ans['ymin'], ans['ymax'] = xmin, xmax, ymin, ymax

        new_split = 'x'
        x1, y1 = [x[j] for j in left_index], [y[j] for j in left_index]
        ans['left'] = build_tree(x1, y1, new_split)
        ans['right'] = build_tree([i for i in x if i not in x1], [i for i in y if i not in y1], new_split)

    return ans

if __name__=="__main__":
    x = [-1.58, 0.91, -0.73, -4.22, 4.19, -0.33]
    y = [-2.01, 3.98, 4.00, 1.16, -2.02, 2.15]

    split = 'x'

    ans = build_tree(x, y, split)


    def pretty(d, indent=0):
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                pretty(value, indent + 1)
            else:
                print('\t' * (indent + 1) + str(value))

    print pretty(ans)

    in_x, in_y = -3, 1.5

    node = ans
    while (not node['is_leaf']):
        print node['is_leaf'], node
        print "changing", node['split'], node['split_value']
        if node['split']=='x':
            if in_x <= node['split_value']:
                node = node['left']
                print "left"
            else:
                node = node['right']
                print "right"
        else:
            if in_y <= node['split_value']:
                node = node['left']
                print "left"
            else:
                node = node['right']
                print "right"
    print node['data_x'], node['data_y']


    print "------ Pruning -------"


