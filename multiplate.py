import os
import shutil

# 경로 설정
json_directory = r'C:\Users\User\Desktop\Capstone_Self-Driving-master\yangpa\carlabel'
image_directory = r'C:\Users\User\Desktop\Capstone_Self-Driving-master\yangpa\carplate'
destination_directory = r'C:\Users\User\Desktop\Capstone_Self-Driving-master\yangpa\carplate2'  # 이미지들 복사할 폴더

# 대상 디렉토리가 없다면 생성
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# json 파일 목록 가져오기
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

# 동일한 이름의 jpg 파일 복사
for json_file in json_files:
    # json 파일 이름에서 확장자 제거
    base_name = os.path.splitext(json_file)[0]

    # 해당 이름의 jpg 파일 확인
    jpg_file = base_name + '.jpg'
    jpg_file_path = os.path.join(image_directory, jpg_file)

    if os.path.exists(jpg_file_path):
        # jpg 파일을 대상 디렉토리로 복사
        shutil.copy(jpg_file_path, destination_directory)
        print(f'Copied: {jpg_file}')
    else:
        print(f'Image file not found for: {json_file}')

print("Image copying process completed.")