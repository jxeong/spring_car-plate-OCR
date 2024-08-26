import os
from PIL import Image
import numpy as np
import json
import cv2

# 이미지가 있는 디렉토리를 설정합니다.
for img in os.scandir('./data/0826/image'):
    save_name = ''

    # 이미지 파일명을 가져옵니다.
    name = img.name

    # 이미지 경로를 설정합니다.
    img_path = f'./data/0826/image/{name}'
    print(f"Trying to read image from: {img_path}")

    # PIL을 사용하여 이미지를 읽어옵니다.
    try:
        with Image.open(img_path) as pil_img:
            img = np.array(pil_img)  # PIL 이미지를 numpy 배열로 변환
    except Exception as e:
        print(f"Error loading image: {img_path}, {str(e)}")
        continue

    h, w, c = img.shape

    # 이미지에 해당하는 JSON 파일 경로를 설정합니다.
    json_path = f'./data/0826/labels/{os.path.splitext(name)[0]}.json'

    # JSON 파일을 읽어와서 포인트를 추출합니다.
    with open(json_path, 'rt', encoding='UTF8') as json_file:
        data = json.load(json_file)

    # JSON 데이터에서 좌표 포인트를 추출합니다.
    points = data['shapes'][0]['points']

    # 절대 좌표로 변환합니다.
    coord_list = [(float(points[0][0]), float(points[0][1])),  # 좌상단
                  (float(points[1][0]), float(points[1][1])),  # 좌하단
                  (float(points[2][0]), float(points[2][1])),  # 우하단
                  (float(points[3][0]), float(points[3][1]))]  # 우상단

    # 상대 좌표로 변환합니다.
    lista = [(round(coord_list[0][0] / w, 4), round(coord_list[0][1] / h, 4)),
             (round(coord_list[1][0] / w, 4), round(coord_list[1][1] / h, 4)),
             (round(coord_list[2][0] / w, 4), round(coord_list[2][1] / h, 4)),
             (round(coord_list[3][0] / w, 4), round(coord_list[3][1] / h, 4))]

    # 새로운 이미지 파일명을 생성합니다.
    save_name = (f"{lista[0][0]}_{lista[0][1]}__"
                 f"{lista[1][0]}_{lista[1][1]}__"
                 f"{lista[2][0]}_{lista[2][1]}__"
                 f"{lista[3][0]}_{lista[3][1]}.jpg")

    print(save_name)

    # 이미지를 저장할 경로를 설정합니다.
    save_path = f'./data/0826/newimage/{save_name}'

    # OpenCV를 사용하여 numpy 배열 이미지를 저장합니다.
    cv2.imwrite(save_path, img)
