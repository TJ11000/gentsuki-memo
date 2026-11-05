# -*- coding: utf-8 -*-
# project_paste.md を作る（あなたのバイク欄＋CLAUDE.md＋芯＋型＋帽子・claude.ai Project の指示欄用）
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
c = open('CLAUDE.md', encoding='utf-8').read()
c = c.replace('（Claude Code がこのフォルダで動く時に読む 1 枚）', '（この Project で動く時に読む 1 枚）')
c = c.replace('先に読む物: `my_bike.md`（本人が最初に書いた欄・空でもよい）、`core/shin.md`（芯）、`core/sheet.md`（型）、`hats/genki_nishu.md`（原付の範囲）。',
              '先に読む物: 一番上の【あなたのバイク】（空でもよい）と、下の【芯】【型】【原付の範囲】。')
def body(p):
    return open(p, encoding='utf-8').read().split('\n', 1)[1].replace('`my_bike.md`', '【あなたのバイク】')
mb = open('my_bike.md', encoding='utf-8').read().replace('# あなたのバイク', '# 【あなたのバイク】')
out = mb.rstrip() + '\n\n---\n\n' + c.rstrip() + '\n\n---\n\n# 【芯】\n' + body('core/shin.md') + '\n---\n\n# 【型】\n' + body('core/sheet.md') + '\n---\n\n# 【原付の範囲】\n' + body('hats/genki_nishu.md')
open('project_paste.md', 'w', encoding='utf-8').write(out)
open('../genki_memo_project_paste.md', 'w', encoding='utf-8').write(out)
print(len(out))
