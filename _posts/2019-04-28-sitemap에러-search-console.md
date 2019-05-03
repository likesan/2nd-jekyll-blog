---
layout : post
category : [Blog, Jekyll, Error, Search Console]
comments : true
---

* TOC
{:toc}

구글 Search Console을 통해 다시 수정된 주소로
구글에 검색되게 만들고자 했다.

그 중 만난 에러

# 문제

```
error on line 36 at column 231: xmlParseEntityRef: no name
```

# 해결 

포스트 제목에
`! @ # $% ^ & * () _ `
중 하나가 들어가 있으면 대체로 에러가 발생된단다.

# 참고

[Swarakalibata ci Rss error - xmlParseEntityRef: no name](https://members.phpmu.com/forum/read/swarakalibata-ci-rss-error)

