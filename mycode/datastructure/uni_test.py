
def sub_string(str1, str2):
    if isinstance(str1, basestring) & isinstance(str2, basestring):
        if len(str2) > len(str1):
            return False
        if len(str2) == 0 and len(str1) == 0:
            return True
        for i in range(0,len(str1)):
           if str1[i:i+len(str2)] == str2:
                return True
        return False
    else:
        print ("input string please")


def sub_sequence(str1, str2):
    # check if str2 in str1
    if len(str2) > len(str1):
        return False
    str1_list = list(str1)


    for i in range(len(str2)):
        len1 = len(str1_list)
        try:
            str1_list.remove(str2[i])
        except ValueError:
            return False
        if len(str1_list) != len1-1:
            return False

    return True


def check_unique(input_str):
    dict = {}
    for i in range(0,len(input_str), 1): #traverse a list
        # print input_str[i]
        if input_str[i] in dict:
            return False
        else:
            dict[input_str[i]] = 1
    return True

def print_char_num(input_str):
    dict = {}
    for i in range(0,len(input_str), 1):
        if input_str[i] in dict:
            dict[input_str[i]] += 1
        else:
            dict[input_str[i]] = 1
    for k, v in dict.iteritems():
        print k , v
    for k in dict.keys():
        print k
    for v in dict.values():
        print v
    return



if __name__ == "__main__":

    str1 = 12
    str2 = 1
    res2 = sub_string(str1, str2)
    print res2
    # res1 = sub_sequence(str1, str2)
    # print res1

    # input_str = "asioi"
    # res = check_unique(input_str)
    # print res
    # print "\n"
    # print_char_num(input_str)