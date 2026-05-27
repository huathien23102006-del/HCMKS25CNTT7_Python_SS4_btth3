total_bill = int(input("Nhập tổng số lượng hóa đơn: "))
max_bill = 0
min_bill = 0
for i in range (1, total_bill + 1, 1):
    in_bill = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))
    if(i == 1):
        min_bill = in_bill
        
    if(in_bill > max_bill):
        max_bill = in_bill
    
    if(in_bill < min_bill):
        min_bill = in_bill

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print(max_bill)
print(min_bill)