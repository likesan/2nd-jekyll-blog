---
layout: post
category : Coding
tags : [Jekyll, Hexo, Node.js, React, Javascript, Blog]
thumbnail : https://images.unsplash.com/photo-1485856407642-7f9ba0268b51?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80
---


# Jekyll 에서 Hexo로 이사한 후기

## Jekyll에서는 Open graph태그를 Social Platform서 불러읽어들이지 못하는 문제를 보였다.
바로 **Og:image meta**태그를 Facebook에서 긁어내면 
```
{ % include ----.html % }
``` 
과 같이 liquid가 나타나는 에러였다.

## 이게 가장 큰 요인이 됐다.
LinkedIn에서 나온 다른 분의 github.io 테크블로그는
같은 깃블로그인데도 Hexo로 만들어서 인지 Og:image 태그를 다이나믹하게 페이스북으로
끌어오는데 문제가 없어보였다.

## Node.js로 돌아가는 Hexo는 ReactJS를 연습하고 싶어하는 나 

그리고 한 가지 더, ReactJs 든 Node.js든 결국 Javascript 친화적인 언어들이니. 도움이 될거라 생각했다. 난 ReactJS를 잘하고 싶으니까.

## Renamer로 모든 마크다운 파일 제목의 '-'을 벗겨냈다.

![renamer-strip-out-hyphen](https://user-images.githubusercontent.com/35059428/64538678-a247c380-d34f-11e9-8a4d-2987457f2740.png)

## Hexo에서는 마크다운에 들어있는 Table of Content, 즉 목차들을 인식하지 못했다.
`*TOC {:toc}`
라고 되어있는 이 부분들 지워내야했다.

이를 위해선 Sed를 써서, md 파일 내에 있는 저 마크다운 명시부분만 삭제 하거나 Find and replace 도구를 다운 받아 사용해야했다.

그런데 이 Sed는 파일에 하이픈이 달려있으면 인식하지 못하는 오류를 가졌다.

선행적으로 Renamer를 써서 제목 내에 있는 모든 하이픈을 벗겨내야했다.

## 제목 내의 모든 하이픈을 벗겨내기 위한 Renamer 설치 방법 

`$ npm install -g renamer`

자세한 사용방법은 [Renamer Gitdoc](https://github.com/75lb/renamer)에서 확인해보자

하이픈 없애는 명령어 `renamer -d --find "/-/g" --replace "_" *`


## sed 없이 Find and replace 도구만으로 파일 내 특정 텍스트를 바꾸는 방법

![find-and-replace-사용기](https://user-images.githubusercontent.com/35059428/64540265-7da11b00-d352-11e9-9890-61d7c114ae20.gif)
