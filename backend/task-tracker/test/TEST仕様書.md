# **単体テスト仕様書**

## **目的**
各関数が個別に正しい動作をすることを確認する。

### **テスト項目一覧**
| テスト項目ID | テスト内容                                    | 期待結果                                                   |
|--------------|-----------------------------------------------|-----------------------------------------------------------|
| UT001        | `load_tasks`: 存在しないファイルを読み込む      | 空のリストを返却                                           |
| UT002        | `load_tasks`: ファイルが存在しデータがある場合  | ファイル内のタスクデータをリスト形式で返却                 |
| UT003        | `save_tasks`: リストをJSON形式で保存する        | 指定された内容がファイルに正しく保存される                 |
| UT004        | `add_task`: 新しいタスクを追加する             | タスクが正しくリストに追加され、JSONに保存される           |
| UT005        | `update_task`: 指定IDのタスクを更新する         | 指定されたタスクの内容が正しく変更され、JSONに保存される   |
| UT006        | `update_task`: 存在しないIDを更新する          | エラーメッセージを表示                                     |
| UT007        | `delete_task`: 指定IDのタスクを削除する         | タスクがリストから削除され、JSONに保存される               |
| UT008        | `delete_task`: 存在しないIDを削除する          | エラーメッセージを表示                                     |
| UT009        | `mark_in_progress`: 指定IDのタスクを進行中に設定| ステータスが`in-progress`に更新され、JSONに保存される       |
| UT010        | `mark_done`: 指定IDのタスクを完了に設定         | ステータスが`done`に更新され、JSONに保存される             |
| UT011        | `list_tasks`: 全タスクをリスト表示する          | すべてのタスクの詳細を表示                                 |
| UT012        | `list_tasks`: 指定ステータスのタスクを表示する  | 指定ステータスのタスクのみ表示                             |
| UT013        | `list_tasks`: 空のリストを表示する              | "No tasks found." を表示                                   |

---

### **テストケース詳細**

以下に、単体テストのテストケース詳細を全て記載します。

---

## **UT001: 存在しないファイルを読み込む**
- **事前条件**: `tasks.json` ファイルが存在しない。
- **入力**: `load_tasks()`
- **期待結果**:
  - 空のリスト `[]` を返却する。

---

## **UT002: ファイルが存在しデータがある場合**
- **事前条件**: 
  - `tasks.json` ファイルが存在。
  - ファイルに以下のデータが格納されている：
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
    ]
    ```
- **入力**: `load_tasks()`
- **期待結果**:
  - ファイル内のデータをリスト形式で返却。
  - 出力例:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
    ]
    ```

---

## **UT003: リストをJSON形式で保存する**
- **事前条件**: `tasks.json` ファイルが存在。
- **入力**:
  - `save_tasks([{"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}])`
- **期待結果**:
  - 指定された内容がファイルに正しく保存される。
  - ファイルの内容:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
    ]
    ```

---

## **UT004: 新しいタスクを追加する**
- **事前条件**: `tasks.json` ファイルに3つのタスクが存在。
- **入力**: `add_task("New Task")`
- **期待結果**:
  - 新しいタスクがリストに追加される。
  - ファイルに保存された内容:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."},
        {"id": 2, "description": "Task 2", "status": "todo", "createdAt": "...", "updatedAt": "..."},
        {"id": 3, "description": "Task 3", "status": "todo", "createdAt": "...", "updatedAt": "..."},
        {"id": 4, "description": "New Task", "status": "todo", "createdAt": "...", "updatedAt": "..."}
    ]
    ```

---

## **UT005: 指定IDのタスクを更新する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `update_task(1, "Updated Task")`
- **期待結果**:
  - タスクID 1 の `description` が `Updated Task` に更新される。
  - ファイルに保存された内容:
    ```json
    [
        {"id": 1, "description": "Updated Task", "status": "todo", "createdAt": "...", "updatedAt": "..."}
    ]
    ```

---

## **UT006: 存在しないIDを更新する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `update_task(99, "Updated Task")`
- **期待結果**:
  - タスクID 99 が見つからず、エラーメッセージを表示。
  - 出力:
    ```plaintext
    Task ID 99 not found.
    ```

---

## **UT007: 指定IDのタスクを削除する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `delete_task(1)`
- **期待結果**:
  - タスクID 1 がリストから削除される。
  - ファイルが空の状態になる：
    ```json
    []
    ```

---

## **UT008: 存在しないIDを削除する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `delete_task(99)`
- **期待結果**:
  - タスクID 99 が見つからず、エラーメッセージを表示。
  - 出力:
    ```plaintext
    Task ID 99 not found.
    ```

---

