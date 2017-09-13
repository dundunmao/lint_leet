# -*- encoding: utf-8 -*-
# Time:  O(n)
# Space: O(1)
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
# Note:
# The read function will only be called once for each test case.
#

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# read4是每次从给的file_content里读四个char读进buffer里，返回读了几个char,如果里面不够4个了，就返回实际读了几个
# 这题要求实现一个函数，输入为需要读的各数n，需要维护的内存buf，用read4函数，使读n个数进到buf里，返回实际读了几个数，
# 如果读了n个就返回n，如果file_content里的数小于n个，就只能读file_conten里的实际各数。
def read4(buffer):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buffer[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        our_buf = []
        api_buf = ['']*4
        pos = 0
        for i in range(n/4+1):
            size = read4(api_buf)
            if size != 0:
                our_buf[pos:pos+size] = api_buf
                pos = pos+size
            else:
                break
        s = min(n,pos)
        buf = our_buf[:s]
        return s



        # read_bytes = 0
        # buffer = [''] * 4
        # for i in xrange(n / 4 + 1):
        #     size = read4(buffer)
        #     if size:
        #         buf[read_bytes:read_bytes + size] = buffer
        #         read_bytes += size
        #     else:
        #         break
        # return min(read_bytes, n)


if __name__ == "__main__":
    global file_content
    buf = ['' for _ in xrange(100)]
    # file_content = "a"
    # print buf[:Solution().read(buf, 9)]
    file_content = "abcdefghijklmnop"
    print buf[:Solution().read(buf, 9)]