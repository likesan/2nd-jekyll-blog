---
layout: post
tags : instagram marketing instafeed.js
comments: true
---


# Instagram의 API 정책이 바뀐 뒤로, 안됨.


기껏 3-4시간 투자해서 해놨더니,
계속해서 다음과 같은 에러가 계속해서 났다.

```console
Uncaught Error: Error from Instagram: invalid media id
```

AccessToken을 서버사이드로 받았었고,
Manage Account에서 Disable Oauth Implicit, Enforce to Require Login 등도 다 만져봤었지만...

[안되는 이유](https://github.com/stevenschobert/instafeed.js)가 있었다.
밑의 내용은, Instafeed.js 개발자 Readme.md 서 발췌

```
 IMPORTANT! Instagram is changing the API that Instafeed.js depends on.
Before you decide to use instafeed.js, be aware that Instagram is shutting down the API platform that enables instafeed to work. As of now, instafeed.js works for some common uses (eg. embedding a single user's feed on a web page), but can't work for more complex uses (eg. retrieving all public images with a particular hashtag, finding posts based on a location, etc).
The platform API will be turned off completely in 2020, which means that instafeed.js in its current form will stop working then.
```

```
중요사항! 인스타그램이 Instafeed.js과 관련된 API를 바꾸고 있습니다.
Instafeed.js를 쓰기 전에, Instagram 측에서 Instafeed.js 가 작동하지 못하게 하고 있다는 사실을 알아두세요. 

지금은, 개인의 피드를 웹사이트에 올리는 정도의 일반적인 작업만 가능하지만, 모든 사진을 불러오거나, 특정 헤시태그의 사진만을 불러오거나, 위치를 통해 알아내는 것들은 불가능합니다.

2020년부터는  API Platform 측에서 Instafeed.js가 완전히 사용되지 못하도록 조치할 예정입니다.
```


# 이 부분부터는 적용 방법


좀 더 눈에 띄는 Landingpage를 만들기 위해,
[`Instafeed.js`](http://instafeedjs.com/)를 쓰기로 했다.
블로그를 새로 만들 때마다 다는 녀석.

CDN 이 있을 줄 알았더니, Local에 설치를 해줘야만 된다.

## 순서

1. `Yarn add instafeed.js`

2. CDN `<head></head>` 안에 붙이기

    밑의 두 개 중 하나를 골라쓰자. 축소버전.

```
https://cdnjs.cloudflare.com/ajax/libs/instafeed.js/1.4.1/instafeed.min.js
```

```
https://matthewelsom.com/assets/js/libs/instafeed.min.js
```
3. 내 인스타그램의 accesstoken과 client ID를 찾아넣기

https://instagram.com/developer

로 들어가 내 Accesstoken과 Client ID를 얻을 수 있다.
(insight 통계자료도 여기서 얻을 수 있을랑가 모르겠다. 이거 이 후에 인스타그램 통계자료를 아예 떼올까 싶다.)

    1) Client ID 는 `Manage Account` 버튼을 클릭하면 나타난다.

    2) Server side를 이용해 AccessToken을 얻어내기

```
curl -F 'client_id=[clientID]' -F 'client_secret=[clientSecret]' -F 'grant_type=authorization_code' -F 'redirect_uri=[redirectURI]' -F 'code=[code]' https://api.instagram.com/oauth/access_token

```

    중요한건, 대괄호 `[..]` 부분을 없애야 된다는 점.

![accesstoken-instagram-gitbash](https://user-images.githubusercontent.com/35059428/56186886-87e51480-6053-11e9-8e80-c3c4feb15bee.png)

    
    3) 해당 Accesstoken을 사용할 수 있도록 Instagram 측에서 허락을 받자

    https://api.instagram.com/v1/users/self/?access_token=`ACCESS-TOKEN`

    위 `ACCESS-TOKEN` 부분에, 2번에서 알아낸 AccessToken을 복붙해넣자.





# 참고

[Sample Instagram Feed with Instafeed.js by Matthew Elsom](https://codepen.io/matthewelsom/pen/zrrrLN)

[instafeed.js: The access_token provided is invalid](https://stackoverflow.com/questions/37675155/instafeed-js-the-access-token-provided-is-invalid#answer-37675277)


# 별첨

## Accesstoken 

instagram.com/developer 사이트의 방식대로 시도해보았으나, Accesstoken 받아지지 않았음.       
       
인터넷 url 에 `https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code` 로 접속해서 들어가보자. 

Parameter 값으로 `CLIENT-ID`와 해당 FEED를 사용할 `redirect-uri`을 적어주어야한다. 
그러면 떠오른 URI 값이 parameter에 나타난다. 
       
![accesstoken-instagram-feed](https://user-images.githubusercontent.com/35059428/56182735-0e92f500-6046-11e9-892b-22036a983e42.png)

