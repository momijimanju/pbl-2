# pbl-2

### 概要

PBLのプロジェクトです。現在は受付システムのみの実装を目的としています。

### 使用ツール

- git
- django
- boostrap
- Postgresql

### 開発環境構築

#### githubの環境を作る

`git clone https://github.com/momijimanju/pbl-2.git`でcloneしてきてください。

#### python仮想環境の作成

Git cloneしたディレクトリでwindowsなら`py -m venv myvenv`でmyvenvというディレクトリが生成されます。

そこで、`cd myvenv/Scripts`でディレクトリを移動し、`activate.bat`で仮想環境に入れます。

次にpipパッケージを同期します。pblディレクトリに入り`pip install -r requirements.txt`でインストールが始まります。

#### 構築できたかの確認

最後にpblディレクトリの中のmanage.pyを実行します。

仮想環境に入った状態で`python manage.py runserver`でサーバーを起動し、ブラウザで`localhost:8000/reception/[url.pyで指定したpath]`にアクセスしてください。

一例として、`localhost:8000/reception/firstform/`にアクセスできれば、環境構築は正しくできています。



