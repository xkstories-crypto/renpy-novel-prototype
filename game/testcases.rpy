## 自動テスト。全エンドを最後まで通して、落ちないことを確かめる
## 実行: renpy.py <このプロジェクト> test "routes::truth_end"（1本ずつ）
## まとめて流すと2本目が最初の選択肢で止まる（ゲームではなくテストの続け方の問題）

testsuite global:
    teardown:
        exit

testsuite routes:
    before testcase:
        $ _test.transition_timeout = 0.05
        run Jump("start")

    testcase truth_end:
        advance until screen "choice"
        pause 0.5
        click "放課後、一緒に行ってあげるよ"
        advance until screen "choice"
        pause 0.5
        click "下駄箱のあたりを調べてみる"
        advance until screen "choice"
        pause 0.5
        click "下駄箱のピンクのインクのことを話す"
        advance until "真相エンド"
        advance until "おしまい"

    testcase friends_end:
        advance until screen "choice"
        pause 0.5
        click "放課後、一緒に行ってあげるよ"
        advance until screen "choice"
        pause 0.5
        click "購買でパンを買う"
        advance until screen "choice"
        pause 0.5
        click "もう少しだけ待ってみよう"
        advance until "仲良しエンド"
        advance until "おしまい"

    testcase normal_end:
        advance until screen "choice"
        pause 0.5
        click "ラブレターじゃん、よかったな"
        advance until screen "choice"
        pause 0.5
        click "下駄箱のあたりを調べてみる"
        advance until screen "choice"
        pause 0.5
        click "やっぱりいたずらだよ、帰ろう"
        advance until "ふつうエンド"
        advance until "おしまい"
