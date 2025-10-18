# Python 学习计划

## 学习背景

作为一名擅长 .NET 开发的工程师，我注意到近年来人工智能（AI）技术的迅猛发展，期望通过学习 Python 来拓展技能领域。由于 Python 在 AI 和数据科学领域的广泛应用，掌握这门语言将有助于在新兴技术领域中保持竞争力。

由于不希望从枯燥的语法学习开始，我计划通过项目驱动的方式逐步掌握 Python，并且希望学习曲线与 .NET 相似，了解 Python 中与 .NET 框架和组件对应的工具，如 ABP、Furion、SQLSugar、EF Core、StackExchange.Redis 等。此外，我还希望了解 .NET 中的概念（如管道、中间件、身份认证）在 Python 中的实现方式，最终通过学习完成一个有趣的 Python 项目。

## 学习目标

1. **掌握 Python 语言基础**：通过项目实践，熟悉 Python 的语法和特性
2. **了解 Python 中的主流框架和组件**：学习与 .NET 中 ABP、Furion、SQLSugar、EF Core、StackExchange.Redis 等对应的 Python 工具
3. **理解 .NET 概念在 Python 中的实现**：探索管道、中间件、身份认证等概念在 Python 中的应用
4. **完成一个实际的 Python 项目**：通过项目实践，巩固所学知识，提升开发能力

## .NET 与 Python 生态系统对比

| .NET 组件 | Python 对应组件 | 说明 |
|-----------|----------------|------|
| **Web 框架** | | |
| ABP Framework | Django | 全功能 Web 框架，内置管理后台、认证等 |
| Furion | FastAPI | 现代化、高性能的 Web 框架 |
| ASP.NET Core | Flask | 轻量级、灵活的 Web 框架 |
| **ORM 工具** | | |
| Entity Framework Core | SQLAlchemy | 功能强大的 ORM 框架 |
| SqlSugar | Django ORM | 简单易用的 ORM |
| **缓存** | | |
| StackExchange.Redis | redis-py | Redis 客户端库 |
| **消息队列** | | |
| MassTransit | Celery | 分布式任务队列 |
| **身份认证** | | |
| ASP.NET Core Identity | Django Auth | 用户认证和授权系统 |
| JWT Bearer | PyJWT | JWT 令牌处理 |
| **依赖注入** | | |
| Microsoft.Extensions.DependencyInjection | dependency-injector | 依赖注入容器 |
| **配置管理** | | |
| IConfiguration | python-decouple | 配置管理 |
| **日志** | | |
| Serilog | loguru | 结构化日志记录 |
| **测试** | | |
| xUnit | pytest | 单元测试框架 |

## 学习计划

### 第一阶段：Python 基础与环境搭建（第 1-2 周）

**学习内容：**
- Python 基础语法：变量、数据类型、控制结构、函数、类等
- Python 开发环境搭建：安装 Python 解释器、使用虚拟环境、配置 IDE（PyCharm、VS Code）
- 包管理：pip、conda、poetry
- 代码风格：PEP 8、black、flake8

**实践任务：**
- 编写简单的 Python 脚本，熟悉语法和运行环境
- 搭建开发环境，确保能够顺利运行 Python 程序
- 完成 5-10 个基础练习项目（计算器、文件处理等）

### 第二阶段：Web 开发框架学习（第 3-5 周）

**学习内容：**
- **Django**：全功能 Web 框架（类似 ABP）
  - 模型（Models）- 类似 EF Core 的 Code First
  - 视图（Views）- 类似 Controller
  - 模板（Templates）- 类似 Razor Pages
  - 管理后台（Admin）- 类似 ABP 的自动生成管理界面
  - 中间件（Middleware）- 类似 ASP.NET Core 中间件
  - 认证系统（Authentication）- 类似 ASP.NET Core Identity

- **FastAPI**：现代化 Web 框架（类似 Furion）
  - 自动 API 文档生成
  - 类型提示和验证
  - 异步支持
  - 依赖注入

- **Flask**：轻量级框架（类似 ASP.NET Core）
  - 路由系统
  - 模板引擎
  - 扩展系统

