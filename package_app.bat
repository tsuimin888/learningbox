@echo off
echo 正在打包任务清单应用...

REM 安装依赖
echo 正在安装依赖...
pip install -r requirements.txt

REM 运行测试
echo 正在运行测试...
python -m pytest test_main.py -v

REM 打包应用
echo 正在打包应用...
python build.py

echo.
echo 打包完成！
echo 可执行文件位于 dist/任务清单.exe
pause