FROM python:3.9-slim

WORKDIR /app

# 复制 requirements 文件并安装依赖
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY src/ .

EXPOSE 5000

# 使用 gunicorn 运行应用
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]