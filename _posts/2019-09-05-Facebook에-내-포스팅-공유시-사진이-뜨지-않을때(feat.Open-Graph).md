---
layout : post
category : [Facebook, Open Graph, SEO, Marketing, Blogging]
commnets : true
thumbnail : https://images.unsplash.com/photo-1526498460520-4c246339dccb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80 
---

* TOC
{:toc}

# Facebook에 내 포스팅을 공유해도 Img가 나타나지 않을때

## 문제화면

![Facebook-링크-등록시-아무런-사진도-안뜰때](https://user-images.githubusercontent.com/35059428/64408123-9393af00-d0b8-11e9-9080-f35f8b55fb8d.png)

## 원인

`<meta property='og:img'>` 가 설정되어있지 않아서 일어났던 문제.

## 해결방법

```html
<meta property="og:type" content="website">
<meta property="og:title" content="{% if page.title %}{{ page.title }}{% endif %}">
<meta property="og:description" content="{% if page.content %}{{ page.content | markdownify | strip_html  | truncatewords: 15 }}{%endif%}">
<meta property="og:url:secure" content="{{ site.url }}">
<meta property="og:img:secure" content="{% if page.thumbnail %}{{ page.thumbnail }}{% endif %}">
```


## 시행착오

gitpage에서 meta tag 수정시

` page.thumbnail ` 혹은 ` page.title `로 접근해야지
post.thumbnail 또는 post.title로 접근하면 인식하지 못한다.


## 결과 