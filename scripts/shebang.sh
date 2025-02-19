#!/bin/bash

# 指定されたシバンに置換するスクリプト
if [ -z "$1" ]; then
    echo "Usage: $0 <new_shebang>"
    exit 1
fi

NEW_SHEBANG="#!$1"
TARGET_DIR="./ffaicu"
OLD_SHEBANG='#!/usr/local/bin/perl --'

# 対象フォルダ内のすべてのファイルを処理
find "$TARGET_DIR" -type f | while read -r file; do
    if grep -q "^$OLD_SHEBANG" "$file"; then
        echo "Updating shebang in: $file"
        sed -i "1s|^$OLD_SHEBANG|$NEW_SHEBANG|" "$file"
    fi
done

echo "Shebang update complete."
