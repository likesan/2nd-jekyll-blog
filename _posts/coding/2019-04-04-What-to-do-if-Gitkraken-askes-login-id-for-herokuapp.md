---
layout: post
category: ["Coding","Git","Heroku"]
comments: true
---


It can be very embrassing but you can just solve it out by 2 commands


1. `heroku login`
you can figure out what is the login id

2. `heroku auth:token`
then it would be your password to access!!

```python
C:\Users\sjisy\OneDrive\Desktop\ellie-blog-project>cd djangoblog

C:\Users\sjisy\OneDrive\Desktop\ellie-blog-project\djangoblog>heroku login
heroku: Press any key to open up the browser to login or q to exit:
Logging in... done
Logged in as xxxxxxx@gmail.com

C:\Users\sjisy\OneDrive\Desktop\ellie-blog-project\djangoblog>heroku auth:token
 »   Warning: token will expire 12/11/2019
 »   Use heroku authorizations:create to generate a long-term token
1111-2221-333e-44444-555555555

C:\Users\sjisy\OneDrive\Desktop\ellie-blog-project\djangoblog>

C:\Users\sjisy\OneDrive\Desktop\ellie-blog-project\djangoblog>



```

