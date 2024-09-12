# valid paranthsis
class Solution(object):
    def isValid(self, s):
        b=[]
        for i in range(len(s)):
            if s[i]=="(":
                b.append(s[i])
            elif s[i]=="[":
                b.append(s[i])
            elif s[i]=="{":
                b.append(s[i])
            elif s[i]==")":
                if len(b)!=0:
                    tem=b.pop(-1)
                    if tem!="(":
                        return False
                else:
                    return False
            elif s[i]=="]":
                if len(b)!=0:
                    tem=b.pop(-1)
                    if tem!="[":
                        return False
                else:
                    return False
            elif s[i]=="}":
                if len(b)!=0:
                    tem=b.pop(-1)
                    print(tem)
                    print(s[i])
                    if tem!="{":
                        return False
                else:
                    return False
        if len(b)==0:
            return True

                
            
            