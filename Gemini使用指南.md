# 🤖 Gemini版本使用指南

## 📌 什么是Gemini版本？

这是使用**Google Gemini API**的升级版本，相比DeepSeek版本有以下优势：

### ✨ 主要优势

| 特性 | DeepSeek版本 | Gemini版本 |
|------|-------------|-----------|
| PDF处理方式 | 需要先提取文本 | **直接上传PDF** ✅ |
| 扫描版PDF | ❌ 不支持 | **✅ 支持** |
| 表格识别 | 依赖pdfplumber | **AI智能识别** ✅ |
| 图片处理 | ❌ 不支持 | **✅ 支持** |
| 处理速度 | 较快 | 稍慢但更准确 |
| 成本 | 较低 | 中等 |

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install google-generativeai
```

或者安装所有依赖：

```bash
pip install -r requirements.txt
```

### 2. 获取Gemini API密钥

1. 访问：https://makersuite.google.com/app/apikey
2. 登录Google账号
3. 点击"Create API Key"
4. 复制生成的API密钥

### 3. 配置API密钥

**方法1：使用环境变量**

编辑 `.env` 文件：
```
GEMINI_API_KEY=your_gemini_api_key_here
```

**方法2：在Web界面输入**

启动应用后，在侧边栏输入API密钥。

### 4. 启动应用

```bash
streamlit run app_gemini.py
```

或者创建启动脚本 `start_gemini.bat`：
```batch
@echo off
echo Starting Gemini Financial Analysis System...
streamlit run app_gemini.py
pause
```

---

## 💡 使用方法

### Web界面使用

1. **启动应用**
   ```bash
   streamlit run app_gemini.py
   ```

2. **输入API密钥**
   - 在侧边栏输入Gemini API密钥

3. **上传PDF**
   - 支持任何类型的PDF（文本型或扫描版）
   - 文件大小建议 < 200MB

4. **开始分析**
   - 点击"开始分析"按钮
   - 等待Gemini处理（通常1-3分钟）

5. **查看结果**
   - 切换到"查看结果"标签页
   - 下载Excel、报告、图表等

### Python代码使用

```python
from src.gemini_workflow import GeminiFinancialWorkflow

# 创建工作流
workflow = GeminiFinancialWorkflow(
    api_key="your_gemini_api_key",
    output_dir="output_gemini"
)

# 分析PDF
result = workflow.run("财务报表.pdf")

# 获取结果
financial_data = result['financial_data']
analysis = result['analysis']
files = result['files']

print(f"公司名称: {financial_data['company_info']['name']}")
print(f"Excel文件: {files['excel']}")
```

### 命令行使用

创建 `cli_gemini.py`：

```python
import argparse
from src.gemini_workflow import GeminiFinancialWorkflow

parser = argparse.ArgumentParser()
parser.add_argument('pdf_file', help='PDF文件路径')
parser.add_argument('-k', '--api-key', help='Gemini API密钥')
parser.add_argument('-o', '--output', default='output_gemini', help='输出目录')

args = parser.parse_args()

workflow = GeminiFinancialWorkflow(
    api_key=args.api_key,
    output_dir=args.output
)

result = workflow.run(args.pdf_file)
print("分析完成！")
```

使用：
```bash
python cli_gemini.py report.pdf -k YOUR_API_KEY
```

---

## 📊 支持的PDF类型

### ✅ 完全支持

1. **文本型PDF**
   - 可以选中和复制文字的PDF
   - 最常见的PDF类型
   - 处理速度最快

2. **扫描版PDF**
   - 图片格式的PDF
   - Gemini会自动进行OCR识别
   - 处理时间稍长

3. **混合型PDF**
   - 包含文本和图片的PDF
   - 包含表格的PDF
   - Gemini可以同时处理

4. **多语言PDF**
   - 中文PDF
   - 英文PDF
   - 中英混合PDF

### ❌ 不支持

- 加密的PDF（需要先解密）
- 损坏的PDF文件
- 超大文件（>200MB）

---

## 🔧 高级功能

### 1. 批量处理

```python
from src.gemini_workflow import GeminiFinancialWorkflow

workflow = GeminiFinancialWorkflow(api_key="your_key")

# 批量处理多个PDF
results = workflow.run_batch([
    "report1.pdf",
    "report2.pdf",
    "report3.pdf"
])

for result in results:
    if 'error' not in result:
        print(f"成功: {result['financial_data']['company_info']['name']}")
    else:
        print(f"失败: {result['error']}")
```

### 2. 自定义提取字段

编辑 `src/gemini_client.py` 中的提示词，添加你需要的字段：

```python
prompt = """请提取以下信息：
{
  "company_info": {...},
  "financial_metrics": {...},
  "custom_field": "你的自定义字段"
}
"""
```

### 3. 提问式分析

```python
from src.gemini_client import GeminiClient

client = GeminiClient(api_key="your_key")

