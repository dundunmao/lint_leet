# input="aaabbcddddeeea"
# output="3a2b1c4d3e1a"

def compress_string(input_s):
    #validate input_s, we can also raise an exception for illegal input type of a given string, we return an empty by default
    # if type(input_s) != 'string':
    #     return ''

    output_str = ''
    output_str_list = []
    #extend the string pool (a list for chars) to 2X input_s lenth, due to the case
    # 'abc' => '1a1b1c' expected which doublel the original string, actually not a compressed string and therefore can not achieve the goal for string compression. This need more code to handle such a condition.
    for i in range(0, len(input_s)*2):
        output_str_list.append('')

    insert_index = 0

    i = 0

    while i < len(input_s):
        j = i + 1
        counter = 1
        while j < len(input_s) and input_s[j] ==  input_s[i]:
            i += 1
            j += 1
            counter += 1
        # print insert_index, len(output_str_list), i, len(input_s)
        output_str_list[insert_index] = input_s[i]
        # print output_str_list[insert_index]
        # if counter > 1:
        count_str = str(counter)
        # print counter
        for k in range(0, len(count_str)):
            output_str_list[insert_index] = count_str[k]
            insert_index +=1
        insert_index += 1
        output_str_list[insert_index] = input_s[i]
        insert_index += 1
        i = j

    # convert a list of chars to the output string called output_str
    for i in range(0, len(output_str_list)):
        if output_str_list[i]:
            output_str += output_str_list[i]
    return output_str

if __name__ == '__main__':
    #testing
    #case 1: an illegal input
    # print compress_string('')
    # case 2: an empty string
    # print compress_string([1,3,4])
    # case 3: an normal string = > 2a1b2vfew
    # print compress_string('aabvvfevw')
    #case 4: an normal string
    print compress_string('aaabbcddddeeea') == '3a2b1c4d3e1a'

# input="aaabbcddddeeea"
# output="3a2b1c4d3e1a"
def compress_string_mm(input_s):
    #validate input_s tpye
    # if type(input_s) != 'str':
    #     return ""
    output_str = ""
    output_list = []
    start = input_s[0]
    count = 1
    i = 1
    if len(input_s) == 1:
        output_list =['1',input_s]
        output_str = ''.join(output_list)
        return output_str
    while i<len(input_s):
        if input_s[i] == start:
            count+=1
            i+=1
            if i == len(input_s):
                output_list.extend([str(count),start])
        else:
            a = [str(count),start]
            print a
            start = input_s[i]
            count =1
            i+=1
            output_list.extend(a)
            if i == len(input_s):
                output_list.extend([str(count),start])
    # transfer list to str
    output_str = ''.join(output_list)
    return output_str

if __name__ == "__main__":
    print compress_string_mm('aaabbcddddeeea')
    print compress_string_mm('a')






















