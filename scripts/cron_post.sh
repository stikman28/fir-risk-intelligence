#!/bin/bash
# FIR Risk Social Post — cron wrapper
# Usage: cron_post.sh <platform> <file>
# Example: cron_post.sh linkedin intel/2026-03-26-risk-profile-inversion.md

PLATFORM="$1"
FILE="$2"
XPYTHON="/Users/stikman/Projects/ai-assistant/AIQToolkit/.venv/bin/python3"
REPO="/Users/stikman/Projects/ai-assistant/fir-risk-intelligence"
LOG="/tmp/fir-social-$(date +%Y%m%d-%H%M%S)-${PLATFORM}.log"

cd "$REPO" || exit 1

echo "$(date): Posting $FILE to $PLATFORM" >> "$LOG"

if [ "$PLATFORM" = "linkedin" ]; then
    "$XPYTHON" scripts/post_to_linkedin.py "$FILE" >> "$LOG" 2>&1
elif [ "$PLATFORM" = "x" ]; then
    "$XPYTHON" scripts/post_to_x.py "$FILE" >> "$LOG" 2>&1
else
    echo "Unknown platform: $PLATFORM" >> "$LOG"
    exit 1
fi

echo "$(date): Done" >> "$LOG"
