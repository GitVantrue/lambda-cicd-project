import json

def lambda_handler(event, context):
    """
    Lambda 핸들러 함수
    로컬에서 편집 후 Git Push하면 자동으로 배포됩니다
    """
    
    try:
        # 이벤트 데이터 처리
        body = json.loads(event.get('body', '{}')) if event.get('body') else {}
        
        # 비즈니스 로직
        result = {
            'message': '안녕하세요! CI/CD 테스트 중입니다!',
            'input_data': body,
            'version': '1.0.0'
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result, ensure_ascii=False)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': '오류가 발생했습니다'
            }, ensure_ascii=False)
        }