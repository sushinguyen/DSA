1. khởi tạo biến i = 0
2. giả sử đúng -> i + 1
xét mảng con từ vị trí 0 đến n-i-1
 lượt thứ $i+1$, thuật toán so sánh và hoán đổi các cặp phần tử kề nhau từ trái sang phải trong mảng con này
 Mỗi lần gặp phần tử lớn hơn, nó sẽ được và đẩy sang phải
 Kết thúc lượt lặp, phần tử lớn nhất trong mảng con (cũng chính là phần tử lớn thứ $i+1$ của toàn bộ mảng) sẽ bị đẩy về vị trí cuối cùng của mảng con, tức là vị trí n-(i+1). Do đó, bất biến được duy trì
3. Vòng lặp kết thúc khi i = n hoặc khi thuật toán early-exit xác định không còn hoán đổi nào, tức là mảng đã sắp xếp. Theo bất biến vòng lặp, lúc này $n$ phần tử lớn nhất đã nằm đúng vị trí, đồng nghĩa với việc toàn bộ mảng đã được sắp xếp tăng dần. Điều này chứng minh thuật toán dừng và chạy đúng.