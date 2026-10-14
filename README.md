# ai_python_study

我的 Python + AI 学习仓库。

- **`ai/`** —— 用大模型 API 写的小应用（Streamlit 聊天机器人、API 调用示例）
- **`lei/`** —— 面向对象编程练习题（继承、多态、抽象类、魔法方法……）

## 目录结构

```
ai_python_study/
├── ai/                              AI 应用练习
│   ├── ai_parter_1.py               Streamlit 聊天机器人「蛋蛋」（调用 DeepSeek）
│   ├── deepseek测试.py               最小可运行的 DeepSeek API 调用示例
│   ├── streamlit入门.py              Streamlit 基础用法演示
│   └── resource/
│       └── 蛋.jpg                    页面 logo
├── lei/                             面向对象编程练习
│   ├── getter---setter.py           属性的封装（@property / setter）
│   ├── 继承---重写.py                继承与方法重写
│   ├── 多态.py                       多态
│   ├── 抽象类.py                     抽象类与抽象方法
│   ├── 类方法 实例方法 静态方法.py      三种方法类型的区别
│   ├── 魔法方法.py                   __init__ / __str__ 等魔术方法
│   ├── 二叉树.py                     二叉树（待补充）
│   ├── 练习.py                       综合练习
│   └── main.py                      练习入口
├── requirements.txt                 依赖清单
├── NOTES.md                         环境踩坑记录（Windows）
└── README.md
```

## 环境准备

需要 Python 3.10 以上，建议用虚拟环境 `.venv`。

```powershell
# 1. 创建虚拟环境
python -m venv .venv

# 2. 激活（每次开新终端都要做一次）
.\.venv\Scripts\Activate.ps1

# 3. 安装依赖
pip install -r requirements.txt
```

如果第 2 步报「禁止运行脚本」，先执行一次
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`。

## 配置 API Key

脚本从**环境变量或 Streamlit Secrets** 读取密钥，代码里不写任何密钥：

```powershell
# 本地开发：临时生效
$env:DEEPSEEK_API_KEY = "你的key"

# 本地开发：永久生效（设置完要重开终端）
setx DEEPSEEK_API_KEY "你的key"
```

Key 在 <https://platform.deepseek.com> 申请。仓库里不含密钥，公开也是安全的。

## 运行

```powershell
cd ai

# 聊天机器人（会自动打开浏览器 http://localhost:8501）
streamlit run ai_parter_1.py

# 入门演示页面
streamlit run streamlit入门.py

# 命令行调用一次大模型
python deepseek测试.py
```

## 部署到公网（让别人用网址体验）

用 [Streamlit Community Cloud](https://share.streamlit.io)，免费，直接从 GitHub 仓库部署：

1. 确认这个仓库是**公开**的。
2. 打开 <https://share.streamlit.io>，用 GitHub 账号登录，点 **Create app** → **Yup, I have an app**。
3. 填写：
   - Repository：`sleepgodfangxixi/ai_python_study`
   - Branch：`main`
   - Main file path：`ai/ai_parter_1.py`
4. 展开 **Advanced settings**，在 **Secrets** 里粘贴（TOML 格式）：

   ```toml
   DEEPSEEK_API_KEY = "sk-你的key"
   ```

5. 点 **Deploy**。等几分钟，就能拿到形如
   `https://xxx.streamlit.app` 的网址，发给任何人都能打开。

⚠️ **注意费用**：应用是公开的，但用的是**你自己的 API Key**，
所以别人聊天消耗的是你的余额。建议在 DeepSeek 平台只充少量金额，并定期看一眼用量。

密钥只存在 Streamlit 的服务器上，不会进仓库——`.streamlit/secrets.toml`
已经写进 `.gitignore`。

## 说明

- `ai/` 使用 `openai` 库，通过 `base_url="https://api.deepseek.com"` 指向 DeepSeek。
  它的接口与 OpenAI 兼容，所以换模型只要改 `model=` 那一个参数
  （`deepseek-flash` 是官方模型名，另有 `deepseek-v4-pro`）。
- `lei/` 是纯 Python，不依赖第三方库，直接 `python 文件名.py` 就能运行。
- Windows 上的环境坑（编码、GitHub 加速器证书）都记在 [NOTES.md](NOTES.md) 里。
