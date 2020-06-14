# JikkyoAlways_for_YouTube  
YouTubeLiveのチャットを某動画サイト風にオーバーレイします.  
これでYouTubeで動画を見ながら視線を変えずにチャットを見ることができます.  
  
# 推奨環境  
Windows10-64bit  
YouTube Data API v3  
(JIkkyoAlways_for_YouTube.py編集はPython3.7)  
  
# 利用方法  
* https://console.cloud.google.com でYouTube Data API v3を有効化  
* Windows環境で[JikkyoAlways_for_YouTube.exe](https://github.com/T3aHat/JikkyoAlways_for_YouTube/raw/master/JikkyoAlways_for_YouTube.exe)をダウンロード.なお,信頼できないサイトからDLしたexeファイルを実行する際は"十分"注意してください.  
  
  # 機能及び変数紹介  
## `ctrl+s`  
![settings.png](https://github.com/T3aHat/JikkyoAlways_for_YouTube/blob/master/image/settings.png)  
* `bold`  
コメントを太字にする.  
* `num of comments`  
一度に流れるコメント数.  
* `fontsize`  
フォントサイズ.`rec`とすると,画面に合うフォントサイズになる(仕様は`JikkyoAlways.py`を参照)  
* `maximum length of comment` 
コメントの長さ.n文字よりも長いツイートを流れないようにする.  
* `velocity`  
コメントの流れる速度.  
* `acceleration`  
コメントの加速度.長いコメントを速く流せる.  
コメントの速さ=`velocity+len(コメント)*acceleration`  
* `colour`  
コメントのフォントカラー. http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter にある`COLORS`で定義されたcolour name,もしくは`#`に続けて8bitでRGB指定可能.(ex.`red`は`#FF0000`に同じ)  
* `duration`  
YoutubeAPIv3でチャットを取得する周期(ミリ秒).1000msよりも小さな値が入力された場合はAPIを過剰に叩いて即使用料上限に到達するのを防ぐために1000msに設定されます.  
2020/06/15現在でYouTube Data APIをユーザーが新規登録した場合の一日あたりのAPI使用量（クォータ）の上限は10000で,一度の取得で __おおよそ__ 8回APIを叩いています.    

* Default  
各種変数をデフォルトに戻す.
* Apply  
変数の変更を適用.なお,`fontsize`に"hoge"など型エラーを起こすものを入れるとエラーになる.  
そこら辺のデバッグはしていないので,察して使用してください...  
  
## `Ctrl+t`  
![tweet.png](https://github.com/T3aHat/JikkyoAlways/blob/master/image/tweet.png)   
テキストボックスにツイートしたいテキストを入力して`Tweet`ボタンを押すと，API認証しているアカウントからツイート.また，TweetDeck同様`ctrl+Enter`でもツイートできます．    
正常にツイートできるとテキストボックスの文字が消えます.  
失敗した場合はエラーコードがテキストボックスに表示されます.  
* `append Search Word`  
オンにすると,テキストボックス内のテキストの末尾に改行(`\n`)と検索ワードを追加してツイート．ハッシュタグを追っているときに便利.  
 ## `Ctrl+f` 
フルスクリーンにする.フルスクリーン時は,フルスクリーンを解除する.  
    
# 田所あずさの純真Alwaysはいいぞ  
https://www.youtube.com/watch?v=sBy76SY6zoQ  