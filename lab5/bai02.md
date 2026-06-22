# 1.Khởi tạo
* Tập các đỉnh chưa chốt: T = {0,1,2,3,4,5}
* Nhãn khoảng cách: L(0) = 0, các đỉnh còn lại L(1) = L(2) = L(3) = L(4) = L(5) = $\infty$
* Đỉnh liền trước: P(x) = $P(x)=\emptyset$ với mọi x.

# 2.Các bước lặp chi tiết
**Bước 1: Chốt đỉnh 0**
* Chọn v = 0 (vì L(0) = 0 nhỏ nhất). Loại khỏi tập: T = {1,2,3,4,5}.
* Cập nhật các đỉnh liền kề của 0:
    * Đỉnh 1: L(1) = min($\infty$, 0+4) = 4 => P(1) = 0
    * Đỉnh 2: L(2) = min($\infty$, 0+1) = 1 => P(2) = 0

**Bước 2: Chốt đỉnh 2**
* Chọn v = 2 (vì L(2) = 1 nhỏ nhất). Loại khỏi tập: T = {1,3,4,5}.
* Cập nhật các đỉnh liền kề của 2:
    * Đỉnh 1: L(1) = min(4, 1+2) = 3 => P(1) = 2
    * Đỉnh 3: L(3) = min($\infty$, 1+5) = 6 => P(3) = 2
    * Đỉnh 4: L(4) = min($\infty$, 1+8) = 9 => P(4) = 2

**Bước 3: Chốt đỉnh 1**
* Chọn v = 1 (vì L(1) = 3 nhỏ nhất). Loại khỏi tập: T = {3,4,5}
* Cập nhật các đỉnh liền kề của 1:
    * Đỉnh 3: L(3) = min(6, 3+1) = 4 => P(3) = 1

**Bước 4: Chốt đỉnh 3**
* Chọn v = 3 (vì L(3) = 4 nhỏ nhất). Loại khỏi tập: T = {4,5}
* Cập nhật các đỉnh liền kề của 3:
    * Đỉnh 4: L(4) = min(9, 4+3) = 7 => P(4) = 3
    * ĐỈnh 5: L(5) = min($\infty$, 4+6) = 10 => P(5) = 3

**Bước 5: CHốt đỉnh 4**
* Chọn v = 4 (vì L(4) = 7 nhỏ nhất). Loại khỏi tập: T = {5}
* Cập nhật các đỉnh liền kề của 4:
    * Đỉnh 5: L(5) = min(10, 7+2) = 9 => P(5) = 4

**Bước 6: Chốt đỉnh 5**
* Chọn v = 5 (vì L(5) = 9 nhỏ nhất). Tập T = 0
* Không còn đỉnh nào kề chưa chốt --> Kết thúc thuật toán

# 3.Kết luận
**Khoảng cách ngắn nhất từ đỉnh 0:**
* L(0) = 0
* L(1) = 3
* L(2) = 1
* L(3) = 4
* L(4) = 7
* L(5) = 9
**Truy vết đường đi ngắn nhất đến đỉnh cuối (đỉnh 5):**
* Đi Ngược từ các đỉnh liền trước: 5 <-- 4 (P(5)=4) <-- 3 (P(4)=3) <-- 1 (P(3)=1) <-- 2 (P(1)=2) <-- 0 (P(2)=0)
* Đường đi ngắn nhất: 0 --> 2 --> 1 --> 3 --> 4 --> 5