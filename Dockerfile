# 使用官方 Node.js 镜像作为基础镜像
FROM python:3.8.10

# 复制项目文件
COPY . /app/

# 设置工作目录
WORKDIR /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用监听的端口
EXPOSE 8000

# 定义启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
