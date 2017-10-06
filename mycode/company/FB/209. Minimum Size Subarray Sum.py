# -*- encoding: utf-8 -*-
# •	Map store previous values ( O(N) )
# •	把第一题extend到2D。给一个matrix, all elements are positive，问有没有个sub rectangle加起来和等于target。return true/false。
# •	Lz听到题目有点懵，认真调整心态，解决之。先写了个cumulative sum。把所有从0,0 到i,j的和算在新的matrix的i,j上。方便之后算head到tail的sub rectangle的和。这一步O(n^2)
