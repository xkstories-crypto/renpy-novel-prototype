## お試しシナリオ「屋上の手紙」。絵の置き場所と名前は placeholders.rpy、演出と好感度表示は effects.rpy
##
## 使っている機能:
##   名前入力 / 選択肢 / 好感度ゲージ / フラグ / 条件つき選択肢 / 3つのエンド分岐
##   立ち絵の表情切り替え・跳ねる・左右移動 / 画面揺れ / 場面転換 / BGM

# BGM。audio/bgm_main.ogg を置くとタイトル画面から流れてループする（このリポジトリには同梱していない。無ければ無音で進む）
define BGM = "audio/bgm_main.ogg"
define config.main_menu_music = BGM if renpy.loadable(BGM) else None

define s = Character("さくら", color="#ff8fb1")
define me = Character("[player_name]", color="#8fd3ff")

default player_name = "湊"
default affection = 0
default clue_footprint = False   # 昼休みに下駄箱で手がかりを見つけたか

label start:
    # タイトル画面から流れている曲はそのまま続ける（頭から鳴らし直さない）
    if renpy.loadable(BGM):
        play music BGM if_changed
    scene bg black
    "春。二年生になって、最初の一週間。"

    # 名前入力（自動テスト中は入力を飛ばす）
    if not renpy.is_in_test():
        $ player_name = renpy.input("あなたの名前は？", default="湊", length=8).strip() or "湊"

    "おれの名前は[player_name]。ごく普通の高校生だ。"

    jump morning


label morning:
    scene bg classroom with fade
    show screen affection_hud
    show sakura normal at center with dissolve

    s "おはよう、[player_name]くん。ねえ、ちょっと見てほしいものがあるの。"
    s "朝来たら、机の中にこれが入ってて……。"
    "差し出されたのは白い封筒。中のメモには一行だけ。"
    "『放課後、屋上で待ってる』"

    show sakura surprised at center, hop
    s "差出人の名前が無いの！　どう思う？"

    menu:
        "放課後、一緒に行ってあげるよ":
            $ change_affection(1)
            me "ひとりだと心配だろ。おれも一緒に行くよ。"
            show sakura smile
            s "ほんと？　ありがとう、心強いな。"

        "ラブレターじゃん、よかったな":
            $ change_affection(-1)
            me "ラブレターだろ、それ。モテるなあ。"
            show sakura surprised at center, hop
            s "ちょっ……！　そういうのじゃないかもしれないでしょ！"
            show sakura normal
            s "……もういい。"

    jump lunch


label lunch:
    "昼休み。"
    show sakura normal at center
    s "わたし、委員会があるから先に行くね。"
    hide sakura with moveoutright

    "さて、何をしようか。"

    menu:
        "下駄箱のあたりを調べてみる":
            $ clue_footprint = True
            "さくらの下駄箱の前に、小さな上履きの跡が残っている。"
            "かかとに、ピンクのインクが付いていた。"
            "……どこかで見た色だな。"

        "購買でパンを買う":
            "焼きそばパンは今日も売り切れだった。"

    jump rooftop


label rooftop:
    "放課後。"
    scene bg rooftop with dissolve
    show sakura normal at left with dissolve
    s "誰もいない……ね。"
    show sakura normal at center with move
    s "いたずらだったのかな。"

    # 屋上のドアが勢いよく閉まる
    show layer master at shake
    "バンッ！！"
    show layer master
    show sakura surprised at center, hop
    s "ひゃっ！？　び、びっくりした……風でドアが閉まったみたい。"
    show sakura normal

    s "ねえ、[player_name]くん。この手紙のこと、どう思う？"

    menu:
        "下駄箱のピンクのインクのことを話す" if clue_footprint:
            me "下駄箱の前に、ピンクのインクが付いた足跡があった。"
            me "さくら、そのペン……いつも使ってるやつだよな。"
            show sakura surprised at center, hop
            s "……っ！"
            jump ending_check

        "やっぱりいたずらだよ、帰ろう":
            me "いたずらだったんだよ。暗くなる前に帰ろう。"
            jump ending_check

        "もう少しだけ待ってみよう":
            $ change_affection(1)
            me "せっかく来たんだし、もう少し待ってみよう。"
            show sakura smile
            s "……うん。"
            jump ending_check


label ending_check:
    if clue_footprint and affection >= 1:
        jump ending_truth
    elif affection >= 1:
        jump ending_friends
    else:
        jump ending_normal


label ending_truth:
    show sakura smile
    s "……バレちゃった。あの手紙、書いたのわたしなの。"
    s "直接言う勇気がなくて。でも、来てくれるかなって。"
    s "[player_name]くん。わたし、あなたのことが――"
    "夕日が、屋上をオレンジ色に染めていた。"
    "（好感度 [affection]：真相エンド）"
    jump finish


label ending_friends:
    show sakura smile
    s "結局、誰も来なかったね。"
    s "でも……今日、ここに来てよかった。また明日ね！"
    "（好感度 [affection]：仲良しエンド）"
    jump finish


label ending_normal:
    s "そっか。じゃあ、また明日。"
    hide sakura with dissolve
    "差出人は、結局わからないままだった。"
    "（好感度 [affection]：ふつうエンド）"
    jump finish


label finish:
    hide screen affection_hud
    stop music fadeout 2.0
    scene bg black with fade
    "―― おしまい ――"
    return
