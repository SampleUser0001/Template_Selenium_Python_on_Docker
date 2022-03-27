# Template_Selenium_Python_on_Docker

## 使い方

### 準備

1. Dockerfileのimageを変更する。
2. 必要に応じてDockerfileにpipを書く。
3. 必要に応じてdocker-compose.ymlを修正する。
4. ```app/src/sample.env```をコピーして、```app/src/.env```を作成する。
5. ```app/src/.env```を編集する。

### Selenium Server起動

``` bash
docker-compose up -d
```

### テスト

``` sh
docker-compose exec test bash start.sh
```

### 起動引数を渡したい場合

1. ```app/start.sh```を修正する。
2. ```app/src/app.py```を修正する。
3. 下記で実行。

    ``` sh
    docker-compose exec test bash start.sh ${引数 ... }
    ```

## 参考

- [Qiita:Docker を使う（python のイメージで色々確認してみる）](https://qiita.com/landwarrior/items/fd918da9ebae20486b81)
- [Future Tech Blog:仕事でPythonコンテナをデプロイする人向けのDockerfile (1): オールマイティ編](https://future-architect.github.io/articles/20200513/)
- [Use_Selenium_Python:SampleUser0001:Github](https://github.com/SampleUser0001/Use_Selenium_Python)