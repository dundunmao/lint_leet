# -*- encoding: utf-8 -*-
# Logger Rate Limiter 记录速率限制器
# 这道题让我们设计一个记录系统每次接受信息并保存时间戳，然后让我们打印出该消息，前提是最近10秒内没有打印出这个消息
# Example:
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;

class Logger():
    def __init__(self):
        self.message = {}
    def shouldPrintMessage(self,time,str):
        if self.message.has_key(str):
            if time - self.message[str] > 10:
                return True
            else:
                return False
        else:
            self.message[str] = time
            return True


