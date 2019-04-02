# Hello World
[はじめての Django アプリ作成、その 1](https://docs.djangoproject.com/ja/2.0/intro/tutorial01/)を模写

## 作成手順
Step1.[Polls アプリケーションをつくる](https://docs.djangoproject.com/ja/2.0/intro/tutorial01/#creating-the-polls-app)  
Step2.[はじめてのビュー作成](https://docs.djangoproject.com/ja/2.0/intro/tutorial01/#write-your-first-view)

## 動作チェック

http://127.0.0.1:8000/polls/ を開く`Hello , world. You're at the polls index.`と表示される

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
$ django-admin startproject [ProjectName]
```

### プロジェクトの作成-参考サイト
* [Djangoプロジェクトの作成](https://www.python-izm.com/web/django/django_project/)
* [Building A Real-Time iOS Chat Application With Django](http://lucasjackson.io/realtime-ios-chat-with-django/)

## データベースのマイグレーション

```
python manage.py migrate
```

## アプリケーションの追加

```
python manage.py startapp [ApplicationName]
```
