# Python 베이스 이미지 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /webapp

# 필수 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmariadb-dev-compat libmariadb-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 복사
COPY . .

# 포트 설정
EXPOSE 9080

# 애플리케이션 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:9080"]
