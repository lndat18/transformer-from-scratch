# Transformer From Scratch 🚀

Dự án này tập trung vào việc xây dựng mô hình **Transformer** hoàn toàn từ đầu (from scratch) bằng ngôn ngữ Python và thư viện PyTorch. Kiến trúc này dựa trên bài báo nghiên cứu nổi tiếng của Google Brain: [*"Attention Is All You Need"* (2017)](https://arxiv.org/abs/1706.03762).

## 📌 Giới thiệu

Mục tiêu của dự án là hiểu sâu về cơ chế vận hành của các mô hình ngôn ngữ hiện đại (như GPT, BERT, T5) thông qua việc tự lập trình từng module cốt lõi của Transformer. Dự án cung cấp một framework gọn nhẹ, dễ hiểu cho việc huấn luyện các bài toán dịch máy (Machine Translation) hoặc các tác vụ Sequence-to-Sequence khác.

## ✨ Tính năng chính

- **Core Module Implementation**: Xây dựng Multi-head Attention, Positional Encoding, và Feed-forward Network.
- **Full Architecture**: Tích hợp hoàn chỉnh Encoder, Decoder và liên kết Encoder-Decoder Attention.
- **Masking Mechanism**: Hỗ trợ Padding Mask và Look-ahead Mask (dành cho Decoder).
- **Flexibility**: Dễ dàng cấu hình các siêu tham số qua file YAML.
- **Evaluation**: Hỗ trợ tính toán chỉ số BLEU score để đánh giá chất lượng mô hình.

## 📂 Cấu trúc thư mục

```text
.
├── README.md
├── configs/
│   └── config.yaml         # Cấu hình siêu tham số
├── data/
│   ├── processed/          # Dữ liệu đã tiền xử lý
│   └── raw/                # Dữ liệu thô
├── dataset.py              # Xử lý dữ liệu và tạo DataLoader
├── evaluate.py             # Script đánh giá mô hình
├── evaluations/
│   ├── __init__.py
│   └── bleu_score.py       # Tính toán chỉ số BLEU
├── notebooks/              # Jupyter notebooks cho thử nghiệm
├── requirements.txt        # Các thư viện phụ thuộc
├── train.py                # Script huấn luyện chính
├── transformer/            # Mã nguồn chính của mô hình
│   ├── __init__.py
│   ├── attention.py        # Cơ chế Multi-head attention
│   ├── decoder.py          # Khối Decoder
│   ├── encoder.py          # Khối Encoder
│   ├── layer.py            # Các lớp Encoder/Decoder Layer
│   ├── model.py            # Kiến trúc Transformer tổng quát
│   ├── positional.py       # Positional encoding
│   ├── token_embedding.py  # Embedding layers
│   └── utils.py            # Các hàm tiện ích
└── weights/                # Lưu trữ trọng số mô hình sau khi train
```

## 🛠️ Cài đặt

1. Clone repository:
    ```bash
    git clone https://github.com/your-username/transformer-from-scratch.git
    cd transformer-from-scratch
    ```

2. Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Hướng dẫn sử dụng

### 1. Cấu hình
Chỉnh sửa các thông số như `batch_size`, `learning_rate`, `d_model`, `num_layers` trong file `configs/config.yaml`.

### 2. Tiền xử lý dữ liệu
Đặt dữ liệu vào thư mục `data/raw` và chạy script xử lý (nếu có) để chuẩn bị format cho `dataset.py`.

### 3. Huấn luyện
Bắt đầu quá trình huấn luyện bằng cách chạy:
```bash
python train.py
```

### 4. Đánh giá
Sau khi huấn luyện, bạn có thể kiểm tra hiệu suất của mô hình trên tập test:
```bash
python evaluate.py
```

## 📚 Tài liệu tham khảo

- Bài báo: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- Blog: [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) by Harvard NLP
- Blog: [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) by Jay Alammar

---
*Dự án đang trong quá trình phát triển và hoàn thiện.*
