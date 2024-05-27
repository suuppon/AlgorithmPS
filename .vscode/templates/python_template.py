import os

def create_python_file(filename):
    # 파일 이름이 .py로 끝나는지 확인
    if not filename.endswith('.py'):
        filename += '.py'
    
    # 현재 디렉토리 경로에 파일 경로를 조합
    filepath = os.path.join(os.getcwd(), filename)
    
    # 파일 생성 및 기본 코드 작성
    with open(filepath, 'w') as file:
        file.write('import sys\n')
        file.write('input = sys.stdin.readline\n')
    
    print(f'File {filename} created with default imports.')

# 사용 예시
create_python_file('example.py')
