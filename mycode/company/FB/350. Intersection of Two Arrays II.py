# -*- encoding: utf-8 -*-
# 给一个字典包括很多字符串(e.g., abcd, dhfyf)，然后给定一个字符串查看字典中是否包含这个字符串。字符串中可能包括*，*可以匹配任何字符。我用的Trie。
#
# Task那道题，很多面经都提到过。就是比如给你一串task，再给一个cooldown，执行每个task需要时间1，两个相同task之间必须至少相距cooldown的时间，问执行所有task总共需要多少时间。比如执行如下task：12323，假设cooldown是3。总共需要的时间应该是 1 2 3 _ _ 2 3，也就是7个单位的时间。再比如 1242353，假设cool down是4，那总共时间就是 1 2 4 _ _ _ 2 3 5 _ _ _ 3，也就是13个单位的时间
# •	基于1，给出最优的排列，使得字符串最短。
#
#
# 自然string comparator。不知道的搜下。就是string 比较的时候考虑里面数字的大小，比如 abc9 < abc123 abc > ab9  因为char比digit重要。