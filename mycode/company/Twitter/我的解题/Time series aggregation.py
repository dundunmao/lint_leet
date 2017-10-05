# -*- encoding: utf-8 -*-
# input:
# 2015-08, 2016-04
#
# 2015-08-15, clicks, 635
# 2016-03-24, app_installs, 683
# 2015-04-05, favorites, 763
# 2016-01-22, favorites, 788
# 2015-12-26, clicks, 525
# 2016-06-03, retweets, 101
# 2015-12-02, app_installs, 982
# 2016-09-17, app_installs, 770
# 2015-11-07, impressions, 245
# 2016-10-16, impressions, 567
# input里第一行是start time和end time，用'，'and zero or more space隔开，
# 第二行空行，
# 第三行是时间和动作和次数。the purpose is to aggregate the data by month and engagement category for the requested time interval.用逗号或spaces隔开
# 每行用'\n'隔开
# output:
# 2016-03,app_installs,683
# 2016-01,favorites,788
# 2015-12,app_installs,982.clicks,525
# 2015-11,impressions,245
# 2015-08,clicks,635
# output里含有（yyyy-mm）。totals for each engagement type where the total is greater than 0. each field on a given line must be separeted by a single comma',',followed by a single space character' '


def deal_with(input):
    info = input.split('\n')
    start = filter(str.isdigit,info[0].split(',')[0])  #'2015-08'
    end = filter(str.isdigit,info[0].split(',')[1])   #'2016-04'
    #array = [['2015-08-15', ' clicks', ' 635'], ['2016-03-24', ' app_installs', ' 683'], ['2015-04-05', ' favorites', ' 763'], ['2016-01-22', ' favorites', ' 788'], ['2015-12-26', ' clicks', ' 525'], ['2016-06-03', ' retweets', ' 101'], ['2015-12-02', ' app_installs', ' 982'], ['2016-09-17', ' app_installs', ' 770'], ['2015-11-07', ' impressions', ' 245'], ['2016-10-16', ' impressions', ' 567']]
    array = [ele.split(',') for ele in info[2:]]
    res = {}
    for ele in array:
        # res[ele[0][:7]] = []+[(ele[1],ele[2])]
        res.setdefault(filter(str.isdigit, ele[0][:7]), []).append((ele[0][:7],ele[1],ele[2]))
    return start,end,res



def time_series(start,end,list):
    res = []
    trans = [(key,value) for key,value in list.items() if key >= start and key < end]
    sort_trans = sorted(trans,key = lambda x:x[0],reverse=True)
    for ele in sort_trans:
        hash = {}
        array = []
        for tuple in ele[1]:
            if hash.has_key(tuple[1]):
                hash[tuple[1]] += int(tuple[2])
            else:
                hash[tuple[1]] = int(tuple[2])
        for k,v in hash.items():
             array += [k,str(v)]
        res.append([ele[0]]+array)
    res = [','.join(ele) for ele in res]
    return '\n'.join(res)



    # return

if __name__ == "__main__":
    input = '2015-08,2016-04\n \n2015-08-15, clicks, 645\n2015-08-15, clicks, 635\n2016-03-24, app_installs, 683\n2015-04-05, favorites, 763\n2016-01-22, favorites, 788\n2015-12-26, clicks, 525\n2016-06-03, retweets, 101\n2015-12-02, app_installs, 982\n2016-09-17, app_installs, 770\n2015-11-07, impressions, 245\n2016-10-16, impressions, 567'
    # S = 'bbabcab'
    # print check('ADCD','ABCD')
    start,end,list = deal_with(input)
    print time_series(start,end,list)