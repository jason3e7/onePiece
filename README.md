# All in One #

## markdown style ##

### time ###
* mtime:最後更新時間(number).

### rating ###
* number

### type ###
* file
  * md
    * imd, index.md
* dir
  * pdir, package.dir
* link
* groupIndex
  * simd, specialIndex.md
  * gimd, groupIndex.md

### [檔名] ###
* charset, utf8, find first [, reverse find first ](

### (檔案路徑或者連結) ###
* charset, utf8, reverse find first ](, reverse find first ), 不包含字串("](")
 
### tag ###
* charset, ascii

### to ###
* 下次再次使用的情境(utf8, 不包含(", ")), find first ", " 

## sample ##

### file ###
* \#rating:10, \#type:file, \#mtime:20190416. [sample](sample.txt)
  * \#sample, \#test.
  * \#to:資料夾的index(索引).

### md ###
* \#rating:10, \#type:md, \#mtime:20190416. [index](index.md)
  * \#sample.
  * \#to:說明資料.

### imd ###
* \#rating:10, \#type:imd, \#mtime:20190416. [index](index.md)
  * \#sample.

* 自動標 index 的 tag
* to 留空, 就是索引

#### feature 跨網域 ####
* 第二行是 json config, option
  * `config = JSON.parse('{"basePath":"/"}')`
  * sample, `+ config : '{"basePath":"/"}'`, 用加號作為 parse 的差異
  * 是 option, 一但有, 就是再 parseMD 更換 basepath.
  * 測試要複製一份放到另外一個網域

### dir ###
* \#rating:10, \#type:dir, \#mtime:20190416. [sampleDir](sampleDir)
  * \#sample.

* 自動讀取底下的 index.md 
* 不用 to
  * 因為是 group 的結果

### pdir ###
* \#rating:10, \#type:pdir, \#mtime:20190416. [samplePDir](samplePDir)
  * \#sample.
  * \#to:為了什麼把東西都放在同一個資料夾.

### link ###
* \#rating:10, \#type:link, \#mtime:20190416. [google](https://www.google.com)
  * \#google.
  * \#to:Search工具.

### group index ###
#### simd ####
* 特化的類型, 因為類型靠樣子去區分, 全都只有 resource
  * special
* 相同時間, 不同目的, 不同類型, 不同屬性
  * 因為時間相同, 多用於完成或封存或log
* 自動標 index 的 tag
* to 留空, 就是索引
* \#rating:20, \#mtime:20200602, \#type:simd. [index](index.md)
  * \#sample.

```
# 20200602 #
* \#rating:20, [google](https://www.google.com)
  * \#search
  * \#to:為了什麼建立的.
* \#rating:60, [Altoro Mutual](http://demo.testfire.net/)
  * \#video.
  * \#to:為了什麼建立的.
* \#rating:60, [dir](testdir/)
  * \#test.
  * \#to:為了什麼建立的.
* \#rating:60, [file](test.txt)
  * \#test.
  * \#to:為了什麼建立的.
* \#rating:60, [test](test.md)
  * \#test.
  * \#to:為了什麼建立的.
```

* 配套措施, 要能自動全部帶入一樣(目的, 類型, 屬性)
* 配套措施, 要能和imd互轉
* link, pdir, file, md, 依照特徵判斷
  * link, http, https
  * dir, /
  * md, .md
  * file, other

### gimd ###
* 時間, 目的, 類型, 屬性
* \#rating:20, \#mtime:20200602, \#type:gimd. [intent](intent.md)
  * \#sample.
  * \#to:為了什麼建立的.

```
# 20200602, 為了什麼建立的, \#type:link, \#tag1, \#tag2 #
* \#rating:20, [google](https://www.google.com)
* \#rating:60, [youTube](https://www.youtube.com/)
```
* 配套措施, 要能和imd互轉
* ftype
  * link, pdir, file, md 是比較單純的
  * imd, dir 要試一下

## 調整說明 ##
* 加入 group 的概念, 並刪掉多個欄位
  * 因為過往使用的時候, 花費很多時間, 故簡化之
  * groupIndex, 是"群組化索引"的概念, 本質還是索引
* 檢視上還是以時間為主, 但是因為不常改, 之後清單會採取自動產生, 所以用編輯上比較常改的 rating 為第一順位
  * 方便編輯上比較常改的 ftype 為第二順位
* 加上可以自定義 global file 前綴變數.
  * 因為不想要檔案和索引放在一起, 大檔問題
  * 影響特定資料夾的 file 前綴變數, 先開發限定一個就好.
  * md 也要能吃到

### 未來 ###
* groupIndex, 合成一個, 並可以任意欄位 group