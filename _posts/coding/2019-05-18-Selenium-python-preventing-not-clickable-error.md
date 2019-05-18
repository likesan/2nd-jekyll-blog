---
layout : post
category : [Selenium, Instagram, Python, Coding]
comments : true
---

* TOC
{:toc}

To make a click in Selenium(Python)

# Solution 

## Need to scroll on the view which is the target element shows.

```python
Element.location_once_scrolled_into_view
Element.click()
```

## need maximize the browser window

it's better to open a browser within maximized size, not open and maximizing it in 2 steps.
    
```python
chrome_options.add_argument("--start-maximized")
```

