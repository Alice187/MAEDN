import operator
whole_list = []
new = sorted(whole_list, key=operator.itemgetter(0, 1))
print(new)