---
layout : post
category : [Python, Instagram, Coding, Growthhacking]
comments : true
---

* TOC
{:toc}


How I get the accesstoken from My instagram account, through Python-instagram?

# Requirements

1. Python 2/3
2. GitKraken(recommend) 


# Sequence

1. Fork [Python Instagram API](https://github.com/vgavro/python-instagram)

2. Clone in Local Env through GitKraken

3. Process the `python get_access_token.py` 

    ```
    Client ID: 
    Client Secret: 
    Redirect URI: 
    Requested scope (separated by spaces, blank for just basic read):
    Visit this page and authorize access in your browser: 

    access token:
    ```

4. Type all required information with [Instagram Development page](https://instagram.com/developer)


## Error solution

[When 'Client ID must offered' message out, though right Client ID typed.](https://github.com/vgavro/python-instagram/commit/9dfc264571ad7c343af3899445d13afedf23e3aa)
