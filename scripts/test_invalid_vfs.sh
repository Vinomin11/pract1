#!/bin/bash
# Тест: запуск с несуществующим файлом VFS
python3 src/shell_emulator.py \
    --vfs-path vfs/nonexistent.xml \
    --script-path scripts/script_default.txt
