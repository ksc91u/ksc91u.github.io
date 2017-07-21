Title: OneSky Sucks
Date: 2017-07-21 13:00
Modified: 2017-07-21 13:00
Category: i18n
Tags: onesky
Slug: onesky
Authors: Me
Summary: OneSky CDATA 的一堆雷

OneSky 真雷

上面的字串

	<font color="#F06354">*</font> 為必填欄位
	姓名 <font color="#F06354">*</font>
	
下載格式選Android Xml , 很聰明, 自動幫我加CDATA

	&lt;font color=\"#F06354\"&gt;*&lt;/font&gt; 為必填欄位
	<![CDATA[姓名 <font color="#F06354">*</font>]]>
	
馬的為什麼第一個字串就不會加。

一開始看到這個想說, 好, 那所有有html 的我都手動加上 CDATA 好了吧, 結果...

<b>We've encountered a problem when generating the file. Our engineering team will look into the issue and get back to you soon!</b>

[可能的原因1](https://support.oneskyapp.com/hc/en-us/articles/115001927147-I-cannot-export-my-file-from-OneSky)

[也可能是這樣](https://support.oneskyapp.com/hc/en-us/articles/222717448-Common-import-export-issues)

但是 Sorry~ 錯誤訊息不會告訴你

我是剛好可以下載 xliff xml 格式, 之後丟上去 [這裏](https://localise.biz/free/converter/ios-to-android) 他才告訴我說哪一行錯了, 才發現

<b>你手動加了CDATA, OneSky 又幫你加一次, 然後就說錯了不讓你下載了</b>

結論

1. OneSky 會自動幫你加 CDATA
2. 但是有的該加的不加
3. 不該加的幫你加了 
4. 錯了不會告訴你原因