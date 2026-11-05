# project_paste.md を作る（CLAUDE.md＋芯＋型＋帽子を 1 枚に・claude.ai Project の指示欄用）
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
c = open('CLAUDE.md', encoding='utf-8').read()
c = c.replace("（Claude Code がこのフォルダで動く時に読む 1 枚）", "（この Project で動く時に読む 1 枚）")
c = c.replace("起動したら先にこの 3 枚を読む。", "下の 3 つの節が、元のフォルダでは別ファイルやった物。先にこの 3 つを読む。")
c = c.replace("- `core/shin.md` — 芯。", "- 【芯】— ").replace("- `core/sheet.md` — 1 枚の型。", "- 【1 枚の型】— ").replace("- `hats/genki_nishu.md` — 帽子。", "- 【帽子】— ")
c = c.replace("（欄は `core/sheet.md` の「入口」）", "（欄は【1 枚の型】の「入口」）").replace("（`core/shin.md` 止まり方）", "（【芯】止まり方）")
c = c.replace("帽子を替えると別の現場の係になる（`hats/_TEMPLATE.md`）。芯は触らん。", "帽子を替えると別の現場の係になる。芯は触らん。")
c = c.replace("紙 1 枚（`core/sheet.md` の型）", "紙 1 枚（【1 枚の型】の型）")
c = c.replace("`my_bike.md`（本人が最初に 1 回だけ書いておく欄）", "【あなたのバイク】（この指示の一番上・本人が最初に 1 回だけ書いておく欄）")


def body(p):
    return open(p, encoding='utf-8').read().split('\n', 1)[1].replace('`core/sheet.md`', '【1 枚の型】').replace('`core/shin.md`', '【芯】')


mb = open('my_bike.md', encoding='utf-8').read().replace('# あなたのバイク', '# 【あなたのバイク】')  # MY_BIKE
out = mb.rstrip() + '\n\n---\n\n' + c.rstrip() + "\n\n---\n\n# 【芯】\n" + body('core/shin.md') + "\n---\n\n# 【1 枚の型】\n" + body('core/sheet.md') + "\n---\n\n# 【帽子】\n" + body('hats/genki_nishu.md')
open('project_paste.md', 'w', encoding='utf-8').write(out)
open('../genki_memo_project_paste.md', 'w', encoding='utf-8').write(out)
print(len(out))
