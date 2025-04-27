from app import models, database

# データベースセッションを開く
db = database.SessionLocal()

# 登録するサンプル問題リスト（10問）
sample_quizzes = [
    models.Quiz(
        question="Pythonでリストを定義するために使う記号は？",
        choice1="{}",
        choice2="[]",
        choice3="()",
        choice4="<>",
        correct_choice=2,
    ),
    models.Quiz(
        question="HTMLでリンクを作るために使うタグは？",
        choice1="<link>",
        choice2="<a>",
        choice3="<href>",
        choice4="<url>",
        correct_choice=2,
    ),
    models.Quiz(
        question="SQLでデータを取得するための命令は？",
        choice1="SELECT",
        choice2="INSERT",
        choice3="UPDATE",
        choice4="DELETE",
        correct_choice=1,
    ),
    models.Quiz(
        question="HTTPのステータスコードで「成功」を表すのは？",
        choice1="200",
        choice2="404",
        choice3="500",
        choice4="301",
        correct_choice=1,
    ),
    models.Quiz(
        question="CSSで文字色を変えるプロパティは？",
        choice1="font-color",
        choice2="text-style",
        choice3="color",
        choice4="background",
        correct_choice=3,
    ),
    models.Quiz(
        question="Pythonで関数を定義するキーワードは？",
        choice1="function",
        choice2="def",
        choice3="func",
        choice4="lambda",
        correct_choice=2,
    ),
    models.Quiz(
        question="データベースで，1行のデータのことを何と呼ぶ？",
        choice1="カラム",
        choice2="テーブル",
        choice3="レコード",
        choice4="フィールド",
        correct_choice=3,
    ),
    models.Quiz(
        question="Webページを構成する言語として正しいものは？",
        choice1="Python",
        choice2="C++",
        choice3="HTML",
        choice4="Java",
        correct_choice=3,
    ),
    models.Quiz(
        question="Pythonで無限ループを作るには？",
        choice1="while True:",
        choice2="for i in range(0,0):",
        choice3="loop:",
        choice4="repeat:",
        correct_choice=1,
    ),
    models.Quiz(
        question="HTTPのPOSTリクエストは主に何をする？",
        choice1="データ取得",
        choice2="データ送信",
        choice3="データ削除",
        choice4="ページ移動",
        correct_choice=2,
    ),
]

# データベースに保存
db.add_all(sample_quizzes)
db.commit()
db.close()

print("✅ 10問のクイズデータを登録しました！")
