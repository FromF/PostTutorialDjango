# グレースケール変換
Python DjangoとOpen CVでグレースケールに変換する

JPGファイルをアップするとグレースケールになったJPGファイルが表示される

## 参考サイト

* [Djangoで画像処理アプリケーションを作った](https://qiita.com/takuto412/items/fb2d84c2a0ac03522005)
* [【Django】画像をアップロードして表示する](https://ymgsapo.com/show-image-imagefield/)
* [Django データベース操作 についてのまとめ](https://qiita.com/okoppe8/items/66a8747cf179a538355b)

## ライブラリ

### OpenCVインストール

```
pip install opencv-python
```

### Pillowインストール

画像を扱うときに使うライブラリ

```
pip install Pillow
```

### importがうまく行かないとき

```
pip install --upgrade pip
```

### インストールの参考サイト
* [pip で OpenCV のインストール](https://qiita.com/fiftystorm36/items/1a285b5fbf99f8ac82eb)



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

## アプリケーションの追加

```
python manage.py startapp GrayScale
```

## データベースのマイグレーション

```
python manage.py makemigrations GrayScale
python manage.py migrate
```

## 管理者アカウント作成

```
python manage.py createsuperuser
```
