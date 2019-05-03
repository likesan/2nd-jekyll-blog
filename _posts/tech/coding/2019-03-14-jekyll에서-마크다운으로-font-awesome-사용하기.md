---
layout: post
comments : true
category: ["Coding","Jekyll"]
---


* Toc
{:toc}

- [FontAwesome 사이트](https://fontawesome.com/icons?from=io)에서 CDN을 복사한다.

```
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
```

- `_layout` 폴더의 `Default.html` 문서, `<head></head>` 태그 안에 저 CDN을 넣어준다.

- 다시 FontAwesome 사이트에서 [사용하고 싶은 아이콘]((https://fontawesome.com/icons?from=io))을 찾아낸다.


# 주요 참조

- [Embedding Fontawesome Icons - Markdown Monster Documents](https://markdownmonster.west-wind.com/docs/_4ue01xl6q.htm)

- [Why is Font Awesome not working on my jekyll-built Github site?](https://stackoverflow.com/questions/25797627/why-is-font-awesome-not-working-on-my-jekyll-built-github-site#answer-25823072)

