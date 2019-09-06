---
layout: post
comments: true
category : [Google Adsense, Marketing, Passive income, Coding, Blogging]
thumbnail : https://images.unsplash.com/photo-1518183214770-9cffbec72538?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80
---

* TOC
{:toc}

# Google adsense 사이드 ad 만들기

그렇게 어렵진 않았다.
하지만, 생각보다 손이 가는 건 어쩔 수 없었다.

## Liquid 문법을 알아야했다.

Java, Javascript 등을 하다보면
else if 문을 어떻게 넣어줘야하는지 헷갈리기 시작한다.


## 내가 넣은 Sidebar 의 CSS 는 다음과 같다. 

```css
@media(max-width:768px) {
    .floating-ad {
     display: none;
    }
}
@media(min-width:769px){
    .floating-ad {
        top: 3.42em;
        position: fixed;
        width: 20vw;
        height: 50vw;
        right: 5;
        display: inline-block;
        /* border: 1px solid black; */
    }
}
```
### 구현된 모습

![google-adsense-넣기-사이드바](https://user-images.githubusercontent.com/35059428/64404808-ba011c80-d0af-11e9-9f48-ca1d40d7f638.gif)


### 주된 특징은 다음과 같다.

1. `@media` 태그를 써, 타블렛크기까지는 나타나지 않게 했다. `display:none;`
2. 스크롤을 내리든 홀리든 계속해서 고정되어있는 상태인 `position : fixed` 를 사용했다.
3. 크기가 반응형으로 유지되기 위해 크기 단위를 `vw`를 사용했다. `vh`를 쓰면 모바일 같은 경우, 하단부에 브라우저 nav bar가 드러나, 이에 영향받아 그 크기가 줄었다 늘었다 정신없어진다.


## 결론

한 1시간 30분정도 걸렸나?
생각보다 css를 만지는 시간이 오래 걸렸다.
그리고 liquid에서 elsif 조건문을 어떤 식으로 구현해내야하는지 구글링해가면서
걸리는 시간도 존재했다.

그래도, 이렇게 사이드바에 걸어놓으면 수익이 늘어난다고 하니
어찌될지는 지켜볼 일이다.
