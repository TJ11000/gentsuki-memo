#!/bin/bash
# 試験: tests/cases.tsv の入口を 1 回目だけ回して、出た色と期待する色を並べる。
# 使い方: このフォルダの一つ上（genki_memo）で  bash tests/run.sh
# 要るもの: Claude Code（claude コマンド）。1 本ずつ順に回す（同じフォルダで並べて回すと会話が混ざるため）。
cd "$(dirname "$0")/.."
out=tests/out
mkdir -p "$out"
pass=0; total=0
printf "%-40s  期待  出た  判定\n" "入口"
while IFS=$'\t' read -r input expect; do
  [ -z "$input" ] && continue
  total=$((total+1))
  ans=$(printf '%s\n' "$input" | claude -p --setting-sources project)
  printf '%s\n' "$ans" > "$out/$total.txt"
  got="なし"
  for c in 🔴 🟡 🟢; do
    if printf '%s' "$ans" | head -5 | grep -q "$c"; then got="$c"; break; fi
  done
  if [ "$got" = "$expect" ]; then mark="合う"; pass=$((pass+1)); else mark="合わん"; fi
  printf "%-40s  %s    %s    %s\n" "$input" "$expect" "$got" "$mark"
done < tests/cases.tsv
echo "合う: $pass / $total（出力の全文は tests/out/）"
