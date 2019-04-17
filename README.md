# All in One #

## markdown style ##

### time ###
* mtime:最後更新時間(number).
* ctime:創立的時間(number).
* dtime:預計刪除時間(number), 後面會有刪除的原因(utf8), find first ", ".

### rating ###
* number

### type ###
* file
  * md
    * imd, index.md
* link
* dir
  * pdir, package.dir

### [檔名] ###
* charset, utf8, find first [, reverse find first ](

### (檔案路徑或者連結) ###
* charset, utf8, reverse find first ](, reverse find first ), 不包含字串("](")
 
### tag ###
* charset, ascii

### to ###
* 下次再次使用的情境(utf8, 不包含(", ")), find first ", " 

### from ###
* ref(utf8, 不包含(", ")), reverse find first "."

## sample ##

### file ###
* \#mtime:20190416, \#rating:10, \#type:file. [sample](sample.txt)
  * \#index, \#test.
  * \#to:資料夾的index(索引), \#from:自己創立. 
  * \#ctime:20190416, \#dtime:99999999, 資料過時或不用就可以刪除.

### md ###
* \#mtime:20190416, \#rating:10, \#type:md. [index](index.md)
  * \#index.
  * \#to:說明資料, \#from:自己創立. 
  * \#ctime:20190402, \#dtime:99999999, 資料過時或不用就可以刪除.

### imd ###
* \#mtime:20190416, \#rating:10, \#type:imd. [index](index.md)
  * \#index.
  * \#to:為了什麼建立的.
  * \#ctime:20190402.

* 不用 from
  * 因為是自己寫的結果 
* 不用 dtime
  * dtime 其他資料都消逝就可以刪除了.
* 會進行 parser, index.md 預設就會 parse(不要 parse 兩次)
* 某程度來說是為了 link group.

### link ###
* \#mtime:20190416, \#rating:10, \#type:link. [google](https://www.google.com)
  * \#google.
  * \#to:資料夾的index(索引), \#from:. 
  * \#ctime:20190402, \#dtime:99999999, 資料過時或不用就可以刪除.
  
### dir ###
* \#mtime:20190416, \#rating:10, \#type:dir. [sampleDir](sampleDir)
  * \#index.

* 自動讀取底下的 index.md 
* 不用 to 和 from
  * 因為是 group 的結果
* 不用 ctime 和 dtime
  * dtime 其他資料都消逝就可以刪除了.

### pdir ###
* \#mtime:20190416, \#rating:10, \#type:pdir. [samplePDir](samplePDir)
  * \#index.
  * \#to:為了什麼把東西都放在同一個資料夾.
 
* 不用 ctime 和 dtime
  * dtime 其他資料都消逝就可以刪除了.
