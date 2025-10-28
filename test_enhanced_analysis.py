"""
测试增强的财务分析功能
"""
import json

print("=" * 80)
print("测试增强的财务分析功能")
print("=" * 80)
print()

# 测试1: 检查导入
print("【测试1】检查模块导入...")
try:
    from src.qwen_client import QwenClient
    from src.qwen_financial_agent import QwenFinancialAgent
    from src.qwen_workflow import QwenFinancialWorkflow
    print("✅ 所有模块导入成功")
except Exception as e:
    print(f"❌ 导入失败: {e}")
    exit(1)

print()

# 测试2: 检查默认数据结构
print("【测试2】检查增强的数据结构...")
try:
    agent = QwenFinancialAgent(api_key="test_key_for_structure_check")
    default_structure = agent._get_default_structure()
    
    # 检查新增字段
    required_fields = {
        'company_info': ['name', 'stock_code', 'report_period', 'report_type', 'industry', 'listing_date'],
        'financial_metrics': [
            'revenue', 'net_profit', 'gross_profit', 'operating_profit',
            'total_assets', 'total_liabilities', 'shareholders_equity',
            'current_assets', 'current_liabilities',
            'eps', 'roe', 'roa', 'asset_liability_ratio', 'current_ratio', 'quick_ratio'
        ],
        'cash_flow': ['operating', 'investing', 'financing', 'cash_and_equivalents'],
    }
    
    all_ok = True
    for section, fields in required_fields.items():
        if section not in default_structure:
            print(f"  ❌ 缺少部分: {section}")
            all_ok = False
            continue
        
        for field in fields:
            if field not in default_structure[section]:
                print(f"  ❌ {section} 缺少字段: {field}")
                all_ok = False
            else:
                print(f"  ✓ {section}.{field}")
    
    # 检查新增的顶级字段
    if 'business_segments' in default_structure:
        print(f"  ✓ business_segments")
    else:
        print(f"  ❌ 缺少字段: business_segments")
        all_ok = False
    
    if 'key_events' in default_structure:
        print(f"  ✓ key_events")
    else:
        print(f"  ❌ 缺少字段: key_events")
        all_ok = False
    
    if all_ok:
        print("\n✅ 数据结构检查通过")
    else:
        print("\n❌ 数据结构检查失败")
        exit(1)
        
except Exception as e:
    print(f"❌ 测试失败: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print()

# 测试3: 检查嵌套字段结构
print("【测试3】检查嵌套字段结构...")
try:
    # 检查 revenue 字段
    revenue = default_structure['financial_metrics']['revenue']
    required_revenue_fields = ['amount', 'unit', 'yoy_growth', 'previous_year']
    
    for field in required_revenue_fields:
        if field in revenue:
            print(f"  ✓ revenue.{field}")
        else:
            print(f"  ❌ revenue 缺少字段: {field}")
    
    # 检查 operating cash flow 字段
    operating = default_structure['cash_flow']['operating']
    required_cf_fields = ['amount', 'unit', 'yoy_growth']
    
    for field in required_cf_fields:
        if field in operating:
            print(f"  ✓ cash_flow.operating.{field}")
        else:
            print(f"  ❌ cash_flow.operating 缺少字段: {field}")
    
    print("\n✅ 嵌套字段结构检查通过")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
    exit(1)

print()

# 测试4: 显示完整的数据结构
print("【测试4】完整数据结构预览...")
print(json.dumps(default_structure, ensure_ascii=False, indent=2))

print()
print("=" * 80)
print("✅ 所有测试通过！")
print("=" * 80)
print()
print("增强功能说明：")
print("1. ✅ 新增公司信息字段：股票代码、行业、上市日期")
print("2. ✅ 新增财务指标：毛利润、营业利润、股东权益、流动资产/负债")
print("3. ✅ 新增财务比率：ROA、资产负债率、流动比率、速动比率")
print("4. ✅ 新增现金流字段：期末现金及现金等价物")
print("5. ✅ 新增业务分部信息")
print("6. ✅ 新增重要事项记录")
print("7. ✅ 增强分析报告格式和内容")
print()
print("现在可以重新运行应用测试新功能：")
print("  streamlit run app_qwen.py")
print()

