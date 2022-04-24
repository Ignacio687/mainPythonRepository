
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

# hacer esto recursivo