## このウェブサイトへの貢献方法

1. Python と pip をインストールしてください。
2. このリポジトリを Fork してください。
3. リポジトリ内の `sourcedir` フォルダ下の md ファイルを更新する、もしくはリポジトリ内の `sourcedir` フォルダ下に md ファイルを追加してください。
4. ターミナルアプリを起動後、このリポジトリに `cd` してください。
5. 下記のコマンドを実行してください。 `builddir` 下にウェブサイトがビルドされます。 `builddir` 下の index.html をクリックするとビルドされたウェブサイトの確認ができます。
  ```
  pip install -r requirements.txt
  pip install -U Sphinx
  mkdir builddir
  sphinx-build -b html sourcedir builddir
  ```
6. 3 の md ファイルを git でコミットしてください。
7. 6 のコミットを 2. にプッシュしてください。
8. 7 のプッシュ内容を、このリポジトリに対してプルリクエストしてください。
