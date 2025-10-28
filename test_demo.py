"""
演示脚本 - 使用示例财务数据测试系统
"""
import json
import os
from src.table_generator import TableGenerator
from src.visualizer import FinancialVisualizer

# 创建示例财务数据
demo_data = {
    "company_info": {
        "name": "示例科技股份有限公司",
        "report_period": "2023年度",
        "report_type": "年度报告"
    },
    "financial_metrics": {
        "revenue": {
            "amount": 1250000000,
            "unit": "元",
            "yoy_growth": "15.3%"
        },
        "net_profit": {
            "amount": 185000000,
            "unit": "元",
            "yoy_growth": "22.8%"
        },
        "total_assets": {
            "amount": 3500000000,
            "unit": "元"
        },
        "net_assets": {
            "amount": 1800000000,
            "unit": "元"
        },
        "asset_liability_ratio": "48.6%",
        "eps": "2.35",
        "roe": "12.8%"
    },
    "cash_flow": {
        "operating": 320000000,
        "investing": -150000000,
        "financing": -80000000,
        "unit": "元"
    },
    "other_metrics": {
        "gross_margin": "35.2%",
        "current_ratio": "1.85"
    }
}

def main():
    print("="*60)
    print("财务报表智能分析系统 - 演示模式")
    print("="*60)
    print("\n使用示例数据测试系统功能...\n")
    
    # 创建输出目录
    output_dir = "demo_output"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. 生成表格
    print("1. 生成财务数据表格...")
    table_gen = TableGenerator(output_dir=output_dir)
    excel_path = table_gen.generate_financial_table(demo_data, output_format="excel")
    print(f"   ✓ Excel表格: {excel_path}\n")
    
    # 2. 生成可视化图表
    print("2. 生成可视化图表...")
    visualizer = FinancialVisualizer(output_dir=output_dir)
    chart_paths = visualizer.create_all_charts(demo_data)
    
    for chart_path in chart_paths:
        if chart_path:
            print(f"   ✓ {os.path.basename(chart_path)}")
    
    # 3. 保存示例数据
    print("\n3. 保存示例数据...")
    json_path = os.path.join(output_dir, "示例数据.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(demo_data, f, ensure_ascii=False, indent=2)
    print(f"   ✓ JSON数据: {json_path}")
    
    # 4. 生成示例分析报告
    print("\n4. 生成示例分析报告...")
    report_path = os.path.join(output_dir, "示例分析报告.txt")
    
    analysis_text = """
财务状况总体评价：
示例科技股份有限公司2023年度财务表现良好，营业收入和净利润均实现双位数增长，
显示出较强的盈利能力和成长性。

盈利能力分析：
- 营业收入12.5亿元，同比增长15.3%，保持稳健增长态势
- 净利润1.85亿元，同比增长22.8%，增速高于收入增速，盈利质量提升
- 净资产收益率12.8%，处于行业中上水平
- 每股收益2.35元，为股东创造了良好回报

偿债能力分析：
- 资产负债率48.6%，处于合理区间，财务结构稳健
- 流动比率1.85，短期偿债能力良好
- 总资产35亿元，净资产18亿元，资产质量较高

现金流分析：
- 经营活动现金流3.2亿元，现金创造能力强
- 投资活动现金流-1.5亿元，公司持续投入发展
- 筹资活动现金流-0.8亿元，财务结构优化

主要风险和机会：
风险：需关注投资项目的回报情况，确保投资效益
机会：公司盈利能力持续提升，具备进一步扩张的基础
建议：保持稳健的财务政策，优化资产配置，提升运营效率
"""
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write("示例科技股份有限公司 财务分析报告\n")
        f.write("="*60 + "\n")
        f.write(analysis_text)
        f.write("\n" + "="*60 + "\n")
        f.write("财务数据摘要\n")
        f.write("="*60 + "\n")
        f.write(json.dumps(demo_data, ensure_ascii=False, indent=2))
    
    print(f"   ✓ 分析报告: {report_path}")
    
    print("\n" + "="*60)
    print("✅ 演示完成！")
    print("="*60)
    print(f"\n所有文件已保存到: {output_dir}/")
    print("\n您可以:")
    print("1. 查看生成的Excel表格和图表")
    print("2. 运行 'streamlit run app.py' 启动Web应用")
    print("3. 使用真实的PDF财务报表进行分析")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()

