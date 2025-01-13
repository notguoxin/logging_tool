@echo off
rmdir /s /q dist
python -m build --wheel .