## 演出（ATL）と、好感度の表示（screen）

## 立ち絵がぴょんと跳ねる。驚いたとき用
transform hop:
    yoffset 0
    easein 0.10 yoffset -40
    easeout 0.10 yoffset 0
    easein 0.08 yoffset -15
    easeout 0.08 yoffset 0

## 画面全体を左右に揺らす。`show layer master at shake` で使う
transform shake:
    block:
        linear 0.04 xoffset -14
        linear 0.04 xoffset 14
        repeat 5
    linear 0.04 xoffset 0


## 好感度 ##################################################################

define AFFECTION_MAX = 5

init python:

    def change_affection(amount):
        store.affection += amount
        if amount > 0:
            renpy.notify("好感度 +{}".format(amount))
        elif amount < 0:
            renpy.notify("好感度 {}".format(amount))

## 画面左上に常に出しておく好感度ゲージ
screen affection_hud():
    zorder 50

    frame:
        xpos 20
        ypos 20
        padding (16, 10)
        background Solid("#00000099")

        hbox:
            spacing 12
            yalign 0.5
            text "好感度" size 20 yalign 0.5
            bar:
                value AnimatedValue(max(affection, 0), AFFECTION_MAX, delay=0.5)
                xsize 160
                ysize 20
                yalign 0.5
            text "[affection]" size 20 yalign 0.5
