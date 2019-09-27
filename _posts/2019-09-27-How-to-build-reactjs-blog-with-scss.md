---
layout : post
category : Coding
comments : true
tags : [ReactJs, SCSS, Front-End, Blog]
thumbnail : https://images.unsplash.com/photo-1536859355448-76f92ebdc33d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80
---

* TOC
{:toc}

# I wanna build a gatsby blog or react blog. 

![reactblogsome](https://images.unsplash.com/photo-1536859355448-76f92ebdc33d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)
people would mind that is like a 'starting from scratch'
but... I need to know how to make it.
at the same time, I need pretty good result.
yeah What I need is understanding reactJS, not only Gatsby.
ReactJS is more generally used for front end coding.
SCSS is the thing that I need as well.
because that's far faster than any other skill.
I've already used with CSS however, that was very confusing and many caring needed.
I don't want to do that..

this is very good article to understand about ReactJS + SCSS.
That requires a webpack as well.

## Why?

![og metatags doesn't work with jekyll](https://user-images.githubusercontent.com/35059428/64468825-a3b09a80-d15b-11e9-8473-aac35a819fc2.png)

I've managed a blog for a half of year. I used gitpage with just jekyll. However there is a problem. That doesn't allow to OG tags dynamically acknowledge the post's title or image card.
I've tried this on Facebook 2 weeks ago, but simply it doesn't work.
The liquid tags come out.

only static picture can be set on posting. **Jekyll is limited.**


## Good resources for scratching the ReactJS blog

### [Basic usage of ReactJS with SCSS](https://medium.com/@jsh901220/react%EC%97%90-scss-%EC%A0%81%EC%9A%A9%EB%B0%8F-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-1-c7bd2895f5a6)

1. need to create React JS app `create-react-app name`
2. `SCSS` is most generally used preprocess css. 
3. need to command `yarn eject` in the folder.
4. need to modify `webpack.config.dev.js` and `webpack.config.prod.js`
5. before modification of them, need to add `yarn add node-sass sass-loader`
6. need to modify `test: /\.css&/` to `test: /\.(css|scss)$/,` to allow recognize scss at 160 line. 
7. at 170 line, change like this
   ```
    {                
    loader: require.resolve("sass-loader"),                
        options: {         
            sourceMap: true                
        }              
    }
   ```

### [Where is the best hosting platform for my ReactJS blog?](https://blog.bitsrc.io/8-react-application-deployment-and-hosting-options-for-2019-ab4d668309fd)

heroku, gitpage, netify... the matter what I've acknowledged is... as much as I build, I can deploy on the many platform.

and another issue is... 

### How can I make the all my previous markdown files to be read in ReactJS blog?

[I found a resource to solve my concern.](https://medium.com/@shawnstern/importing-multiple-markdown-files-into-a-react-component-with-webpack-7548559fce6f) That article explains how to render a directory which is full of markdown files. 

