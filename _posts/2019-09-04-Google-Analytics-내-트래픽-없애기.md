---
layout: post
comments : true 
category : coding 
tags : [ Coding, Google Analytics, Inner Traffic, filtering]
thumbnail : https://images.unsplash.com/photo-1560472354-b33ff0c44a43?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1120&q=80
---

* TOC
{:toc}

Google Analytics 에서 
내 트래픽 없애기

# 굉장히 복잡하게 이것 저것을 시도해봤다.
무슨 Filter에서 Exclude 들어가서는, Regular Expression(레겍스)를 써가며 198.168.1.1 등등을 시도했으나

# 그냥 크롬 앱 다운 받으면 끝남

[그냥 크롬 앱을 하나 다운](https://chrome.google.com/webstore/detail/google-analytics-opt-out/fllaojicojecljbmefodhfapmkghcbnh?hl=ko) 받아쓰면 되는거였다.

너무 쉬워서, 내 자신이 하찮아질 정도...

# 이걸 알아낸 덕분에 1 시간 소모 되던 시간을 멈출 수 있었다.

구글링을 통해 `How to filtering Dynamic innertraffic` 등으로 계속 검색하다, 한 [Stackoverflow 답변](https://stackoverflow.com/questions/621200/how-to-filter-myself-out-of-google-analytics-with-a-dynamic-ip-address/6028459#answer-6028459)서 알아낼 수 있었다.

