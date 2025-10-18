# pip 包管理

## 1. pip 简介

pip（Pip Installs Packages）是 Python 的官方包管理工具，用于安装和管理 Python 包。

### 1.1 pip 的特点
- **官方工具**：Python 官方推荐的包管理工具
- **简单易用**：命令行界面，操作简单
- **功能完整**：支持安装、卸载、升级、搜索等操作
- **依赖管理**：自动处理包依赖关系

### 1.2 pip 版本检查
```bash
# 检查 pip 版本
pip --version
pip3 --version

# 升级 pip
pip install --upgrade pip
```

## 2. 基础操作

### 2.1 安装包
```bash
# 安装最新版本
pip install requests

# 安装指定版本
pip install requests==2.31.0

# 安装版本范围
pip install "requests>=2.30.0,<3.0.0"

# 从 requirements.txt 安装
pip install -r requirements.txt

# 安装开发依赖
pip install -e .  # 安装当前目录的包（开发模式）
```

### 2.2 卸载包
```bash
# 卸载包
pip uninstall requests

# 卸载多个包
pip uninstall requests numpy pandas

# 从 requirements.txt 卸载
pip uninstall -r requirements.txt
```

### 2.3 升级包
```bash
# 升级包
pip install --upgrade requests

# 升级所有包
pip list --outdated  # 查看过时的包
pip install --upgrade package_name

# 升级 pip 本身
pip install --upgrade pip
```

### 2.4 查看包信息
```bash
# 列出已安装的包
pip list

# 查看包详细信息
pip show requests

# 查看过时的包
pip list --outdated

# 查看包依赖
pip show --verbose requests
```

## 3. 搜索和查找

### 3.1 搜索包
```bash
# 搜索包
pip search requests  # 注意：此功能已被禁用

# 使用 PyPI 网站搜索
# 访问 https://pypi.org/ 进行搜索
```

### 3.2 查看包信息
```bash
# 查看包信息
pip show requests

# 输出示例：
# Name: requests
# Version: 2.31.0
# Summary: Python HTTP for Humans.
# Home-page: https://requests.readthedocs.io
# Author: Kenneth Reitz
# Author-email: me@kennethreitz.com
# License: Apache 2.0
# Location: /usr/local/lib/python3.11/site-packages
# Requires: urllib3, certifi, charset-normalizer, idna
```

## 4. 依赖管理

### 4.1 requirements.txt
```bash
# 生成 requirements.txt
pip freeze > requirements.txt

# 安装 requirements.txt 中的包
pip install -r requirements.txt

# requirements.txt 示例
requests==2.31.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
```

### 4.2 依赖解析
```bash
# 检查依赖冲突
pip check

# 查看包依赖树
pip show --verbose package_name
```

### 4.3 约束文件
```bash
# 创建约束文件
pip freeze > constraints.txt

# 使用约束文件安装
pip install -c constraints.txt package_name
```

## 5. 虚拟环境

### 5.1 创建虚拟环境
```bash
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境
# macOS/Linux:
source myenv/bin/activate

# Windows:
myenv\Scripts\activate

# 在虚拟环境中安装包
pip install requests
```

### 5.2 虚拟环境管理
```bash
# 查看虚拟环境中的包
pip list

# 生成虚拟环境的 requirements.txt
pip freeze > requirements.txt

# 退出虚拟环境
deactivate
```

## 6. 配置和优化

### 6.1 pip 配置文件
创建 `~/.pip/pip.conf`（Linux/macOS）或 `%APPDATA%\pip\pip.ini`（Windows）：
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
timeout = 120
retries = 5

[install]
user = true
upgrade-strategy = only-if-needed

[list]
format = columns
```

### 6.2 镜像源配置
```bash
# 临时使用镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

# 永久配置镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 常用镜像源
# 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云：https://mirrors.aliyun.com/pypi/simple/
# 中科大：https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣：https://pypi.douban.com/simple/
```

### 6.3 缓存管理
```bash
# 查看缓存位置
pip cache dir

# 查看缓存信息
pip cache info

# 清理缓存
pip cache purge

# 禁用缓存
pip install --no-cache-dir requests
```

## 7. 高级功能

### 7.1 从不同源安装
```bash
# 从 Git 仓库安装
pip install git+https://github.com/user/repo.git

# 从本地目录安装
pip install /path/to/local/package

# 从 wheel 文件安装
pip install package.whl

# 从 tar.gz 文件安装
pip install package.tar.gz
```

### 7.2 开发模式安装
```bash
# 开发模式安装（可编辑安装）
pip install -e .

# 从 Git 仓库开发模式安装
pip install -e git+https://github.com/user/repo.git#egg=package
```

### 7.3 用户安装
```bash
# 安装到用户目录
pip install --user requests

# 查看用户安装的包
pip list --user
```

## 8. 故障排除

### 8.1 常见问题
```bash
# 权限问题
pip install --user package_name

# 网络问题
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org package_name

# 版本冲突
pip install --force-reinstall package_name

# 清理并重新安装
pip uninstall package_name
pip install package_name
```

### 8.2 调试信息
```bash
# 显示详细输出
pip install -v requests

# 显示调试信息
pip install -vv requests

# 显示安装日志
pip install --log install.log requests
```

## 9. 最佳实践

### 9.1 项目依赖管理
```bash
# 1. 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 2. 安装项目依赖
pip install -r requirements.txt

# 3. 开发时安装开发依赖
pip install -r requirements-dev.txt

# 4. 生成锁定文件
pip freeze > requirements-lock.txt
```

### 9.2 requirements.txt 最佳实践
```txt
# 生产依赖
requests==2.31.0
numpy>=1.24.0,<2.0.0
pandas>=2.0.0,<3.0.0

# 开发依赖（requirements-dev.txt）
pytest>=7.0.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.0.0
```

### 9.3 版本管理策略
```bash
# 使用精确版本（生产环境）
requests==2.31.0

# 使用兼容版本（开发环境）
requests>=2.30.0,<3.0.0

# 使用最新版本（实验性）
requests>=2.31.0
```

## 10. 与其他工具集成

### 10.1 与 conda 集成
```bash
# 在 conda 环境中使用 pip
conda create -n myenv python=3.11
conda activate myenv
pip install requests
```

### 10.2 与 Poetry 集成
```bash
# Poetry 项目中使用 pip
poetry shell
pip install additional-package
```

### 10.3 与 Docker 集成
```dockerfile
# Dockerfile 示例
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "app.py"]
```

## 11. 总结

本章介绍了 pip 包管理的完整内容：

1. **基础操作**：安装、卸载、升级、查看
2. **依赖管理**：requirements.txt、约束文件
3. **虚拟环境**：创建、激活、管理
4. **配置优化**：镜像源、缓存、配置文件
5. **高级功能**：不同源安装、开发模式
6. **故障排除**：常见问题和解决方法
7. **最佳实践**：项目依赖管理策略

pip 是 Python 开发中必不可少的工具，掌握其使用方法对 Python 学习至关重要。
