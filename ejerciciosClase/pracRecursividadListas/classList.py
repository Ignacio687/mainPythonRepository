
from ast import Break
from operator import truediv
from pickletools import read_unicodestring1


class SearchList():
    def searchProcedural(self, list, value):
        if len(list) == 0:
            return False
        while len(list) >1:
            if list[round(len(list)/2)-1]<value:
                list = list[round(len(list)/2):]
            elif list[round(len(list)/2)-1]>=value:
                    list = list[0:round(len(list)/2)]
        if list[0]==value:
            return True 
        else:
            return False




        # start = 0
        # end = len(list)
        # while list[start] or list[end] == value or start == end or start == (end-1):
        #     if list[end//2-value] == value:
        #         return True
        #         break
        #     elif list[(end-start)//2] > value:
        #         end = (end//2)-1
        #     elif list[end//2-start] < value:
        #         start = start+(end//2-start)+1


# hacer esto recursivo