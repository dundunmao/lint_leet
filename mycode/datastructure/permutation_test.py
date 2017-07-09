__author__ = 'eva'

# def check_permuta(str1, str2):
#     if len(str1) == len(str2):
#
#         dict = {}
#         for i in range(0,len(str1), 1): #traverse a list
#             dict[input_str1[i]] = 1
#         for j in range(0,len(str2), 1):
#             try:
#                 del dict[str2[j]]
#             except:
#                     return False
#         if dict == {}:
#             return True
#         else:
#             return False
#     else:
#         return False

def check_permuta(str1, str2):
    if isinstance(str1, basestring) & isinstance(str2, basestring):
        if len(str1) == len(str2):
            dict = {}
            for i in range(0,len(str1), 1):
                if input_str1[i] in dict:
                    dict[input_str1[i]] += 1
                else:
                    dict[input_str1[i]] = 1
            for j in range(0,len(str2), 1):
                try:
                    if dict[str2[j]] == 1:
                        del dict[str2[j]]
                    else:
                        dict[str2[j]] -= 1
                except KeyError:
                        return False
            if dict == {}:
                return True
            else:
                return False
        else:
            return False
    else:
        print "input string!"
if __name__ == "__main__":
    input_str1 = "1"
    input_str2 = 1
    res = check_permuta(input_str1,input_str2)
    print res
    print "\n"

