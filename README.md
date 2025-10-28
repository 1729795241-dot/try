# 📊 财务报表智能分析系统

基于DeepSeek大模型的智能财务报表分析工具，支持处理长文本PDF财务报表（数百页），自动提取财务信息、生成表格和可视化图表。

## ✨ 主要功能

- 📄 **PDF文本提取**: 支持长文本分块处理，可处理数百页的财务报表
- 🔍 **智能信息提取**: 使用DeepSeek大模型自动提取关键财务指标
- 📊 **自动生成表格**: 将财务数据结构化为Excel/CSV表格
- 📈 **数据可视化**: 自动生成多种财务图表（柱状图、饼图、雷达图、交互式仪表盘）
- 🤖 **AI分析报告**: 生成专业的财务分析报告
- 🌐 **Web应用界面**: 提供友好的Streamlit Web界面

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥

编辑 `.env` 文件，设置您的DeepSeek API密钥：

```env
DEEPSEEK_API_KEY=sk-f714f944a8a04ed3b13ea5894bead929
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
```

### 3. 运行Web应用

```bash
streamlit run app.py
```

然后在浏览器中打开 `http://localhost:8501`

### 4. 或使用命令行工具

```bash
# 分析单个PDF文件
python cli.py your_report.pdf

# 分析多个PDF文件
python cli.py report1.pdf report2.pdf report3.pdf

# 指定输出目录
python cli.py report.pdf -o results
```

## 📁 项目结构

```
.
├── src/                      # 源代码目录
│   ├── __init__.py
│   ├── pdf_extractor.py      # PDF文本提取模块
│   ├── llm_client.py         # DeepSeek API调用模块
│   ├── financial_agent.py    # 财务信息提取Agent
│   ├── table_generator.py    # 表格生成模块
│   ├── visualizer.py         # 数据可视化模块
│   └── workflow.py           # 工作流编排
├── app.py                    # Streamlit Web应用
├── cli.py                    # 命令行工具
├── requirements.txt          # 依赖包列表
├── .env                      # 环境变量配置
└── README.md                 # 项目说明文档
```

## 🔧 核心模块说明

### PDF提取模块 (`pdf_extractor.py`)

- 使用 `pdfplumber` 提取PDF文本
- 支持分块处理长文本
- 可提取PDF中的表格

### LLM客户端 (`llm_client.py`)

- 封装DeepSeek API调用
- 提供财务信息提取、分析报告生成等功能
- 支持自定义提示词

### 财务Agent (`financial_agent.py`)

- 智能提取财务指标（收入、利润、资产等）
- 解析LLM返回的JSON数据
- 提供默认数据结构

### 表格生成器 (`table_generator.py`)

- 生成Excel/CSV格式的财务数据表格
- 支持多期数据对比
- 使用pandas和openpyxl处理

### 可视化器 (`visualizer.py`)

- 生成多种图表类型：
  - 柱状图：主要财务指标对比
  - 饼图：现金流结构分布
  - 雷达图：财务健康度评估
  - 交互式仪表盘：综合财务数据展示
- 使用matplotlib和plotly

### 工作流 (`workflow.py`)

- 编排完整的分析流程
- 支持单文件和批量处理
- 自动保存所有结果文件

## 📊 输出文件

系统会在输出目录（默认为 `output/`）生成以下文件：

1. **Excel表格**: `{公司名称}_财务数据.xlsx`
   - 主要财务指标表
   - 现金流量表

2. **分析报告**: `{公司名称}_分析报告.txt`
   - AI生成的财务分析
   - 财务数据摘要

3. **原始数据**: `{公司名称}_数据.json`
   - 结构化的财务数据（JSON格式）

4. **可视化图表**:
   - `{公司名称}_财务指标柱状图.png`
   - `{公司名称}_现金流饼图.png`
   - `{公司名称}_雷达图.png`
   - `{公司名称}_交互式仪表盘.html`

## 🎯 使用场景

- 📈 **投资分析**: 快速分析上市公司财务报表
- 🏢 **企业尽调**: 批量处理多家企业的财务数据
- 📚 **财务研究**: 提取和对比历史财务数据
- 🎓 **教学演示**: 展示财务分析的自动化流程

## ⚙️ 配置选项

### PDF提取配置

在 `PDFExtractor` 中可以调整：
- `chunk_size`: 每个文本块的页数（默认5页）

### LLM配置

在 `DeepSeekClient` 中可以调整：
- `temperature`: 生成温度（默认0.3）
- `max_tokens`: 最大token数（默认4000）
- `model`: 使用的模型（默认deepseek-chat）

## 🔍 提取的财务指标

系统会自动提取以下财务信息：

**公司基本信息**:
- 公司名称
- 报告期间
- 报告类型

**主要财务指标**:
- 营业收入（含同比增长率）
- 净利润（含同比增长率）
- 总资产
- 净资产
- 资产负债率
- 每股收益
- 净资产收益率

**现金流信息**:
- 经营活动现金流
- 投资活动现金流
- 筹资活动现金流

## 🛠️ 技术栈

- **PDF处理**: pdfplumber, PyPDF2
- **LLM**: DeepSeek API (OpenAI兼容接口)
- **数据处理**: pandas, numpy
- **可视化**: matplotlib, plotly, seaborn
- **Web框架**: Streamlit
- **Excel处理**: openpyxl, xlsxwriter

## 📝 注意事项

1. **API密钥**: 确保设置了有效的DeepSeek API密钥
2. **文件大小**: 建议单个PDF文件不超过200MB
3. **处理时间**: 长文本处理可能需要几分钟，请耐心等待
4. **数据准确性**: AI提取的数据仅供参考，重要决策请人工核验

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- DeepSeek AI - 提供强大的大语言模型
- Streamlit - 提供优秀的Web框架
- 所有开源库的贡献者

---

**开发者**: AI Agent  
**版本**: 1.0.0  
**最后更新**: 2025-10-28

