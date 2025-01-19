import requests
import sys

def fetch_github_activity(username):
    # GitHub APIエンドポイントを設定
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # GitHub APIにリクエストを送信
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードを確認
        
        # JSONレスポンスを取得
        events = response.json()
        
        # イベントがない場合の処理
        if not events:
            print("このユーザーには最近のアクティビティがありません。")
            return
        
        # イベントをターミナルに表示
        print(f"ユーザー: {username} の最近のアクティビティ:")
        for event in events:
            # イベントのタイプに応じたメッセージを表示
            if event["type"] == "PushEvent":
                repo_name = event["repo"]["name"]
                commit_count = len(event["payload"]["commits"])
                print(f"  - {repo_name} に {commit_count} コミットをプッシュしました")
            elif event["type"] == "IssuesEvent":
                repo_name = event["repo"]["name"]
                action = event["payload"]["action"]
                issue_title = event["payload"]["issue"]["title"]
                print(f"  - {repo_name} に新しいイシューを{action}しました: {issue_title}")
            elif event["type"] == "WatchEvent":
                repo_name = event["repo"]["name"]
                print(f"  - {repo_name} をスターしました")
            # 他のイベントタイプも必要に応じて追加可能
        print("\n取得完了！")
    
    except requests.exceptions.RequestException as e:
        print("エラーが発生しました:", e)
    except KeyError as e:
        print("予期しないデータ形式:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python github_activity.py <GitHubユーザー名>")
    else:
        username = sys.argv[1]
        fetch_github_activity(username)
