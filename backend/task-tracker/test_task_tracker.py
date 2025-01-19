import unittest
import os
import json
from datetime import datetime
from custom_runner import CSVTestRunner
from task_tracker import (
    load_tasks, save_tasks, add_task, update_task,
    delete_task, mark_in_progress, mark_done, list_tasks
)


class TestTaskTracker(unittest.TestCase):
    TEST_FILE = "tasks.json"

    def setUp(self):
        """テスト用の環境をセットアップ"""
        self.sample_tasks = [
            {"id": 1, "description": "Task 1", "status": "todo",
             "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()}
        ]
        with open(self.TEST_FILE, "w") as file:
            json.dump(self.sample_tasks, file, indent=4)

    def tearDown(self):
        """テスト終了後にタスクファイルを削除"""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def load_test_tasks(self):
        """テスト用ファイルを読み込む"""
        with open(self.TEST_FILE, "r") as file:
            return json.load(file)

    def test_load_tasks_file_not_found(self):
        """UT001: ファイルが存在しない場合"""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)
        tasks = load_tasks()
        self.assertEqual(tasks, [])

    def test_load_tasks_file_exists(self):
        """UT002: ファイルが存在しデータがある場合"""
        tasks = load_tasks()
        self.assertEqual(len(tasks), len(self.sample_tasks))
        self.assertEqual(tasks[0]["description"], "Task 1")

    def test_save_tasks(self):
        """UT003: リストをJSON形式で保存"""
        new_tasks = [
            {"id": 1, "description": "New Task", "status": "todo",
             "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()}
        ]
        save_tasks(new_tasks)
        tasks = self.load_test_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "New Task")

    def test_add_task(self):
        """UT004: 新しいタスクを追加"""
        add_task("New Task")
        tasks = self.load_test_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[-1]["description"], "New Task")

    def test_update_task(self):
        """UT005: 指定IDのタスクを更新"""
        update_task(1, "Updated Task")
        tasks = self.load_test_tasks()
        self.assertEqual(tasks[0]["description"], "Updated Task")

    def test_update_task_nonexistent_id(self):
        """UT006: 存在しないIDを更新する"""
        with self.assertLogs(level="INFO") as cm:
            update_task(99, "Updated Task")  # 存在しないIDで更新を試みる
        # ログ出力に "Task ID 99 not found." が含まれていることを確認
        self.assertIn("Task ID 99 not found.", cm.output[0])

    def test_delete_task(self):
        """UT007: 指定IDのタスクを削除"""
        delete_task(1)
        tasks = self.load_test_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_task_nonexistent_id(self):
        """UT008: 存在しないIDを削除する"""
        with self.assertLogs(level="INFO") as cm:
            delete_task(99)  # 存在しないIDで削除を試みる
        # ログ出力に "Task ID 99 not found." が含まれていることを確認
        self.assertIn("Task ID 99 not found.", cm.output[0])

    def test_mark_in_progress(self):
        """UT009: 指定IDのタスクを進行中に設定"""
        mark_in_progress(1)
        tasks = self.load_test_tasks()
        self.assertEqual(tasks[0]["status"], "in-progress")

    def test_mark_done(self):
        """UT010: 指定IDのタスクを完了に設定"""
        mark_done(1)
        tasks = self.load_test_tasks()
        self.assertEqual(tasks[0]["status"], "done")

    def test_list_tasks_all(self):
        """UT011: 全タスクをリスト表示"""
        with self.assertLogs(level="INFO") as cm:
            list_tasks()  # デフォルトの TEST_FILE を使用
        self.assertIn("ID: 1, Description: Task 1, Status: todo", cm.output[0])
        self.assertIn("Created At:", cm.output[0])
        self.assertIn("Updated At:", cm.output[0])

    def test_list_tasks_by_status(self):
        """UT012: 指定ステータスのタスクを表示する"""
        # タスクを初期設定
        self.sample_tasks = [
            {"id": 1, "description": "Task 1", "status": "todo",
             "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()},
            {"id": 2, "description": "Task 2", "status": "done",
             "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()}
        ]
        # 初期データをテスト用ファイルに保存
        with open(self.TEST_FILE, "w") as file:
            json.dump(self.sample_tasks, file, indent=4)

        # ステータス "done" のタスクをリストアップ
        with self.assertLogs(level="INFO") as cm:
            list_tasks(status="done")

        # ログに "Task 2" の情報が含まれていることを確認
        self.assertIn("ID: 2, Description: Task 2, Status: done", cm.output[0])
        # "Task 1" は含まれていないことを確認
        self.assertNotIn("Task 1", cm.output[0])


    def test_list_tasks_empty(self):
        """UT013: 空のリストを表示"""
        delete_task(1)  # タスクを削除
        with self.assertLogs(level="INFO") as cm:
            list_tasks()  # 空のタスクをリスト
        self.assertIn("No tasks found.", cm.output[0])

    def test_list_tasks_invalid_status(self):
        """UT014: 無効なステータスを指定した場合"""
        with self.assertLogs(level="INFO") as cm:
            list_tasks(status="invalid_status")  # 無効なステータスを渡す
        self.assertIn("No tasks found.", cm.output[0])  # "No tasks found." がログに含まれることを確認

    def test_list_tasks_by_status(self):
        """UT015: 特定のステータスのタスクをリスト表示"""
        add_task("Task 2")  # 新しいタスクを追加
        mark_done(1)  # ID 1 のタスクを完了に設定
        with self.assertLogs(level="INFO") as cm:
            list_tasks(status="done")  # ステータス "done" のタスクをリスト
        self.assertIn("ID: 1, Description: Task 1, Status: done", cm.output[0])
        self.assertNotIn("Task 2", cm.output[0])  # "Task 2" はリストに含まれない

if __name__ == "__main__":
    # テストスイートを収集
    suite = unittest.defaultTestLoader.discover(".", pattern="test_*.py")
    
    # カスタムランナーで実行
    runner = CSVTestRunner(verbosity=2, output_csv="./test/result_unit/test_summary.csv", coverage_report="./test/result_unit/test_coverage.txt")
    runner.run(suite)