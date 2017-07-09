# -*- encoding: utf-8 -*-
# 1级
# 标签：math
# 题目；找两个长方形的重叠后的总面积，第一个（A,B）(C,D)第二个（E,F)(G,H)
# 思路：（两个面积之和）-（重叠面积）
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        total = (C - A) * (D - B) + (G - E) * (H - F)
        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))

        return total - width * height