# Python 安装与配置

## 1. Python 版本选择

### 1.1 版本说明
- **Python 3.x**：当前主流版本，推荐使用
- **Python 2.x**：已停止维护，不推荐使用
- **最新稳定版**：Python 3.11 或 3.12（推荐）

### 1.2 版本检查
```bash
# 检查是否已安装 Python
python --version
python3 --version

# 检查 pip 版本
pip --version
pip3 --version
```

## 2. macOS 安装 Python

### 2.1 使用官方安装包
1. 访问 [Python 官网](https://www.python.org/downloads/)
2. 下载 macOS 安装包（.pkg 文件）
3. 运行安装包，按提示完成安装
4. 验证安装：
```bash
python3 --version
pip3 --version
```

### 2.2 使用 Homebrew（推荐）
```bash
# 安装 Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python
brew install python

# 验证安装
python3 --version
pip3 --version
```

### 2.3 使用 pyenv（版本管理）
```bash
# 安装 pyenv
brew install pyenv

# 配置环境变量（添加到 ~/.zshrc 或 ~/.bash_profile）
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# 重新加载配置
source ~/.zshrc

# 安装 Python 版本
pyenv install 3.11.5
pyenv install 3.12.0

# 设置全局版本
pyenv global 3.11.5

# 验证安装
python --version
```

## 3. Windows 安装 Python

### 3.1 使用官方安装包
1. 访问 [Python 官网](https://www.python.org/downloads/)
2. 下载 Windows 安装包（.exe 文件）
3. **重要**：勾选 "Add Python to PATH"
4. 选择 "Install Now" 或 "Customize installation"
5. 验证安装：
```cmd
python --version
pip --version
```

### 3.2 使用 Microsoft Store
1. 打开 Microsoft Store
2. 搜索 "Python"
3. 选择 Python 3.11 或 3.12
4. 点击 "获取" 进行安装

### 3.3 使用 Chocolatey
```powershell
# 安装 Chocolatey（如果未安装）
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 安装 Python
choco install python

# 验证安装
python --version
pip --version
```

## 4. Linux 安装 Python

### 4.1 Ubuntu/Debian
```bash
# 更新包列表
sudo apt update

# 安装 Python 3 和 pip
sudo apt install python3 python3-pip python3-venv

# 验证安装
python3 --version
pip3 --version

# 可选：设置 python 命令指向 python3
sudo apt install python-is-python3
```

### 4.2 CentOS/RHEL/Fedora
```bash
# CentOS/RHEL
sudo yum install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# 验证安装
python3 --version
pip3 --version
```

### 4.3 使用 pyenv（推荐）
```bash
# 安装依赖
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# 安装 pyenv
curl https://pyenv.run | bash

# 配置环境变量（添加到 ~/.bashrc）
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# 重新加载配置
source ~/.bashrc

# 安装 Python
pyenv install 3.11.5
pyenv global 3.11.5
```

## 5. 虚拟环境配置

### 5.1 为什么使用虚拟环境
- **隔离依赖**：不同项目使用不同版本的包
- **避免冲突**：防止包版本冲突
- **便于部署**：确保项目依赖的一致性

### 5.2 使用 venv（Python 内置）
```bash
# 创建虚拟环境
python3 -m venv myenv

# 激活虚拟环境
# macOS/Linux:
source myenv/bin/activate

# Windows:
myenv\Scripts\activate

# 验证激活
which python  # macOS/Linux
where python  # Windows

# 安装包
pip install requests

# 退出虚拟环境
deactivate
```

### 5.3 使用 virtualenv
```bash
# 安装 virtualenv
pip install virtualenv

# 创建虚拟环境
virtualenv myenv

# 激活虚拟环境
# macOS/Linux:
source myenv/bin/activate

# Windows:
myenv\Scripts\activate

# 退出虚拟环境
deactivate
```

### 5.4 使用 conda
```bash
# 安装 Miniconda 或 Anaconda
# 下载地址：https://docs.conda.io/en/latest/miniconda.html

# 创建虚拟环境
conda create -n myenv python=3.11

# 激活虚拟环境
conda activate myenv

# 安装包
conda install numpy pandas

# 退出虚拟环境
conda deactivate
```

## 6. IDE 和编辑器配置

### 6.1 VS Code 配置
1. 安装 VS Code
2. 安装 Python 扩展
3. 配置 Python 解释器：
   - 按 `Cmd+Shift+P`（macOS）或 `Ctrl+Shift+P`（Windows）
   - 输入 "Python: Select Interpreter"
   - 选择虚拟环境中的 Python 解释器

4. 推荐扩展：
   - Python
   - Python Docstring Generator
   - Python Indent
   - Python Type Hint
   - Pylance

### 6.2 PyCharm 配置
1. 下载并安装 PyCharm Community 或 Professional
2. 创建新项目时选择虚拟环境
3. 配置代码风格：
   - File → Settings → Editor → Code Style → Python
   - 设置缩进、行长度等

### 6.3 Jupyter Notebook
```bash
# 安装 Jupyter
pip install jupyter notebook

# 启动 Jupyter
jupyter notebook

# 或使用 JupyterLab
pip install jupyterlab
jupyter lab
```

## 7. 环境变量配置

### 7.1 macOS/Linux
```bash
# 编辑 ~/.zshrc 或 ~/.bashrc
nano ~/.zshrc

# 添加以下内容
export PATH="/usr/local/bin:$PATH"
export PYTHONPATH="/path/to/your/project:$PYTHONPATH"

# 重新加载配置
source ~/.zshrc
```

### 7.2 Windows
```powershell
# 设置环境变量
$env:PATH += ";C:\Python311\Scripts"
$env:PYTHONPATH = "C:\path\to\your\project"

# 永久设置（需要管理员权限）
[Environment]::SetEnvironmentVariable("PATH", $env:PATH, "User")
[Environment]::SetEnvironmentVariable("PYTHONPATH", "C:\path\to\your\project", "User")
```

## 8. 常见问题解决

### 8.1 Python 命令不存在
```bash
# macOS/Linux: 检查 PATH
echo $PATH

# 添加 Python 到 PATH
export PATH="/usr/local/bin:$PATH"

# Windows: 检查环境变量
echo %PATH%
```

### 8.2 pip 命令不存在
```bash
# 安装 pip
python -m ensurepip --upgrade

# 或下载 get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### 8.3 权限问题
```bash
# 使用用户安装
pip install --user package_name

# 或使用虚拟环境
python -m venv myenv
source myenv/bin/activate
pip install package_name
```

### 8.4 网络问题
```bash
# 使用国内镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name

# 永久配置镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 9. 项目结构建议

### 9.1 标准项目结构
```
my_project/
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
└── venv/  # 虚拟环境（不提交到版本控制）
```

### 9.2 requirements.txt 示例
```
requests==2.31.0
numpy>=1.24.0
pandas>=2.0.0
pytest>=7.0.0
```

### 9.3 .gitignore 示例
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

## 10. 验证安装

### 10.1 创建测试脚本
```python
# test_installation.py
import sys
import platform

print("Python 版本:", sys.version)
print("平台:", platform.platform())
print("架构:", platform.architecture())

# 测试常用库
try:
    import requests
    print("✓ requests 库可用")
except ImportError:
    print("✗ requests 库不可用")

try:
    import numpy
    print("✓ numpy 库可用")
except ImportError:
    print("✗ numpy 库不可用")

try:
    import pandas
    print("✓ pandas 库可用")
except ImportError:
    print("✗ pandas 库不可用")
```

### 10.2 运行测试
```bash
# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate     # Windows

# 运行测试
python test_installation.py
```

## 11. 总结

本章介绍了 Python 开发环境的完整搭建过程：

1. **Python 安装**：不同操作系统的安装方法
2. **虚拟环境**：项目隔离和依赖管理
3. **IDE 配置**：开发工具的选择和配置
4. **环境变量**：系统配置和路径设置
5. **项目结构**：标准化的项目组织方式
6. **问题解决**：常见问题的解决方法

正确配置开发环境是 Python 学习的第一步，为后续的学习和开发打下坚实的基础。
