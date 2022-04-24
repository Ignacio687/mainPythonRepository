
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
            else:
                list = list[0:round(len(list)/2)]
        if list[0]==value:
            return True 
        else:
            return False

    def searchRecursive(self,list,value):
        if len(list)==0:
            return False
        elif len(list)==1:
            if list[0]==value:
                return True
            else: return False
        else:
            if list[round(len(list)/2)-1]<value:
                list = list[round(len(list)/2):]
            else:
                list = list[0:round(len(list)/2)]
        return self.searchRecursive(list, value)
        