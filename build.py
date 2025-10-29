"""
应用打包脚本
"""
import os
import sys
import subprocess
import shutil

def install_requirements():
    """安装打包依赖"""
    print("正在安装打包依赖...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """构建可执行文件"""
    print("正在构建可执行文件...")
    
    # 使用PyInstaller打包
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=学习工具箱",
        "--icon=task.ico",
        "--add-data=task.ico;.",
        "--add-data=config.json;.",
        "--add-data=theme.json;.",
        "--add-data=tasks.json;.",
        "main.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("打包成功！")
    except subprocess.CalledProcessError as e:
        print(f"打包失败: {e}")
        return False
    
    return True

def create_installer():
    """创建安装程序（可选）"""
    print("正在创建安装程序...")
    
    # 如果有Inno Setup，可以创建安装程序
    iss_content = """
[Setup]
AppName=任务清单
AppVersion=1.0
DefaultDirName={pf}\\任务清单
DefaultGroupName=任务清单
UninstallDisplayIcon={app}\\任务清单.exe
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\\任务清单.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "theme.json"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\\任务清单"; Filename: "{app}\\任务清单.exe"
Name: "{group}\\卸载任务清单"; Filename: "{uninstallexe}"
Name: "{commondesktop}\\任务清单"; Filename: "{app}\\任务清单.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
"""
    
    with open("setup.iss", "w", encoding="utf-8") as f:
        f.write(iss_content)
    
    print("已生成Inno Setup安装脚本 setup.iss")

def main():
    """主函数"""
    print("开始打包任务清单应用...")
    
    # 安装依赖
    install_requirements()
    
    # 构建可执行文件
    if build_executable():
        print("可执行文件已生成到 dist/ 目录")
        
        # 创建安装程序脚本
        create_installer()
        
        print("打包完成！")
        print("运行文件位置: dist/任务清单.exe")
    else:
        print("打包失败！")

if __name__ == "__main__":
    main()