## **UT009: 指定IDのタスクを進行中に設定する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `mark_in_progress(1)`
- **期待結果**:
  - タスクID 1 の `status` が `in-progress` に更新される。
  - ファイルに保存された内容:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "in-progress", "createdAt": "...", "updatedAt": "..."}
    ]
    ```

---

## **UT010: 指定IDのタスクを完了に設定する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `mark_done(1)`
- **期待結果**:
  - タスクID 1 の `status` が `done` に更新される。
  - ファイルに保存された内容:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "done", "createdAt": "...", "updatedAt": "..."}
    ]
    ```

---

## **UT011: 全タスクをリスト表示する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `list_tasks()`
- **期待結果**:
  - すべてのタスクが詳細とともに表示される。
  - 出力例:
    ```plaintext
    ID: 1, Description: Task 1, Status: todo, Created At: ..., Updated At: ...
    ```

---

## **UT012: 指定ステータスのタスクを表示する**
- **事前条件**: `tasks.json` ファイルに以下のデータが存在：
  ```json
  [
      {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."},
      {"id": 2, "description": "Task 2", "status": "done", "createdAt": "...", "updatedAt": "..."}
  ]
  ```
- **入力**: `list_tasks("done")`
- **期待結果**:
  - `done` ステータスのタスクのみ表示される。
  - 出力例:
    ```plaintext
    ID: 2, Description: Task 2, Status: done, Created At: ..., Updated At: ...
    ```

---

## **UT013: 空のリストを表示する**
- **事前条件**: `tasks.json` ファイルが空。
- **入力**: `list_tasks()`
- **期待結果**:
  - タスクが見つからない場合、以下のメッセージを表示。
  - 出力:
    ```plaintext
    No tasks found.
    ```

---

#### **UT014: 無効なステータスを指定した場合**
- **事前条件**:
  - `tasks.json` に以下のタスクが存在:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."}
    ]
    ```
- **入力**: `list_tasks(status="invalid_status")`
- **期待結果**:
  - `"No tasks found."` のログが出力される。
  - 他のタスクに影響を与えない。

---

#### **UT015: 特定のステータスのタスクをリスト表示**
- **事前条件**:
  - `tasks.json` に以下のタスクが存在:
    ```json
    [
        {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "...", "updatedAt": "..."},
        {"id": 2, "description": "Task 2", "status": "done", "createdAt": "...", "updatedAt": "..."}
    ]
    ```
- **入力**: `list_tasks(status="done")`
- **期待結果**:
  - 以下のログが出力される:
    ```
    ID: 2, Description: Task 2, Status: done, Created At: ..., Updated At: ...
    ```
  - `"Task 1"` はログに含まれない。

---

# **シナリオテスト仕様書**

## **目的**
一連の操作を通じて、システム全体が期待通りに動作することを確認する。

### **シナリオ一覧**
| シナリオID | シナリオ内容                             | 期待結果                                                                 |
|------------|------------------------------------------|--------------------------------------------------------------------------|
| SC001      | 新しいタスクを追加し、リスト表示する       | 新しいタスクがリストに表示される                                         |
| SC002      | タスクを更新し、変更が反映されていることを確認 | 更新内容がリスト表示で確認できる                                         |
| SC003      | タスクを進行中に設定し、リスト表示で確認する | ステータスが`in-progress`に更新されている                                |
| SC004      | タスクを完了に設定し、リスト表示で確認する  | ステータスが`done`に更新されている                                       |
| SC005      | タスクを削除し、リスト表示で削除が反映されていることを確認 | 指定されたタスクがリストから削除され、他のタスクに影響がない              |

---

### **シナリオケース詳細**

#### **SC001: 新しいタスクを追加し、リスト表示する**
- **手順**:
  1. コマンドラインで次を実行: `python task_tracker.py add "Task 1"`
  2. コマンドラインで次を実行: `python task_tracker.py list`
- **期待結果**:
  - タスクが追加され、リスト表示で確認できる。
  - 出力例:
    ```plaintext
    ID: 1, Description: Task 1, Status: todo, Created At: ..., Updated At: ...
    ```

#### **SC003: タスクを進行中に設定し、リスト表示で確認する**
- **手順**:
  1. コマンドラインで次を実行: `python task_tracker.py mark-in-progress 1`
  2. コマンドラインで次を実行: `python task_tracker.py list in-progress`
- **期待結果**:
  - タスクのステータスが`in-progress`に更新されている。
  - 出力例:
    ```plaintext
    ID: 1, Description: Task 1, Status: in-progress, Created At: ..., Updated At: ...
    ```

#### **SC005: タスクを削除し、リスト表示で削除が反映されていることを確認**
- **手順**:
  1. コマンドラインで次を実行: `python task_tracker.py delete 1`
  2. コマンドラインで次を実行: `python task_tracker.py list`
- **期待結果**:
  - 指定されたタスクが削除され、リストに表示されない。
  - 出力例:
    ```plaintext
    No tasks found.
    ```

---