**实践任务：**
- 使用 Django 创建简单的博客系统
- 使用 FastAPI 创建 RESTful API
- 使用 Flask 创建简单的 Web 应用

### 第三阶段：数据库与 ORM（第 6-7 周）

**学习内容：**
- **SQLAlchemy**：功能强大的 ORM（类似 EF Core）
  - Core 和 ORM 的区别
  - 模型定义和关系映射
  - 查询构建器
  - 迁移系统（Alembic）

- **Django ORM**：简单易用的 ORM（类似 SqlSugar）
  - 模型定义
  - 查询集（QuerySet）
  - 迁移系统

- **数据库连接**：
  - PostgreSQL（类似 SQL Server）
  - MySQL
  - SQLite（开发环境）

**实践任务：**
- 使用 SQLAlchemy 设计数据库模型
- 实现 CRUD 操作
- 学习数据库迁移

### 第四阶段：缓存与消息队列（第 8 周）

**学习内容：**
- **Redis**：
  - redis-py 客户端（类似 StackExchange.Redis）
  - 缓存策略
  - 会话存储
  - 发布/订阅模式

- **Celery**：分布式任务队列（类似 MassTransit）
  - 任务定义和执行
  - 消息代理（Redis、RabbitMQ）
  - 定时任务
  - 监控和管理

**实践任务：**
- 集成 Redis 缓存
- 实现异步任务处理
- 设置定时任务

### 第五阶段：身份认证与安全（第 9 周）

**学习内容：**
- **Django 认证系统**：
  - 用户模型
  - 权限和组
  - 会话管理
  - 自定义认证后端

- **JWT 认证**：
  - PyJWT 库
  - 令牌生成和验证
  - 刷新令牌机制

- **OAuth 2.0**：
  - Authlib 库
  - 第三方登录集成

**实践任务：**
- 实现用户注册和登录
- 添加 JWT 认证
- 集成第三方登录（Google、GitHub）

### 第六阶段：高级概念与最佳实践（第 10-11 周）

**学习内容：**
- **依赖注入**：
  - dependency-injector
  - FastAPI 的依赖系统

- **配置管理**：
  - python-decouple
  - 环境变量管理

- **日志记录**：
  - loguru
  - 结构化日志

- **测试**：
  - pytest
  - 单元测试和集成测试
  - 测试覆盖率

- **API 文档**：
  - Swagger/OpenAPI
  - FastAPI 自动文档生成

**实践任务：**
- 重构项目，应用最佳实践
- 编写完整的测试套件
- 生成 API 文档

### 第七阶段：项目实践（第 12-16 周）

**项目选择：基于 Markdown 的博客系统**

## 项目推荐：基于 Markdown 的博客系统

### 项目概述

开发一个基于 Markdown 的现代化博客系统，支持 Markdown 文件管理、自动解析、标签分类、搜索功能等。这个项目将让您专注于 Python 后端开发，同时 Markdown 的简单性让内容管理更加便捷。

### 核心功能

1. **Markdown 文章管理**
   - Markdown 文件上传和解析
   - 文章创建、编辑、删除
   - 自动提取文章元数据（标题、日期、标签等）
   - 文章预览和发布状态管理

2. **内容展示**
   - 文章列表和分页
   - 文章详情页面
   - 标签分类和归档
   - 搜索功能（全文搜索）

3. **用户系统**
   - 用户注册和登录
   - 权限管理（管理员、作者、访客）
   - 个人资料管理

4. **管理功能**
   - 后台管理界面
   - 文章统计和分析
   - 评论系统（可选）
   - RSS 订阅

5. **高级功能**
   - 文章缓存优化
   - 图片上传和管理
   - 代码高亮
   - 文章分享功能

### 技术栈

**后端：**
- **Web 框架**：FastAPI（现代化、高性能，自动生成 API 文档）
- **ORM**：SQLAlchemy（功能强大的 ORM）
- **数据库**：PostgreSQL（生产环境）+ SQLite（开发环境）
- **缓存**：Redis（文章缓存、会话存储）
- **文件处理**：python-markdown（Markdown 解析）
- **搜索**：Whoosh（全文搜索）或 Elasticsearch
- **认证**：JWT + OAuth 2.0
- **文件存储**：本地存储或云存储（AWS S3、阿里云 OSS）

