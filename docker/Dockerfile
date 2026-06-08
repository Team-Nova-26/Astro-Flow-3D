FROM nvcr.io/nvidia/pytorch:25.04-py3

WORKDIR /workspace

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/workspace

CMD ["bash"]