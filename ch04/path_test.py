import os

print(f'{os.path.realpath(__file__)=}')
print(f'{__name__=}')

c_module_path = os.path.realpath(__file__) # 파일의 실제 경로
c_module_dir = os.path.dirname(c_module_path) #파일 이름 없이 디렉토리 얻어오기
print(c_module_dir)
print(c_module_dir + "/image/labelImage.jpg") #미리 받은 디렉토리로 디렉토리 정보 입력 없이 파일 이름만 입력하여 사진 가져오기