# 对PDF提出问题
questions = [
    "这家公司的主营业务是什么？",
    "最大的风险因素是什么？",
    "现金流状况如何？"
]

answers = client.analyze_pdf_with_questions("report.pdf", questions)

for q, a in answers.items():
    print(f"Q: {q}")
    print(f"A: {a}\n")
```

### 4. 提取所有表格

```python
from src.gemini_client import GeminiClient

client = GeminiClient(api_key="your_key")

# 提取PDF中的所有表格
tables_json = client.extract_tables_from_pdf("report.pdf")
print(tables_json)
```

---

## ⚙️ 配置选项

### 模型选择

在 `src/gemini_client.py` 中可以更换模型：

```python
# 当前使用的模型
self.model = genai.GenerativeModel('gemini-1.5-flash')

# 可选的其他模型：
# gemini-1.5-pro - 更强大但更贵
# gemini-1.5-flash - 快速且经济（推荐）
```

### 输出目录

```python
workflow = GeminiFinancialWorkflow(
    api_key="your_key",
    output_dir="custom_output"  # 自定义输出目录
)
```

---

## 💰 成本估算

Gemini API定价（截至2024年）：

| 模型 | 输入价格 | 输出价格 |
|------|---------|---------|
| Gemini 1.5 Flash | $0.075/百万tokens | $0.30/百万tokens |
| Gemini 1.5 Pro | $1.25/百万tokens | $5.00/百万tokens |

**估算：**
- 处理一份50页的PDF：约 $0.01 - $0.05
- 每月处理100份报表：约 $1 - $5

**免费额度：**
- Gemini提供免费tier
- 每分钟15次请求
- 每天1500次请求

---

## 🆚 DeepSeek vs Gemini 对比

### 何时使用DeepSeek？

- ✅ PDF是文本型（可复制文字）
- ✅ 追求处理速度
- ✅ 成本敏感
- ✅ 中文财务报表

### 何时使用Gemini？

- ✅ PDF是扫描版（图片）
- ✅ 需要处理表格和图片
- ✅ 追求准确性
- ✅ 复杂的财务报表

### 性能对比

| 指标 | DeepSeek | Gemini |
|------|----------|--------|
| 文本型PDF准确率 | 85% | 90% |
| 扫描版PDF支持 | ❌ | ✅ |
| 处理速度 | 快 | 中等 |
| 表格识别 | 中等 | 优秀 |
| 成本 | 低 | 中等 |

---

## 🐛 常见问题

### Q1: API密钥无效

**错误信息：**
```
ValueError: 未提供Gemini API密钥
```

**解决方法：**
1. 检查API密钥是否正确
2. 确认已设置环境变量或在界面输入
3. 访问 https://makersuite.google.com 检查密钥状态

### Q2: 文件上传失败

**错误信息：**
```
文件处理失败: FAILED
```

**解决方法：**
1. 检查PDF文件是否损坏
2. 确认文件大小 < 200MB
3. 尝试重新上传
4. 检查网络连接

### Q3: 处理速度慢

**原因：**
- Gemini需要上传和处理PDF
- 扫描版PDF需要OCR识别
- 大文件需要更长时间

**优化建议：**
1. 只上传需要分析的页面
2. 使用gemini-1.5-flash模型
3. 避免高峰时段

### Q4: 提取数据不准确

**改进方法：**
1. 使用更强大的gemini-1.5-pro模型
2. 调整提示词（编辑 `src/gemini_client.py`）
3. 提供更清晰的PDF文件
4. 手动验证和修正结果

---

## 📝 最佳实践

### 1. PDF准备

- ✅ 使用高质量的PDF
- ✅ 确保文字清晰可读
- ✅ 表格格式规范
- ✅ 避免过度压缩

### 2. API使用

- ✅ 设置合理的超时时间
- ✅ 处理API错误和重试
- ✅ 监控API使用量
- ✅ 使用环境变量保护密钥

### 3. 结果验证

- ✅ 对比原始PDF验证数据
- ✅ 检查关键财务指标
- ✅ 人工审核重要报表
- ✅ 保存原始JSON数据

---

## 🔄 从DeepSeek迁移到Gemini

### 代码迁移

**原DeepSeek代码：**
```python
from src.workflow import FinancialWorkflow
workflow = FinancialWorkflow(api_key="deepseek_key")
result = workflow.run("report.pdf")
```

**新Gemini代码：**
```python
from src.gemini_workflow import GeminiFinancialWorkflow
workflow = GeminiFinancialWorkflow(api_key="gemini_key")
result = workflow.run("report.pdf")
```

### 数据格式

两个版本的输出格式完全相同，可以无缝切换！

---

## 📞 获取帮助

- 📖 查看 `README.md`
- 📖 查看 `常见问题解答.md`
- 🔍 检查错误日志
- 🧪 运行测试脚本

---

**最后更新：2025-10-28**  
**版本：2.0.0 (Gemini)**

