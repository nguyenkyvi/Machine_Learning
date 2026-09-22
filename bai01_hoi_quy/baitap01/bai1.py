import pandas as pd

# Đọc dữ liệu (file gia_nha.csv đang nằm cùng thư mục)
df = pd.read_csv("gia_nha.csv")

# Lọc nhóm căn hộ > 100 m2
nhom_lon = df[df["dien_tich"] > 100]
so_can = len(nhom_lon)
gia_tb = nhom_lon["gia"].mean()

print(f"So can co dien tich > 100 m2: {so_can}")
print(f"Gia trung binh cua nhom can lon: {gia_tb:.2f} ty dong")