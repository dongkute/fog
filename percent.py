import numpy as np

# Dữ liệu của bạn (đã tính trung bình)
your_avg = {
    'mAP': np.mean([0.277903, 0.261249, 0.185500, 0.308754, 0.203665]),
    'ap_start': np.mean([0.061634, 0.008923, 0.053733, 0.029437, 0.012888]),
    'ap_turn': np.mean([0.687165, 0.562762, 0.421334, 0.644419, 0.575519]),
    'ap_walk': np.mean([0.084910, 0.212061, 0.081433, 0.252407, 0.022590])
}

# Dữ liệu bài báo (đã tính trung bình)
paper_avg = {
    'mAP': np.mean([0.277, 0.261, 0.185, 0.309, 0.203]),
    'ap_start': np.mean([0.063, 0.010, 0.054, 0.029, 0.013]),
    'ap_turn': np.mean([0.682, 0.562, 0.420, 0.644, 0.575]),
    'ap_walk': np.mean([0.085, 0.212, 0.082, 0.252, 0.023])
}

# Tính chênh lệch %
diff = {
    'mAP': (your_avg['mAP'] - paper_avg['mAP']) / paper_avg['mAP'] * 100,
    'ap_start': (your_avg['ap_start'] - paper_avg['ap_start']) / paper_avg['ap_start'] * 100,
    'ap_turn': (your_avg['ap_turn'] - paper_avg['ap_turn']) / paper_avg['ap_turn'] * 100,
    'ap_walk': (your_avg['ap_walk'] - paper_avg['ap_walk']) / paper_avg['ap_walk'] * 100
}

print("Kết quả trung bình:")
print(f"mAP: {your_avg['mAP']:.4f} (bài báo: {paper_avg['mAP']:.4f}) → Chênh lệch: {diff['mAP']:.2f}%")
print(f"AP StartHesitation: {your_avg['ap_start']:.4f} (bài báo: {paper_avg['ap_start']:.4f}) → Chênh lệch: {diff['ap_start']:.2f}%")
print(f"AP Turn: {your_avg['ap_turn']:.4f} (bài báo: {paper_avg['ap_turn']:.4f}) → Chênh lệch: {diff['ap_turn']:.2f}%")
print(f"AP Walking: {your_avg['ap_walk']:.4f} (bài báo: {paper_avg['ap_walk']:.4f}) → Chênh lệch: {diff['ap_walk']:.2f}%")