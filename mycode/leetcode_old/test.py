#
#
# month = dict(one='January',
#                  two='February',
#                  three='March',
#                  four='April',
#                  five='May')
# print month
# numbermap = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# print sorted(month, key=numbermap.__getitem__)
#
# print [month[i] for i in sorted(month, key=numbermap.__getitem__)]

s = [1,3,5,7,9,11,13,15]
x = []
for i in s:
    for j in s:
        x.append(round(float(i)/j,5))
i,j = 0,0
for i in x:
    for j in x:
        for k in x:
            if abs(i+j+k - 30)<0.00005:
                print i,j,k
# print i, j, k





# dic = {'FAst': 15, 'second': 2, 'third': 3, 'Fourth': 4}
# print list(dic)
# print dic.values()
# a = dic.__getitem__('second')
#
# print "*****"
# print sorted(dic)
# print sorted(dic.keys())
# print sorted(dic.values())
#
# print "*****"
# print sorted(dic, key= dic.__getitem__)
#
# print [value for (key, value) in sorted(dic.items())]
# print [(key, value) for (key, value) in sorted(dic.items())]
# print sorted(dic, key= dic.__getitem__, reverse=True)
# print sorted(dic, key=str.lower)

