# JikkyoAlways_for_YouTube

YouTubeLive のチャットを某動画サイト風にオーバーレイします.  
これにより YouTube で視線をチャット欄に動かさずに動画を見ながらチャットを見ることができます.

![example.gif](https://github.com/T3aHat/JikkyoAlways_for_YouTube/blob/master/image/example.gif)

# 推奨環境

Windows10-64bit  
YouTube Data API v3  
(JIkkyoAlways_for_YouTube.py 編集は Python3.7)

# 利用方法

- https://console.cloud.google.com で YouTube Data API v3 を有効化
- Windows 環境で[JikkyoAlways_for_YouTube.exe](https://github.com/T3aHat/JikkyoAlways_for_YouTube/raw/master/JikkyoAlways_for_YouTube.exe)をダウンロード.なお,信頼できないサイトから DL した exe ファイルを実行する際は"十分"注意してください.

  # 機能及び変数紹介

## `ctrl+s`

![settings.png](https://github.com/T3aHat/JikkyoAlways_for_YouTube/blob/master/image/settings.png)

- `bold`  
  コメントを太字にする.
- `num of comments`  
  一度に流れるコメント数.
- `fontsize`  
  フォントサイズ.`rec`とすると,画面に合うフォントサイズになる(仕様は`JikkyoAlways.py`を参照)
- `maximum length of comment`
  コメントの長さ.n 文字よりも長いツイートを流れないようにする.
- `velocity`  
  コメントの流れる速度.
- `acceleration`  
  コメントの加速度.長いコメントを速く流せる.  
  コメントの速さ=`velocity+len(コメント)*acceleration`
- `colour`  
  コメントのフォントカラー. http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter にある`COLORS`で定義された colour name,もしくは`#`に続けて 8bit で RGB 指定可能.(ex.`red`は`#FF0000`に同じ)
- `duration`  
  YoutubeAPIv3 でチャットを取得する周期(ミリ秒).1000ms よりも小さな値が入力された場合は API を過剰に叩いて即使用料上限に到達するのを防ぐために 1000ms に設定されます.  
  2020/06/15 現在で YouTube Data API をユーザーが新規登録した場合の一日あたりの API 使用量（クォータ）の上限は 10000 で,一度の取得で **おおよそ** 8 回 API を叩いています.
- `transparency`  
  コメントの透明度．ウィンドウが見えなくならないよう透明度の下限を 0.1(10)とした．
- Default  
  各種変数をデフォルトに戻す.
- Apply  
  変数の変更を適用.なお,`fontsize`に"hoge"など型エラーを起こすものを入れるとエラーになる.  
  そこら辺のデバッグはしていないので,察して使用してください...

## `Ctrl+f`

フルスクリーンにする.フルスクリーン時は,フルスクリーンを解除する.

# 田所あずさの純真 Always はいいぞ

https://www.youtube.com/watch?v=sBy76SY6zoQ
