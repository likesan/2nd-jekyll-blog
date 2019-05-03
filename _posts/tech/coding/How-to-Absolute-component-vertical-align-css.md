---
layout: post
title : How to Absolute displayed Component get to be middle in vertical align?
category : css
comments: true
date : 2018-12-22
thumbnail : "https://document-export.canva.com/DADT4VouGWY/21/thumbnail/0001-1417000423.png"

---


1. [How to center a “position: absolute” element](https://stackoverflow.com/questions/8508275/how-to-center-a-position-absolute-element)

Add below block,

```css
position:absolute;
top:50%;
left:50%;
transition:translate(-50%,-50%)
```


But what is the `translate(-50%, -50%)`?

[This means](https://stackoverflow.com/questions/46184458/transform-translate-50-50/), 
`move me leftwards by 50% of my width, along the x-axis, and`
`move me upwards by 50% of my height, along the y-axis`

