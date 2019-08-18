---
layout: post
comments : true
category : [Instabot, Python, Coding, Marketing, Instagram]
thumbnail :  https://images.pexels.com/photos/1020325/pexels-photo-1020325.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500
---
# Instabot.py Challenge requirement error fixing
Found the solution from Issue board in the repository.

But my trial had focused on [Newest Instabot-py](https://github.com/instabot-py/instabot.py/pull/1788).

1. Download python 3 
2. Upgrade newest Pip
3. instabot master.zip download ( you need to use the `example.py` from there)
4. [pip install python-telegram-handler 하기 ](https://github.com/instabot-py/instabot.py/issues/2133)

    ```
    1) install, pip install python-telegram-handler
    2) install telegram on my phone
    3) create a channel and getting token by the bad ass @BotFather
    4) getting my new bot id by the bad ass @get_id
    5) put the channel id and token on the yml config
    ```

5. `py -m pip install sqlalchemy`

6. Error occured. [The most helpful issue article was this.](https://github.com/instabot-py/instabot.py/issues/2333) The error log requires the instabot-py's upgrade
`python3 -m pip install instabot-py --upgrade`
 but the above command didn't work, with `python3`.
 So modified just as `py -m pip install instabot-py --upgrade`


    ![Instabot-py-challenge-required-solved](https://user-images.githubusercontent.com/35059428/62818143-834dea00-bb75-11e9-8c69-f37da86c3a04.png)

7. Done!