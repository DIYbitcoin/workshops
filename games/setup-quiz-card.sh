#!/bin/bash
# Wipe the card in the reader and set it up for the SeedKeeper quiz.
# Run it once per card from the folder that holds SeedKeeper-v0.2-0.1.cap.

PIN="2048"
QUESTION="Approximately how many minutes apart are blocks?"

HERE=$(cd "$(dirname "$0")" && pwd)
CAP=SeedKeeper-v0.2-0.1.cap
VENV=~/.venvs/seedkeeper-quiz

if [ ! -f "$CAP" ]; then echo "STOP: $CAP is not in this folder"; exit 1; fi
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV" && "$VENV/bin/pip" -q install pysatochip==0.18.7 || exit 1
fi

serial=$(gp --info 2>&1 | grep -m1 -oE "ICSerialNumber=[0-9A-F]+" | cut -d= -f2)
if [ -z "$serial" ]; then echo "STOP: no card read"; exit 1; fi

# Remove every package except the factory one
for pkg in $(gp --list 2>&1 | grep -oE "^PKG: [0-9A-F]+" | cut -d' ' -f2 | grep -vx A0000001515350); do
  gp --delete "$pkg" -f > /dev/null 2>&1
done
left=$(gp --list 2>&1 | grep -E "^(APP|PKG)" | grep -v "A0000001515350")
if [ -n "$left" ]; then echo "STOP: card $serial could not be wiped"; echo "$left"; exit 1; fi

gp --install "$CAP" 2>&1 | grep -E "rror"
echo "card $serial: $("$VENV/bin/python" -I "$HERE/quiz-card.py" "$PIN" "$QUESTION" 2>&1 | tail -1)"
