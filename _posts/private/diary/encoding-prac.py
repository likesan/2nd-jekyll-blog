# -*- coding: utf-8 -*-

import sys



hashtag = [u"사랑",u"고양이",u"꿈"]
i = 0


# print(type(hashtag[0]))
# print(hashtag[0])

while i < len(hashtag):
    print(i)
    print(hashtag[i])
    i=i+1


# 유니코드 - utf-8 는 쌍이다.
# 유니코드로 인식시켜주지 않으면, 
# 에러가 난다고...