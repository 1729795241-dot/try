"""
测试通义千问API连接
"""
import os
from openai import OpenAI

def test_qwen_connection():
    """测试通义千问API连接"""
    
    print("="*70)
    print("通义千问API连接测试")
    print("="*70)
    
    # 获取API密钥
    api_key = os.getenv("DASHSCOPE_API_KEY")
    
    if not api_key:
        print("❌ 未找到API密钥")
        print("\n请设置环境变量：")
        print("  DASHSCOPE_API_KEY=your_api_key_here")
        print("\n或者在.env文件中添加：")
        print("  DASHSCOPE_API_KEY=your_api_key_here")
        return False
    
    print(f"✓ API密钥已找到: {api_key[:10]}...")
    
    # 创建客户端
    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        print("✓ 客户端创建成功")
    except Exception as e:
        print(f"❌ 客户端创建失败: {str(e)}")
        return False
    
    # 测试简单对话
    print("\n测试简单对话...")
    try:
        completion = client.chat.completions.create(
            model="qwen-long",
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '你好，请回复"连接成功"'}
            ],
            timeout=30
        )
        
        response = completion.choices[0].message.content
        print(f"✓ API响应: {response}")
        print("\n" + "="*70)
        print("✅ 通义千问API连接测试成功！")
        print("="*70)
        return True
        
    except Exception as e:
        print(f"❌ API调用失败: {str(e)}")
        print("\n可能的原因：")
        print("1. API密钥无效")
        print("2. 网络连接问题")
        print("3. 服务暂时不可用")
        print("\n建议：")
        print("1. 检查API密钥是否正确")
        print("2. 访问 https://dashscope.console.aliyun.com/ 确认服务状态")
        print("3. 检查网络连接")
        return False

if __name__ == "__main__":
    # 尝试加载.env文件
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✓ .env文件已加载\n")
    except:
        print("⚠ 未找到.env文件或python-dotenv未安装\n")
    
    test_qwen_connection()

