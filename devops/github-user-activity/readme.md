https://roadmap.sh/projects/github-user-activity

---

# GitHub User Activity Fetcher

このプロジェクトは、GitHub APIを使用して指定されたユーザーの最近のアクティビティを取得し、ターミナルに表示するシンプルなコマンドラインツールです。

## 必要条件

- **Python 3.7以上**
- インターネット接続
- 追加ライブラリなしで実行可能

## 使用方法

1. このリポジトリをクローンまたはダウンロードします。

    ```bash
    git clone <このリポジトリのURL>
    cd <リポジトリのフォルダ>
    ```

2. スクリプトを実行します。

    ```bash
    python github_activity.py <GitHubユーザー名>
    ```

    例:

    ```bash
    python github_activity.py m-miyawaki-m
    ```

3. ターミナルに指定したユーザーの最近のアクティビティが表示されます。

## スクリプト概要

このツールは以下の機能を提供します:

- GitHub APIを通じて指定されたユーザーの最近のアクティビティを取得。
- コマンドライン引数としてGitHubユーザー名を受け取るシンプルなCLI。
- 取得したアクティビティをターミナル上に読みやすい形式で表示。

## 出力例

```bash
ユーザー: m-miyawaki-m の最近のアクティビティ:
  - developer-roadmap に 3 コミットをプッシュしました
  - developer-roadmap に新しいイシューをopenedしました: Add more documentation
  - developer-roadmap をスターしました
```

## 注意事項

- GitHub APIには未認証リクエストのレート制限があります。頻繁に使用する場合は認証トークンを使用することを検討してください。
- 本スクリプトは教育目的で設計されています。実際の運用ではエラーハンドリングや認証をより慎重に実装する必要があります。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルをご確認ください。