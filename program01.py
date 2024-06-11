import pandas as pd

# 모델 정보 (수동 입력 또는 CSV 파일 불러오기)
data = {
    '모델': [
        '[갤럭시 S24](https://www.samsung.com/sec/smartphones/galaxy-s24)',
        '[갤럭시 S24+](https://www.samsung.com/sec/smartphones/galaxy-s24plus)',
        '[갤럭시 S24 울트라](https://www.samsung.com/sec/smartphones/galaxy-s24-ultra)',
        '[갤럭시 Z 플립5](https://www.samsung.com/sec/smartphones/galaxy-z-flip5)',
        '[갤럭시 Z 플립5 폴더블](https://www.samsung.com/sec/smartphones/galaxy-z-flip5-foldable)',
        '[갤럭시 A25](https://www.samsung.com/sec/smartphones/galaxy-a25)'],
    '가격': [900000, 1000000, 1200000, 1300000, 1900000, 350000],
    '화면크기': [6.1, 6.6, 6.8, 6.7, 7.6, 6.6],
    '해상도': ['FHD+', 'FHD+', 'WQHD+', 'FHD+', 'UXGA+', 'FHD+'],
    '프로세서': ['Snapdragon 8 Gen 2', 'Snapdragon 8 Gen 2', 'Snapdragon 8 Gen 2', 'Snapdragon 8 Gen 2', 'Snapdragon 8 Gen 2', 'Exynos 1380'],
    'RAM': [8, 12, 12, 8, 12, 6],
    '저장공간': [128, 256, 256, 128, 256, 128],
    '사용자 평점': [4.5, 4.7, 4.9, 4.6, 4.8, 4.2],  # 예시 평점 (0~5점 만점)
    '최저가': [850000, 950000, 1150000, 1250000, 1850000, 330000]  # 예시 최저가
}

# 데이터프레임 변환
df = pd.DataFrame(data)

# 가격 기준 오름차순 정렬
df = df.sort_values(by='가격')

# 출력
print("## 2024년 출시 삼성 갤럭시 모델 비교")

# 표 형식 출력 (열 너비 조정, 숫자 형식 설정)
print(df[['모델', '가격', '화면크기(인치)', '해상도', '프로세서', 'RAM(GB)', '저장공간(GB)', '사용자 평점', '최저가(원)']].to_string(index=False))
