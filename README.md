Call option price(Black-Scholes model) API
======================
ブラック・ショールズモデルで計算したコール・オプション価格を返却するweb API.

使い方(api_bs.py)
--------------------------------- 
例えば
* 初期株価(s0):100
* ストライク(k):100
* オプション満期(年、T):5
* 無リスク金利(/年,r):0.1
* ボラティリティ(/年,vol):0.3
というパラメターのオプション価格を計算したい場合は

`http://127.0.0.1:5000/bs_api?s0=100&k=100&T=5&r=0.1&vol=0.3`

というクエリを投げる（デフォルト設定）

その他のファイル
----------------------------------
その他のファイルはdotcloudにデプロイして使用する際に必要となるファイル。

