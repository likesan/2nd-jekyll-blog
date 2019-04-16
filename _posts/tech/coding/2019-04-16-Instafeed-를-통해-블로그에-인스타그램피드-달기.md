
좀 더 눈에 띄는 Landingpage를 만들기 위해,
[`Instafeed.js`](http://instafeedjs.com/)를 쓰기로 했다.
블로그를 새로 만들 때마다 다는 녀석.

CDN 이 있을 줄 알았더니, Local에 설치를 해줘야만 된다.

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

    2) Accesstoken
        
        인터넷 url 에 `https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code` 로 접속해서 들어가보자. 
        Parameter 값으로 `CLIENT-ID`와 해당 FEED를 사용할 `redirect-uri`을 적어주어야한다.

그러면 떠오른 URI 값이 parameter에 나타난다.

![accesstoken-instagram-feed](https://user-images.githubusercontent.com/35059428/56182735-0e92f500-6046-11e9-892b-22036a983e42.png)


