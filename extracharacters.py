def in_dict(dictionary,ss):
    for i in dictionary:
        if i in ss:
            return True
    return False

def solve(dictionary,ss):
    for i in dictionary:
        if i in ss:
            first_index= ss.index(i)
            second_index=first_index+len(i) -1
            ss=ss[0:first_index]+ss[second_index+1:]
            break
    # print(ss)
    return ss
    
def minExtraChar( s: str, dictionary) -> int:
    while in_dict(dictionary,s):
        s=solve(dictionary,s)
        print(s)
                    
    # print(s)
    return len(s)

# s = "leetscode"
# dictionary = ["leet","code","leetcode"]

# s = "sayhelloworld"
# dictionary = ["hello","sayworld"]

# s="ecolloycollotkvzqpdaumuqgs"
# dictionary=["flbri","uaaz","numy","laper","ioqyt","tkvz","ndjb","gmg","gdpbo","x","collo","vuh","qhozp","iwk","paqgn","m","mhx","jgren","qqshd","qr","qpdau","oeeuq","c","qkot","uxqvx","lhgid","vchsk","drqx","keaua","yaru","mla","shz","lby","vdxlv","xyai","lxtgl","inz","brhi","iukt","f","lbjou","vb","sz","ilkra","izwk","muqgs","gom","je"]

# s="flflbribri"
# dictionary=["flbri","uaaz"]

s="dwmodizxvvbosxxw"

dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
dictionary.sort(key=len,reverse=True)

print(dictionary)
print(minExtraChar(s,dictionary))
    

   
# temp="leet"
# mystr="leetscode"


# first_index=temp.index(temp[0])
# second_index=temp.index(temp[-1])
# print(first_index,second_index)

# mystr=mystr[0:first_index]+mystr[second_index+1:]
# print(mystr)



#include <iostream>
#include <string>



# a="hello"
# print(id(a))
# a="world"
# print(id(a))