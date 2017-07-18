Title: Pelican GitHub Pages
Date: 2017-07-18 10:40
Modified: 2017-07-18 10:40
Category: pelican
Tags: pelican, github pages
Slug: my-super-post3
Authors: Me
Summary: Publish blog with pelican on GitHub pages

Pelican 的 make github 會把內容發布到 gh-pages 這個 branch。
但是 github 的個人 pages ( repo: username.github.io ) 會去找 master branch。

看[這裏](https://github.com/hexojs/hexo/issues/350)的討論

project pages 才會去找 gh-pages branch, 這樣網址就要變成  https://username.github.io/username.github.io  神長！

試試看在 develop 寫文章, publish 到 gh-pages 之後, master merge gh-pages 然後再 push 一次看看。

在找到解法之前先這樣。
