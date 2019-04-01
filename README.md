# DjangoFirstPrj
Python DjangoでPostなどができるプロジェクト

## セットアップの参考サイト

* [pythonのインストール（Mac）](https://qiita.com/okhrn/items/935cf187aec5cf144558)
* [MacOSとHomebrewとpyenvで快適python環境を。](https://qiita.com/crankcube@github/items/15f06b32ec56736fc43a)
* [[MacOS Mojave]pyenvでpythonのインストールがzlibエラーで失敗した時の対応](https://qiita.com/zreactor/items/c3fd04417e0d61af0afe)
* [virtualenvでpython環境を管理する](https://qiita.com/caad1229/items/325ca5c8ad198b0ebce7)

## プロジェクトの作成

Gitからクローンしたディレクトリーでターミナルを開いて下記コマンドを実行し仮想環境を作成する

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

次にプロジェクトを作成
```
$ pip install django==2.0.4 djangorestframework==3.8.2 channels==2.1.0
$ django-admin startproject realtimechatserver
```

