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

`<meta property='og:image'>` 가 설정되어있지 않아서 일어났던 문제.

## 해결방법

1. [페이스북 디버깅 페이지](https://developers.facebook.com/tools/debug/sharing)서 해당 링크의 preview가 어떻게 나오는지 파악해본다.


2. og:image:url 과 og:image:secure_url 을 넣어준다.

    secure_url 은 https로 시작하는 링크를 위해 넣어준다. 참고한 [링크](https://www.joomshaper.com/forums/fix-facebook-provided-og-image-url-encountered-an-unknown-error)


```html
<!-- social image sharing -->
  <meta property="og:image:url" content="{{ site.thumbnail }}">
  <meta property="og:image:secure_url" content="{{ site.thumbnail }}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="600">
  <!-- social image sharing set end -->
```

3. _config.yml 에 thumbnail 부분을 따로 만들어, 다음 한줄을 넣어줬다.
```
thumbnail: https://user-images.githubusercontent.com/35059428/64468325-069f3300-d156-11e9-80ec-45e98bd19703.jpg
```


## 결과 

![succeded-with-og:image:url](https://user-images.githubusercontent.com/35059428/64468825-a3b09a80-d15b-11e9-8473-aac35a819fc2.png)

위 사진에서 처럼, Link Preview가 나타난다.

### 여전히 문제인점

위 사진 맨 밑에 보면

`% include epic.html %` 이라는 Liquid 가 나타날 뿐, Description이 불러와지지 않은 문제가 있다.

메타 태그가 해당 포스트의 title 부분이 불러와지기 전에, 로딩되어 나타나는 문제가 아닐까 유추 중... 계속 해결 중인 부분

