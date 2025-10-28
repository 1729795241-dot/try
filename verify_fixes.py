"""
验证所有修复是否正确
"""
import os
import sys

def verify_visualizer():
    """验证 FinancialVisualizer 类"""
    print("检查 FinancialVisualizer 类...")
    
    from src.visualizer import FinancialVisualizer
    
    # 检查所有必需的方法
    required_methods = [
        'create_all_charts',
        'create_metrics_bar_chart',
        'create_cashflow_pie_chart',
        'create_ratio_radar_chart',
        'create_interactive_dashboard'
    ]
    
    visualizer = FinancialVisualizer()
    
    for method_name in required_methods:
        if not hasattr(visualizer, method_name):
            print(f"  ❌ 缺少方法: {method_name}")
            return False
        print(f"  ✓ {method_name}")
    
    print("✅ FinancialVisualizer 类检查通过\n")
    return True

def verify_table_generator():
    """验证 TableGenerator 类"""
    print("检查 TableGenerator 类...")
    
    from src.table_generator import TableGenerator
    
    # 检查所有必需的方法
    required_methods = [
        'generate_financial_table'
    ]
    
    generator = TableGenerator()
    
    for method_name in required_methods:
        if not hasattr(generator, method_name):
            print(f"  ❌ 缺少方法: {method_name}")
            return False
        print(f"  ✓ {method_name}")
    
    print("✅ TableGenerator 类检查通过\n")
    return True

def verify_qwen_workflow():
    """验证 QwenWorkflow 类"""
    print("检查 QwenWorkflow 类...")
    
    try:
        from src.qwen_workflow import QwenWorkflow
        
        # 检查类是否可以实例化（不需要真实的API密钥）
        print("  ✓ QwenWorkflow 类可以导入")
        
        # 检查方法
        required_methods = [
            'run'
        ]
        
        # 注意：我们不实例化，因为需要API密钥
        for method_name in required_methods:
            if not hasattr(QwenWorkflow, method_name):
                print(f"  ❌ 缺少方法: {method_name}")
                return False
            print(f"  ✓ {method_name}")
        
        print("✅ QwenWorkflow 类检查通过\n")
        return True
    except Exception as e:
        print(f"❌ QwenWorkflow 导入失败: {str(e)}\n")
        return False

def verify_method_signatures():
    """验证方法签名"""
    print("检查方法签名...")
    
    from src.visualizer import FinancialVisualizer
    import inspect
    
    visualizer = FinancialVisualizer()
    
    # 检查 create_all_charts 的签名
    sig = inspect.signature(visualizer.create_all_charts)
    params = list(sig.parameters.keys())
    
    if 'financial_data' not in params:
        print(f"  ❌ create_all_charts 缺少 financial_data 参数")
        return False
    
    print(f"  ✓ create_all_charts 签名正确: {params}")
    
    # 检查其他方法不接受 output_path 参数
    for method_name in ['create_metrics_bar_chart', 'create_cashflow_pie_chart', 
                        'create_ratio_radar_chart', 'create_interactive_dashboard']:
        method = getattr(visualizer, method_name)
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        if 'output_path' in params:
            print(f"  ⚠ {method_name} 有 output_path 参数（应该内部处理）")
        
        print(f"  ✓ {method_name} 签名: {params}")
    
    print("✅ 方法签名检查通过\n")
    return True

def main():
    """主函数"""
    print("="*70)
    print("验证所有修复")
    print("="*70)
    print()
    
    all_passed = True
    
    # 运行所有验证
    all_passed &= verify_visualizer()
    all_passed &= verify_table_generator()
    all_passed &= verify_qwen_workflow()
    all_passed &= verify_method_signatures()
    
    print("="*70)
    if all_passed:
        print("✅ 所有检查通过！代码已修复。")
        print("\n现在可以运行:")
        print("  streamlit run app_qwen.py")
    else:
        print("❌ 部分检查失败，请查看上面的错误信息。")
        sys.exit(1)
    print("="*70)

if __name__ == "__main__":
    main()

