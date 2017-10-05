# -*- encoding: utf-8 -*-
# 给email和phone number，mask 关键信息。
# email留第一个和最后一个，中间用五个*替代，@后面留着。
# 电话号：要看有没有country code，*代表每一个number。如下：
# +1（333）444-5678 --》+*-***-***-5678
# +91（333）444-5678 --》+**-***-***-5678
# +111（333）444-5678 --》+***-***-***-5678
# 333 444 5678 --》***-***-5678
# （333）444-5678 --》***-***-5678

# ignore space
# Input:
# E: jackAndJill@twitter.com
# P: +13334445678
# Output:
# E: j*****l@twitter.com
# P: +*-***-***-5678
def mask_email(email):
    res = [email[0],'*****']
    i = 1
    while i+1 < len(email):
        if email[i+1] == '@':
            res.append(email[i])
            res += email[i+1:]
        i+=1
    return ''.join(res)

def mask_phone(phone):
    res = ['***-***-'] + [str(ele) for ele in phone[-4:]]
    if len(phone) == 10:
        return ''.join(res)
    elif len(phone) == 11:
        res = ['+*-'] + res
        return ''.join(res)
    elif len(phone) == 12:
        res = ['+**-'] + res
        return ''.join(res)
    elif len(phone) == 13:
        res = ['+***-'] + res
        return ''.join(res)


def deal_with(input):
    x = input.split('/n')
    email = [ele for ele in x[0] if ele != ' ']
    phone = [num for num in x[1] if num.isdigit()]
    return email[2:],phone[1:]

if __name__ == '__main__':
    input = 'E: jackAndJill@twitter.com'+ '/n' +'P:+111（333）444-5678'
    email, phone = deal_with(input)
    print mask_email(email)
    print mask_phone(phone)
