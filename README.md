# 任务清单管理应用

一个基于tkintertools和Lingma大模型的低代码开发桌面任务清单管理应用。

## 功能特性

- 创建和管理任务
- 设置任务截止日期和重要程度
- 番茄工作法计时器
- 主题切换（深色/浅色）
- 数据持久化存储

## 安装

1. 克隆或下载本项目
2. 安装依赖:


## 使用方法
1.测试
python -m pytest test_main.py -v
2.直接打包
pip install pyinstaller
pyinstaller --onefile --windowed --name=学习工具箱 --icon=task.ico main.py
3.脚本打包
python build.py
4.批量处理文件
package_app.bat


## 许可证

MIT License


