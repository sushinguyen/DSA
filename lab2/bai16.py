import math

def koko_eating_bananas(piles, h):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / mid)
            
        if total_hours <= h:
            right = mid
        else:
            left = mid + 1
            
    return left

piles = [3, 6, 7, 11]
h = int(input("Nhập: "))
result = koko_eating_bananas(piles, h)

print(f"Tốc độ ăn chuối nhỏ nhất của Koko là: {result} quả/giờ")