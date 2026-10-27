## 仮の絵。images/ に同じ名前の画像（例: images/sakura smile.png）を置くと、そちらが自動で使われる。
## 置く画像の目安:
##   背景   bg classroom.png / bg rooftop.png             … 1280x720
##   立ち絵 sakura normal.png / sakura smile.png / sakura surprised.png … 背景透過PNG、高さ600〜700px程度
##   表情差分が無いときは sakura base.png を1枚置けば、全表情にそれが使われる

init python:

    def _find_image_file(name):
        for ext in (".png", ".webp", ".jpg", ".jpeg"):
            if renpy.loadable("images/" + name + ext):
                return "images/" + name + ext
        return None

    def _has_image_file(name):
        return _find_image_file(name) is not None

    def _placeholder_bg(name, color):
        if not _has_image_file(name):
            renpy.image(name, Solid(color))

    def _placeholder_sprite(name, label, color):
        if _has_image_file(name):
            return

        base = _find_image_file(name.split()[0] + " base")
        if base:
            renpy.image(name, base)
        else:
            renpy.image(name, Composite(
                (300, 500),
                (0, 0), Solid(color, xsize=300, ysize=500),
                (0, 220), Text(label, size=36, xsize=300, text_align=0.5, color="#5a2a3a"),
            ))

    _placeholder_bg("bg classroom", "#c9b79c")
    _placeholder_bg("bg rooftop", "#7fb3e6")
    _placeholder_bg("bg black", "#000000")

    _placeholder_sprite("sakura normal", "さくら\n（通常）", "#ffb6c8")
    _placeholder_sprite("sakura smile", "さくら\n（笑顔）", "#ffd1dc")
    _placeholder_sprite("sakura surprised", "さくら\n（驚き）", "#ff9aa2")
