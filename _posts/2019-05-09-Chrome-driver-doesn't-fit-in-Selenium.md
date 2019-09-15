---
layout : post
category : coding
tags : [selenium, chrome, coding]
comments : true
thumbnail : https://user-images.githubusercontent.com/35059428/64475517-4eee3d80-d1b6-11e9-9974-be484e3b80b5.png
---

# Problem
When chrome Version doesn't fit your selenium required driver

As Selenium doens't work if selenium webdriver version doesn't fit with your installed chrome driver,
download from [Chrome Driver Download page](https://sites.google.com/a/chromium.org/chromedriver/downloads) 


# How to check

in my case, I **set the code to print the error message** in the `Try, Exception` , then the driver version automatically appears out.

```py
except Exception, e:
        print 'type is:', e.__class__.__name__
        print_exc()
```

# Outlook

The outlook is likes below

```cmd
  (Session info: chrome=74.0.3729.131)
  (Driver info: chromedriver=74.0.3729.6 (255758eccf3d244491b8a1317aa76e1ce10d57e9-refs/branch-heads/3729@{#29}),platform=Windows NT 10.0.17134 x86_64)
```