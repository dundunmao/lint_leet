class interview(object):
    def __init__(self):
        pass
    def to_matrix(self,file):
        a = open(file,'r')
        for line in a.readlines():
            line.split('-',' ')
        return a
    def most_url(self,a):
        dict_url= {}
        for i in range(0, len(a)):
            if dict_url.has_key(a[i]):
                dict_url[a[i]] += 1
            else:
                dict_url[a[i]] = 1
        # list_want = sorted(dict_url, key=dict_url.__getitem__(),resever = True)
        # return list_want[0]
        return sorted(dict_url.items(), key=lambda dict_url: (dict_url[1],dict_url[0]), reverse=True)
            
