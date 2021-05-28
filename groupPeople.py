class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        mapping = {}
        index = 0
        for size in groupSizes:
            if size not in mapping:
                mapping[size] = [index]
            else:
                mapping[size].append(index)
            index += 1
        resultList = []
        for size in mapping:
            i = 0
            templist = []
            while(i<size):
                if(mapping[size]!=[]):
                    templist.append(mapping[size].pop())
                    if (len(templist) == size):
                        resultList.append(templist)
                        templist = []
                        i = 0
                    else:
                        i+=1
                else:
                    break
        return resultList
