#!/bin/bash
chkpt() {
  local label="$1"
  local ts
  ts=$(date -u +%H:%M:%S)
  echo "$ts $label" >> trace.log
  git add trace.log 2>/dev/null
  git commit -m "chkpt: $label $ts" --allow-empty 2>&1 | tail -1
  git push 2>&1 | tail -1
}
export -f chkpt
