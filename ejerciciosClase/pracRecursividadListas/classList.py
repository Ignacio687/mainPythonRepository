
from operator import truediv
from pickletools import read_unicodestring1


class SearchList():
    def searchProcedural(self, list, value):
        if len(list) == 0:
            return False
        start = 0
        end = len(list)
        while list[start] or list[end] == value or start == end or start == (end-1):
            if list[end//2] == value:
                return True
                break
            elif list[(end-start)//2] > value:
                end = (end//2)-1
            elif list[end//2] < value:
                start = (end//2)+1


# hacer esto recursivo