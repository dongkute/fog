# 1D-ResNet Ensemble for Freezing of Gait Prediction Trained on Data Collected From a Wearable 3D Lower Back Sensor

![Test Image 1](plots/overview.png)
<br /><br />This repository is home to the source code for the results reported in

[Freezing of Gait Prediction From Accelerometer Data Using a Simple 1D-Convolutional Neural Network -- 8th Place Solution for Kaggle's Parkinson's Freezing of Gait Prediction Competition
](https://arxiv.org/abs/2307.03475).

The paper presents a Deep-Learning based approach to detecting Freezing of Gait (FOG) in accelerometer data.


## Requirements

#### Inference and Evaluation

A standard computer with enough RAM is required for inference and evaluation.

#### Training

For training, an NVIDIA GPU with > 10 GB VRAM is recommended. The algorithm was developed on an NVIDIA RTX3060 with 12 GB of VRAM. Model training  took ~5 hours. As Pytorch's automatic mixed precision feature was utilized, the training code can not be
run on a CPU / Mac while inference and evaluation work on these systems without modifications. 


## Installation
```sh
# install pytorch
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```
```sh
# clone repository
$ git clone https://github.com/janbrederecke/fog
```
```sh
# install requirements
$ cd fog
$ pip install -r requirements.txt
```

Vì tập dữ liệu quá lớn nên không tải hết lên github được, chỉ tải tượng trưng tầm 1/20 cơ sở dữ liệu train ban đầu. 
Tập dữ liệu hoàn chỉnh có ở link : https://www.kaggle.com/competitions/tlvmc-parkinsons-freezing-gait-prediction/data
Tải tập kaggle models ở link drive https://drive.google.com/drive/folders/11iWILyCtXX2gsGISFRZbtkxnrygfzINf?usp=sharing và đặt nó trong `./weights/FoG/`.
Tiến hành inference:

```sh
$ python main.py inference kaggle_models
```

Inference chạy trong dữ liệu ở `/data/test/`.
Kết quả sẽ được lưu trong file results.csv


## Huấn luyện mô hình
Tải tập dữ liệu nói ở trên sau đó đặt `defog` và `tdcsfog` trong `./data/train/`.

đặt metadata files for `defog` and `tdcsfog` in `./data/`.

Bắt đầu huấn luyện
```sh
$ python main.py train
```

log sẽ được ghi trong `./weights/FoG/`.

## Đánh giá
Kết quả đánh giá sẽ được ghi trong `./weights/FoG/`.( evalution_metrics_kaggle_models.npy)

```sh
$ python main.py evaluation kaggle_models
```
Tính độ chênh lệch giữa mô hình thực thi và mô hình có sẵn của bài báo bằng cách chạy file percent.py
