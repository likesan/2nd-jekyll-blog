


Today, finally I've tried to install Reactjs blog with SCSS.

First, the weird things that I've found from an article is different.
The article says that I need write `Yarn eject`
but the bash shows `NOTE: Create React App 2+ supports TypeScript, Sass, CSS Modules and more without ejecting: https://reactjs.org/blog/2018/10/01/create-react-app-v2.html`

So I've tried to read the webpage as well.

that webpage means, already 2+ version, there is no needed for `Yarn eject`.
but rather, I cannot go back if the command execute once.

and I wondered how to make the scss working on `create-react-app 2+`.
[Googling just shows up nice article](https://scotch.io/tutorials/using-sass-in-create-react-app-v2) about that.

According to the above article, I needed just drop a line on cmd.
`npm install node-sass -s`
I wondered what is `node-sass`.
and Below lines are their [public intro](https://www.npmjs.com/package/node-sass) about it.

```
Node-sass is a library that provides binding for Node.js to LibSass, the C version of the popular stylesheet preprocessor, Sass.

It allows you to natively compile .scss files to css at incredible speed and automatically via a connect middleware.
```

So 
I dropped a line `npm install node-sass -s` at the folder of React app installed.
But I was wondering why `node-sass` should be installed? not just `sass`?
So I've tried to look that up, ... but couldn't find out what is the relation between ReactJS and node module... so that I need look that up later.
but here I am for building a React blog not just mastering the knowledges.


and nextly I wondered where should I put my codes for making it likes a blog.
There are so many files in basic structure, rather I needed which file should I click and drop into there? so I've looked up the explanation of basic structure of ReactJs, and [found a good resource.](https://www.freecodecamp.org/news/quick-guide-to-understanding-and-creating-reactjs-apps-8457ee8f7123/#basic-folder-structure-explained)

App.js is the whole container to excute all react component.

