https://roadmap.sh/projects/task-tracker

---

# Task Tracker CLI

## 概要
Task Tracker CLIは、コマンドラインからタスクを管理するためのシンプルなツールです。タスクの追加、更新、削除、ステータス変更、リストアップをサポートし、タスクはJSONファイルに保存されます。

---

## 主な機能
- **タスクの追加**: 新しいタスクを作成します。
- **タスクの更新**: 既存のタスクの内容を変更します。
- **タスクの削除**: 不要なタスクを削除します。
- **ステータス変更**:
  - 進行中 (`in-progress`) に設定
  - 完了 (`done`) に設定
- **タスクのリストアップ**:
  - 全タスクの表示
  - ステータス（完了、進行中、未完了）ごとの表示

---

## 必要条件
- **Python 3.x**
- 標準Pythonモジュールのみ使用（外部ライブラリ不要）

---

## インストール
1. このリポジトリをクローンまたはダウンロードします:
   ```bash
   git clone https://github.com/m-miyawaki-m/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. 必要に応じてPython環境をセットアップします。

3. 初期化:
   JSONファイルが存在しない場合、スクリプト実行時に自動生成されます。

---

## 使用方法
以下は使用可能なコマンド一覧と例です。

### **1. タスクを追加**
```bash
python task_tracker.py add "タスク内容"
```
例:
```bash
python task_tracker.py add "レポートを提出する"
```
出力:
```
Task added successfully (ID: 1)
```

### **2. タスクを更新**
```bash
python task_tracker.py update [タスクID] "新しいタスク内容"
```
例:
```bash
python task_tracker.py update 1 "レポートを提出してレビューを依頼する"
```
出力:
```
Task ID 1 updated successfully.
```

### **3. タスクを削除**
```bash
python task_tracker.py delete [タスクID]
```
例:
```bash
python task_tracker.py delete 1
```
出力:
```
Task ID 1 deleted successfully.
```

### **4. タスクのステータスを変更**
#### 進行中に設定
```bash
python task_tracker.py mark-in-progress [タスクID]
```
例:
```bash
python task_tracker.py mark-in-progress 2
```
出力:
```
Task ID 2 marked as in-progress.
```

#### 完了に設定
```bash
python task_tracker.py mark-done [タスクID]
```
例:
```bash
python task_tracker.py mark-done 2
```
出力:
```
Task ID 2 marked as done.
```

### **5. タスクのリスト表示**
#### 全タスクを表示
```bash
python task_tracker.py list
```
例:
```bash
python task_tracker.py list
```
出力:
```
ID: 1, Description: レポートを提出する, Status: todo, Created At: ..., Updated At: ...
ID: 2, Description: 会議の準備, Status: in-progress, Created At: ..., Updated At: ...
```

#### ステータスごとのタスクを表示
- **完了タスクのみ**:
  ```bash
  python task_tracker.py list done
  ```
- **未完了タスク（todo）**:
  ```bash
  python task_tracker.py list todo
  ```
- **進行中タスク**:
  ```bash
  python task_tracker.py list in-progress
  ```

---

## ファイル構成
```
task-tracker/
├── task_tracker.py    # メインプログラム
├── tasks.json         # タスクデータ保存用ファイル
└── README.md          # プロジェクトの説明書
```

---

## 注意事項
- タスクIDは自動的に生成され、削除後の再利用はされません。
- JSONファイルが存在しない場合、スクリプト実行時に自動生成されます。

---

## 今後の改善案
- コマンド補完機能の追加
- タスクの優先度（High, Medium, Low）のサポート
- JSONデータの暗号化（セキュリティ強化）
- より洗練されたエラーハンドリング

---

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

---

## 貢献
バグ報告や新機能の提案は、[Issues](https://github.com/m-miyawaki-m/task-tracker-cli/issues)ページから行ってください。プルリクエストも歓迎します！