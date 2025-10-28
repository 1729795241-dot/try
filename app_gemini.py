"""
财务报表分析Web应用 - Gemini版本
支持直接上传PDF文件给Gemini处理
"""
import streamlit as st
import os
import json
from pathlib import Path
from src.gemini_workflow import GeminiFinancialWorkflow
from PIL import Image

# 页面配置
st.set_page_config(
    page_title="财务报表智能分析系统 (Gemini)",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4285f4;
        text-align: center;
        padding: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #e8f0fe;
        border: 1px solid: #4285f4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<div class="main-header">🤖 财务报表智能分析系统 (Gemini版)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">基于Google Gemini的智能财务分析助手 - 支持直接处理PDF文件</div>', unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.header("⚙️ 系统设置")
    
    # API密钥设置
    api_key = st.text_input(
        "Gemini API密钥",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password",
        help="输入您的Google Gemini API密钥"
    )
    
    # 输出目录设置
    output_dir = st.text_input(
        "输出目录",
        value="output_gemini",
        help="分析结果保存目录"
    )
    
    st.divider()
    
    st.header("✨ Gemini优势")
    st.markdown("""
    - ✅ **直接处理PDF** - 无需预先提取文本
    - ✅ **支持扫描版** - 可以处理图片型PDF
    - ✅ **更准确** - 更好的表格识别能力
    - ✅ **多模态** - 同时理解文本和图像
    """)
    
    st.divider()
    
    st.header("📖 使用说明")
    st.markdown("""
    1. 输入Gemini API密钥
    2. 上传PDF格式的财务报表
    3. 点击"开始分析"按钮
    4. 等待AI处理完成
    5. 查看分析结果和下载文件
    
    **支持的PDF类型：**
    - 📄 文本型PDF
    - 🖼️ 扫描版PDF
    - 📊 包含表格的PDF
    - 🌍 中英文PDF
    """)
    
    st.divider()
    
    st.header("ℹ️ 系统信息")
    st.info(f"""
    **模型**: Google Gemini 1.5 Flash  
    **版本**: 2.0.0  
    **特性**: 直接PDF处理
    """)

# 主界面
tab1, tab2, tab3 = st.tabs(["📤 上传分析", "📊 查看结果", "📚 历史记录"])

with tab1:
    st.header("上传财务报表")
    
    # 文件上传
    uploaded_file = st.file_uploader(
        "选择PDF文件",
        type=['pdf'],
        help="支持上传任何类型的PDF（文本型或扫描版），文件大小不超过200MB"
    )
    
    if uploaded_file is not None:
        # 显示文件信息
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("文件名", uploaded_file.name)
        with col2:
            st.metric("文件大小", f"{uploaded_file.size / 1024 / 1024:.2f} MB")
        with col3:
            st.metric("文件类型", uploaded_file.type)
        
        # 保存上传的文件
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        temp_pdf_path = os.path.join(temp_dir, uploaded_file.name)
        
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✅ 文件上传成功: {uploaded_file.name}")
        
        # 分析按钮
        if st.button("🚀 开始分析", type="primary", use_container_width=True):
            if not api_key:
                st.error("❌ 请先在侧边栏设置Gemini API密钥")
            else:
                # 创建工作流
                with st.spinner("🔄 Gemini正在分析PDF，请稍候..."):
                    try:
                        workflow = GeminiFinancialWorkflow(api_key=api_key, output_dir=output_dir)
                        result = workflow.run(temp_pdf_path)
                        
                        # 保存结果到session state
                        st.session_state['last_result'] = result
                        st.session_state['last_file'] = uploaded_file.name
                        
                        st.success("✅ 分析完成！")
                        st.balloons()
                        
                        # 显示快速摘要
                        st.subheader("📋 分析摘要")
                        
                        financial_data = result['financial_data']
                        company_info = financial_data.get('company_info', {})
                        metrics = financial_data.get('financial_metrics', {})
                        
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            st.metric(
                                "公司名称",
                                company_info.get('name', 'N/A')
                            )
                        
                        with col2:
                            revenue = metrics.get('revenue', {})
                            st.metric(
                                "营业收入",
                                f"{revenue.get('amount', 'N/A')} {revenue.get('unit', '')}",
                                delta=revenue.get('yoy_growth', 'N/A')
                            )
                        
                        with col3:
                            net_profit = metrics.get('net_profit', {})
                            st.metric(
                                "净利润",
                                f"{net_profit.get('amount', 'N/A')} {net_profit.get('unit', '')}",
                                delta=net_profit.get('yoy_growth', 'N/A')
                            )
                        
                        with col4:
                            st.metric(
                                "净资产收益率",
                                f"{metrics.get('roe', 'N/A')}"
                            )
                        
                        st.info("💡 请切换到【查看结果】标签页查看详细分析结果")
                        
                    except Exception as e:
                        st.error(f"❌ 分析失败: {str(e)}")
                        st.exception(e)

with tab2:
    st.header("分析结果")
    
    if 'last_result' in st.session_state:
        result = st.session_state['last_result']
        
        st.success(f"📄 当前显示: {st.session_state.get('last_file', 'N/A')}")
        
        # 财务数据
        st.subheader("💰 财务数据")
        financial_data = result['financial_data']
        
        # 使用expander显示详细数据
        with st.expander("📊 查看完整财务数据", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.json(financial_data.get('company_info', {}))
                st.json(financial_data.get('financial_metrics', {}))
            
            with col2:
                st.json(financial_data.get('cash_flow', {}))
        
        # AI分析报告
        st.subheader("🤖 Gemini AI分析报告")
        with st.expander("📝 查看分析报告", expanded=True):
            st.markdown(result['analysis'])
        
        # 可视化图表
        st.subheader("📈 可视化图表")
        
        chart_files = result['files'].get('charts', [])
        
        if chart_files:
            # 显示图表
            for chart_path in chart_files:
                if chart_path.endswith('.html'):
                    # 交互式图表
                    st.components.v1.html(open(chart_path, 'r', encoding='utf-8').read(), height=850)
                elif chart_path.endswith('.png'):
                    # 静态图表
                    st.image(chart_path, use_container_width=True)
        else:
            st.info("暂无可视化图表")
        
        # 下载文件
        st.subheader("📥 下载文件")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            excel_path = result['files'].get('excel')
            if excel_path and os.path.exists(excel_path):
                with open(excel_path, 'rb') as f:
                    st.download_button(
                        label="📊 下载Excel表格",
                        data=f,
                        file_name=os.path.basename(excel_path),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
        
        with col2:
            report_path = result['files'].get('report')
            if report_path and os.path.exists(report_path):
                with open(report_path, 'rb') as f:
                    st.download_button(
                        label="📝 下载分析报告",
                        data=f,
                        file_name=os.path.basename(report_path),
                        mime="text/plain"
                    )
        
        with col3:
            json_path = result['files'].get('json')
            if json_path and os.path.exists(json_path):
                with open(json_path, 'rb') as f:
                    st.download_button(
                        label="💾 下载JSON数据",
                        data=f,
                        file_name=os.path.basename(json_path),
                        mime="application/json"
                    )
    else:
        st.info("👈 请先在【上传分析】标签页上传并分析PDF文件")

with tab3:
    st.header("历史记录")
    
    # 列出输出目录中的所有结果
    if os.path.exists(output_dir):
        json_files = list(Path(output_dir).glob("*_数据.json"))
        
        if json_files:
            st.write(f"找到 {len(json_files)} 条历史记录")
            
            for json_file in sorted(json_files, key=os.path.getmtime, reverse=True):
                with st.expander(f"📄 {json_file.stem}"):
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.json(data.get('company_info', {}))
                        with col2:
                            st.json(data.get('financial_metrics', {}))
                        
                        # 删除按钮
                        if st.button(f"🗑️ 删除", key=f"del_{json_file.name}"):
                            os.remove(json_file)
                            st.rerun()
                    except Exception as e:
                        st.error(f"读取失败: {str(e)}")
        else:
            st.info("暂无历史记录")
    else:
        st.info("输出目录不存在")

# 页脚
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>财务报表智能分析系统 v2.0.0 (Gemini版) | Powered by Google Gemini AI</p>
</div>
""", unsafe_allow_html=True)

