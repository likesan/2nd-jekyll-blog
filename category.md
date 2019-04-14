---
layout: default
permalink : /category/
---

<div>
    {% for category in site.categories %}
    <div class="post-preview">
        <a href="/category/{{ category[0] }}/"
            style="text-decoration: none;">{% if category[0] == 'aws' %}
            {{ category[0] | upcase }}
            {% else %}
            {{ category[0] | capitalize }}
            {% endif %}
        </a>
            <br />    
    </div>
    <hr>
    {% endfor %}
</div>