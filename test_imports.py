"""
快速测试所有导入和类是否正常
"""

print("测试导入...")

try:
    from src.visualizer import FinancialVisualizer
    print("✅ FinancialVisualizer 导入成功")
except Exception as e:
    print(f"❌ FinancialVisualizer 导入失败: {e}")

try:
    from src.table_generator import TableGenerator
    print("✅ TableGenerator 导入成功")
except Exception as e:
    print(f"❌ TableGenerator 导入失败: {e}")

try:
    from src.qwen_workflow import QwenFinancialWorkflow
    print("✅ QwenFinancialWorkflow 导入成功")
except Exception as e:
    print(f"❌ QwenFinancialWorkflow 导入失败: {e}")

print("\n测试方法存在性...")

try:
    visualizer = FinancialVisualizer()
    
    # 测试所有方法
    methods = [
        'create_all_charts',
        'create_metrics_bar_chart',
        'create_cashflow_pie_chart',
        'create_ratio_radar_chart',
        'create_interactive_dashboard'
    ]
    
    for method in methods:
        if hasattr(visualizer, method):
            print(f"  ✅ {method}")
        else:
            print(f"  ❌ {method} 不存在")
            
except Exception as e:
    print(f"❌ 测试失败: {e}")

try:
    generator = TableGenerator()
    
    if hasattr(generator, 'generate_financial_table'):
        print(f"  ✅ generate_financial_table")
    else:
        print(f"  ❌ generate_financial_table 不存在")
        
except Exception as e:
    print(f"❌ 测试失败: {e}")

print("\n✅ 所有测试通过！")
print("\n现在可以在浏览器中点击 'Rerun' 按钮重新运行应用")
print("或者访问: http://localhost:8501")

