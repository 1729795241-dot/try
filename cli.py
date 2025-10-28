"""
命令行版本 - 财务报表分析工具
"""
import argparse
import sys
from src.workflow import FinancialWorkflow


def main():
    parser = argparse.ArgumentParser(
        description="财务报表智能分析系统 - 命令行工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python cli.py report.pdf
  python cli.py report.pdf -o results
  python cli.py report1.pdf report2.pdf -o batch_results
        """
    )
    
    parser.add_argument(
        'pdf_files',
        nargs='+',
        help='PDF财务报表文件路径（支持多个文件）'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='output',
        help='输出目录（默认: output）'
    )
    
    parser.add_argument(
        '-k', '--api-key',
        help='DeepSeek API密钥（可选，默认从环境变量读取）'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='显示详细输出'
    )
    
    args = parser.parse_args()
    
    try:
        # 创建工作流
        workflow = FinancialWorkflow(
            api_key=args.api_key,
            output_dir=args.output
        )
        
        # 处理文件
        if len(args.pdf_files) == 1:
            # 单文件处理
            result = workflow.run(args.pdf_files[0])
            
            if result['success']:
                print("\n✅ 处理成功！")
                print(f"\n生成的文件:")
                for key, value in result['files'].items():
                    if isinstance(value, list):
                        print(f"  {key}:")
                        for v in value:
                            print(f"    - {v}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print("\n❌ 处理失败")
                sys.exit(1)
        else:
            # 批量处理
            results = workflow.run_batch(args.pdf_files)
            
            success_count = sum(1 for r in results if r.get('success', False))
            print(f"\n处理完成: {success_count}/{len(results)} 个文件成功")
            
            if success_count < len(results):
                sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

