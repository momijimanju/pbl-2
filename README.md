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

そこで`myvenv¥Scripts¥activate.bat`で仮想環境に入れます。

次にpipパッケージを同期します。pblディレクトリに入り`pip install -r requirements.txt`でインストールが始まります。

#### 構築できたかの確認

最後にpblディレクトリの中のmanage.pyを実行します。

`python manage.py runserver`でサーバーを起動し、ブラウザで`localhost:8000`にアクセスしてください。djangoの画面が表示されたら環境構築は正しくできています。



