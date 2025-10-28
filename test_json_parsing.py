"""
测试JSON解析功能
"""
import json
from src.financial_agent import FinancialAgent

# 创建agent
agent = FinancialAgent(api_key="test")

# 测试各种JSON响应格式
test_cases = [
    # 情况1: 纯JSON
    '''{"company_info": {"name": "测试公司", "report_period": "2023", "report_type": "年报"}, "financial_metrics": {}, "cash_flow": {}, "other_metrics": {}}''',
    
    # 情况2: 带markdown代码块
    '''```json
{"company_info": {"name": "测试公司", "report_period": "2023", "report_type": "年报"}, "financial_metrics": {}, "cash_flow": {}, "other_metrics": {}}
```''',
    
    # 情况3: 带说明文字
    '''这是提取的财务信息：
{"company_info": {"name": "测试公司", "report_period": "2023", "report_type": "年报"}, "financial_metrics": {}, "cash_flow": {}, "other_metrics": {}}
以上是JSON数据。''',
    
    # 情况4: 格式错误
    '''这是一些无效的文本''',
]

print("=" * 60)
print("测试JSON解析功能")
print("=" * 60)

for i, test_case in enumerate(test_cases, 1):
    print(f"\n测试用例 {i}:")
    print(f"输入: {test_case[:100]}...")
    
    result = agent._parse_json_response(test_case)
    
    if result:
        print(f"✓ 解析成功")
        print(f"  公司名称: {result.get('company_info', {}).get('name', 'N/A')}")
    else:
        print(f"✗ 解析失败")
        print(f"  将使用默认结构")

print("\n" + "=" * 60)
print("测试完成")
print("=" * 60)

