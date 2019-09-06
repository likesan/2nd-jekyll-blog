---
layout : post
category : [Jekyll, Blogging, Error, Gem, Ruby]
comments : true
thumbnail : https://images.unsplash.com/photo-1543285198-3af15c4592ce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=967&q=80
---

* TOC
{:toc}

Jekyll Gem file Errors

I met so many errors like this,

# What was the errors?

```ruby
c:\wholesome-sj.github.io>jekyll serve
Traceback (most recent call last):
        10: from C:/Ruby25-x64/bin/jekyll:23:in `<main>'
         9: from C:/Ruby25-x64/bin/jekyll:23:in `load'
         8: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/jekyll-3.8.6/exe/jekyll:11:in `<top (required)>'
         7: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/jekyll-3.8.6/lib/jekyll/plugin_manager.rb:50:in `require_from_bundler'
         6: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler.rb:107:in `setup'
         5: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `setup'
         4: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `map'
         3: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
         2: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
         1: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:31:in `block in setup'
C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:319:in `check_for_activated_spec!': You have already activated liquid 4.0.3, but your Gemfile requires liquid 4.0.0. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)

c:\wholesome-sj.github.io>gem uninstall liquid

Select gem to uninstall:
 1. liquid-4.0.0
 2. liquid-4.0.3
 3. All versions
> 2
Successfully uninstalled liquid-4.0.3

c:\wholesome-sj.github.io>jekyll serve
Traceback (most recent call last):
        10: from C:/Ruby25-x64/bin/jekyll:23:in `<main>'
         9: from C:/Ruby25-x64/bin/jekyll:23:in `load'
         8: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/jekyll-3.8.6/exe/jekyll:11:in `<top (required)>'
         7: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/jekyll-3.8.6/lib/jekyll/plugin_manager.rb:50:in `require_from_bundler'
         6: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler.rb:107:in `setup'
         5: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `setup'
         4: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `map'
         3: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
         2: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
         1: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:31:in `block in setup'
C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:319:in `check_for_activated_spec!': You have already activated rouge 3.6.0, but your Gemfile requires rouge 2.2.1. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)

c:\wholesome-sj.github.io>gem uninstall rouge

Select gem to uninstall:
 1. rouge-2.2.1
 2. rouge-3.6.0
 3. All versions
> 2
Successfully uninstalled rouge-3.6.0

c:\wholesome-sj.github.io>jekyll serve
Traceback (most recent call last):
        10: from C:/Ruby25-x64/bin/jekyll:23:in `<main>'
         9: from C:/Ruby25-x64/bin/jekyll:23:in `load'
         8: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/jekyll-3.8.6/exe/jekyll:11:in `<top (required)>'
         7: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/jekyll-3.8.6/lib/jekyll/plugin_manager.rb:50:in `require_from_bundler'
         6: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler.rb:107:in `setup'
         5: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `setup'
         4: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:26:in `map'
         3: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
         2: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/spec_set.rb:148:in `each'
         1: from C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:31:in `block in setup'
C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/bundler-2.0.2/lib/bundler/runtime.rb:319:in `check_for_activated_spec!': You have already activated jekyll 3.8.6, but your Gemfile requires jekyll 3.8.5. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)

```
These were the version errors.

# How to solve? 

So simply I put the `gem uninstall [---]`

then it came out the duplicated versions of Gems! 
Then I removed unrequired gems, then it leaded to work!

So Simple!