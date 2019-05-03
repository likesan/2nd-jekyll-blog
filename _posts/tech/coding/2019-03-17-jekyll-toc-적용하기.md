---
layout: post
comments : true
category: ["Coding","Jekyll"]
---

* TOC
{:toc}

글을 써놓고,
목차별로 한 눈에 볼 수 있게 만들고 싶었다.
내가 쓴 포스트가 어떤 내용인지 한 눈에 짧고 빠르게 훑어볼 수 있는 방법이랄까?

생각보다 간단한건가. Jekyll은 생각보다 간결하고 쉬워서 정말 좋다. 손이 생각보다 많이 안간다. 딱 스트레스 받을 정도도 없고, '이렇게 적용하면 되는건가?' 하고 한 두 스탭만 넘어가면 되니 정말 편안하다.
노 스트레스 코딩. 코딩하는 재미도 남겨주고 :)

1. `default.html`에 `{{content | toc}}` 해주기

2. 각 post 최상단에 밑의 코드를 넣어주자

    
# 결과 모습

![toc 적용 결과](https://user-images.githubusercontent.com/803398/28401295-0dcfb7ca-6d54-11e7-892b-2f2e6ca755a7.png)


# 참고
[깃허브 plugin](https://github.com/toshimaru/jekyll-toc)
[How I Add a Table of Contents to my Jekyll Blog Written in Markdown](http://www.seanbuscay.com/blog/jekyll-toc-markdown/)