**前端：**
- **框架**：React 或 Vue.js
- **UI 库**：Ant Design 或 Material-UI
- **Markdown 渲染**：react-markdown 或 vue-markdown
- **代码高亮**：prism.js 或 highlight.js
- **编辑器**：Monaco Editor 或 CodeMirror

**部署：**
- **容器化**：Docker + Docker Compose
- **Web 服务器**：Nginx
- **云服务**：AWS、Azure 或阿里云
- **CI/CD**：GitHub Actions

### 项目亮点

1. **技术全面性**：涵盖 Web 开发、数据库、文件处理、缓存、搜索等各个方面
2. **实用性强**：可以真正用于个人博客或团队博客
3. **Markdown 友好**：支持 Markdown 语法，写作体验好
4. **现代化架构**：使用最新的技术栈和最佳实践
5. **可扩展性**：模块化设计，便于后续功能扩展
6. **SEO 友好**：支持静态页面生成，搜索引擎优化

### 学习价值

通过这个项目，您将学会：
- Python Web 开发的完整流程
- FastAPI 框架的使用和最佳实践
- 数据库设计和 ORM 操作
- 文件处理和 Markdown 解析
- 缓存策略和性能优化
- 全文搜索的实现
- 前后端分离开发
- 项目部署和运维
- API 设计和文档生成

### 项目里程碑

**第 12 周**：项目规划和环境搭建
- 项目结构设计
- 开发环境搭建
- 数据库模型设计
- 基础 API 框架搭建

**第 13 周**：核心功能开发
- Markdown 文件解析和存储
- 文章 CRUD 操作
- 用户认证系统
- 基础 API 接口

**第 14 周**：高级功能实现
- 标签系统和分类
- 全文搜索功能
- 缓存优化
- 文件上传和管理

**第 15 周**：前端开发
- 前端框架搭建
- 文章列表和详情页面
- 管理后台界面
- Markdown 编辑器集成

**第 16 周**：优化和部署
- 性能优化
- 测试编写
- 项目部署
- 文档完善

## 学习资源

### 官方文档
- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/zh/)
- [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/zh/)
- [Python-Markdown 官方文档](https://python-markdown.github.io/)
- [Whoosh 搜索库文档](https://whoosh.readthedocs.io/)

### 推荐书籍
- 《Python 编程：从入门到实践》
- 《FastAPI 实战指南》
- 《Flask Web 开发实战》
- 《Python 网络爬虫权威指南》

### 在线课程
- Python 官方教程
- FastAPI 官方教程
- Django Girls 教程
- Markdown 语法教程

### 项目相关资源
- [Markdown 语法指南](https://www.markdownguide.org/)
- [FastAPI 项目模板](https://github.com/tiangolo/full-stack-fastapi-template)
- [SQLAlchemy 最佳实践](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [Redis Python 客户端文档](https://redis-py.readthedocs.io/)

### 实践平台
- LeetCode（算法练习）
- HackerRank（编程挑战）
- GitHub（开源项目学习）
- Stack Overflow（问题解答）

### 参考项目
- [Hugo](https://gohugo.io/) - 静态站点生成器
- [Jekyll](https://jekyllrb.com/) - 静态博客生成器
- [Ghost](https://ghost.org/) - 现代博客平台
- [Hexo](https://hexo.io/) - 静态博客框架

## 学习进度跟踪

- [ ] 第一阶段：Python 基础与环境搭建
- [ ] 第二阶段：Web 开发框架学习
- [ ] 第三阶段：数据库与 ORM
- [ ] 第四阶段：缓存与消息队列
- [ ] 第五阶段：身份认证与安全
- [ ] 第六阶段：高级概念与最佳实践
- [ ] 第七阶段：项目实践

---

*这个学习计划将帮助我从 .NET 开发者的角度，系统性地学习 Python 开发，最终完成一个有趣且实用的项目。*
