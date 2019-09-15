---
layout : post
category : coding
tags : [coding, jekyll, mermaid, diagram]
comments : true
thumbnail : https://user-images.githubusercontent.com/35059428/64475462-c374ac80-d1b5-11e9-8e94-639302d6dbd4.png
---

* TOC
{:toc}

# Summary

<div class="mermaid">
graph LR
head-tags-->Jekyll-Mermaid;
gem-install-`jekyll-mermaid`-on-CMD-->Jekyll-Mermaid;
add-`_config.yml`-a-line-->Jekyll-Mermaid;
add-`gem-'Jekyll-Mermaid'-on-Gemfile-->Jekyll-Mermaid;

</div>

# Sequences

1. `gem install jekyll-mermaid`

    ```ruby
    Successfully installed jekyll-mermaid-1.0.0
    Parsing documentation for jekyll-mermaid-1.0.0
    Done installing documentation for jekyll-mermaid after 1 seconds
    1 gem installed
    ```

2. add `_config.yml`

    ```ruby
    plugin : 
        - [jekyll-mermaid]
    ```

    more options [here](https://github.com/knsv/mermaid/wiki)



3. after that I've tried like to server on. but got below messages.

    ```ruby
    $ jekyll serve
    Configuration file: C:/wholesome-sj.github.io/_config.yml
    Dependency Error: Yikes! It looks like you don't have jekyll-mermaid or one of its dependencies installed. In order to use Jekyll as currently configured, you'll need to install this gem. The full error message from Ruby is: 'cannot load such file -- jekyll-mermaid' If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/! 
    ```

4. so added a line `gem 'jekyll-mermaid'` on `Gemfile`

    but still nothing work with below two code styles,

    ```html
    <pre><code class="language-mermaid">graph LR
    A--&gt;B
    </code></pre>
    ```

    this one only works on VScode preview.
    ```mermaid
    graph TD;
        Mermaid-Diagram-->Jekyll;
        Coding-->Jekyll
    ```

5. so look up to the issue page of mermaid with keyword `jekyll`

    then I found [a thread](https://github.com/knsv/mermaid/issues/772#discussion_bucket).

    then tried to paste `yk-liu's scripts into my <head> tags`

    ```html
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.0.0/mermaid.min.js"></script>
        </head>

    <body>

    <div class="mermaid">graph LR
    A--&gt;B
    </div>
        
    </body>
    <script>
    var config = {
        startOnLoad:true,
        theme: 'forest',
        flowchart:{
                useMaxWidth:false,
                htmlLabels:true
            }
    };
    mermaid.initialize(config);
    window.mermaid.init(undefined, document.querySelectorAll('.language-mermaid'));
    </script>
    ```

    then it's working perfectly :D

# References

1. [Mermaid Jekyll Repository](https://github.com/knsv/mermaid)

