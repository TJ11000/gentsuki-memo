# -*- coding: utf-8 -*-
# 紙の中身の検査（AI を呼ばない・保存した出力を読むだけ）
# 使い方: python3 tests/check_paper.py 出力1.txt 出力2.txt ...
# 見る事（「ここから下は お店の人へ」の線より下＝店に見せるメモだけ）:
#   1. 原因・部品・金額を書いていない（下の「書かない語」が出たら NG）
#   2. 箇条の行（「- 」で始まる行）に札が付いている（core/shin.md の 5 つのどれか）。「分からない所」の節は札なしでよい
# 限界: 語のリストで見ているだけ。言い換えた原因（「〜が弱っている」等）は拾えない。最後は人の目で読む。
import re, sys

LINE = 'ここから下は お店の人へ'
TAGS = ['[本人]', '[本人の推測]', '[本人: 分からん]', '[本人 未回答]', '[AI 知識・店で確認]']
BANNED = [r'\d[\d,]*\s*円', r'円前後', '部品代', '工賃', '交換(が|を|して|する|した方)', '原因は(?!、お店の人が実物を見ないと分かりません)',
          'プラグ', 'ベルト', 'ウエイトローラー', 'ブレーキパッド', 'バッテリー上がり', 'が原因', 'が怪しい']

def check(path):
    t = open(path, encoding='utf-8').read()
    if LINE not in t:
        return None, ['店へのメモが無い（1 回目だけの出力）']
    memo = t.split(LINE, 1)[1]
    bad = []
    for pat in BANNED:
        for m in re.finditer(pat, memo):
            s = memo.rfind('\n', 0, m.start()) + 1
            e = memo.find('\n', m.end())
            bad.append('書かない語「%s」: %s' % (m.group(0), memo[s:e if e >= 0 else None].strip()))
    sec = ''
    for ln in memo.splitlines():
        if ln.startswith('## '):
            sec = ln[3:].strip()
        elif ln.lstrip().startswith('- ') and '分からない所' not in sec:
            if not any(tag in ln for tag in TAGS):
                bad.append('札が無い行（%s）: %s' % (sec, ln.strip()))
    return (len(bad) == 0), bad

ok = ng = skip = 0
for p in sys.argv[1:]:
    r, msgs = check(p)
    if r is None:
        skip += 1; print('飛ばす  %s（%s）' % (p, msgs[0])); continue
    if r:
        ok += 1; print('合う    %s' % p)
    else:
        ng += 1; print('合わん  %s' % p)
        for m in msgs:
            print('        ' + m)
print('合う: %d / %d（飛ばした %d）' % (ok, ok + ng, skip))
