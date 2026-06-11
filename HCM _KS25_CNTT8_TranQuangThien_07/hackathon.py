transaction = [
    {
        "id": "TX001",
        "content": "Thu tien ban hang thang 5",
        "type": "Thu",
        "price": 25000000,
        "tax": 10,
        "actual": 27500000,
        "classify": "Lớn"
    },
{
        "id": "TX002",
        "content": "Thu tien ban hang thang 6",
        "type": "Thu",
        "price": 98000000,
        "tax": 15,
        "actual": 19500000,
        "classify": "Nhỏ"
    }
]
while True:
    choice = input('''
================MENU================
1. Hiển thị nhật ký giao dịch
2.Ghi nhận giao dịch mới
3. Cập nhập chứng từ giao dịch
4. Xóa giao dịch lỗi
5. Tìm kiếm giao dịch
6. Thống kê tổng tiền
7. Phân loại quy mô tự động
8. Thoát chương trình 
=====================================
Mời bạn chọn chức năng (1-8): ''')
    match choice:
        case "1":
            print('-- NHẬT KÝ THU CHI --')
            header = f'{"Mã TX":<5} | {"Nội dung" :<30} | {"Loại":<5} | {"Số tiền gốc":<15} | {"Thuế suất":<10} | {"Số tiền thực tế":<16} | {"Phân loại quy mô":<17}'
            print(header)
            print('-'* len(header))
            for value in transaction:
                print(f'{value["id"]:<5} | {value["content"]:<30} | {value["type"]:<5} | {value["price"]:<15} | {value["tax"]:<10} | {value["actual"]:<16} | {value["classify"]:<17}')
                print('-'* len(header))
        case "2":
            print('-- NHẬP GIAO DỊCH --')
            id_tx = input('Nhập mã TX: ').strip().upper()
            content = input('Nhập vào nội dung: ').strip()
            type_transaction = input('Nhập vào loại giao dịch: ').strip()
            price = int(input('Số tiền phát sinh: '))
            tax = int(input('Thuế suất: '))
            actual = int(price * ( 1 + tax / 100))
            classify = ""
            if actual < 2000000:
                classify = "Nhỏ"
            elif actual > 2000000 and actual < 10000000:
                classify = "Vừa"
            elif actual > 10000000 and actual < 50000000:
                classify = "Lớn"
            else:
                classify = "Rất lớn"

            transaction.append(
                {
                    "id": id_tx,
                    "content": content,
                    "type": type_transaction,
                    "price":price,
                    "tax": tax,
                    "actual": actual,
                    "classify": classify
                }
            )
            print('[Thành công]: Đã thêm giao dịch mới.')



        case "3":
            id_update = input('Nhập mã giao dịch cần cập nhập: ').strip().upper()
            flag = False
            for value in transaction:
                if value["id"] == id_update:
                    value["content"] = input('Nhập vào nội dung: ').strip()
                    value["type"] = input('Nhập vào loại giao dịch: ').strip()
                    value["price"] = int(input('Số tiền phát sinh: '))
                    value["tax"] = int(input('Thuế suất: '))
                    value["actual"] = int(value["price"] * (1 + value["tax"] / 100))
                    value["classify"] = ""
                    if value["actual"] < 2000000:
                        value["classify"] = "Nhỏ"
                    elif value["actual"] > 2000000 and value["actual"] < 10000000:
                        value["classify"] = "Vừa"
                    elif value["actual"] > 10000000 and value["actual"] < 50000000:
                        value["classify"] = "Lớn"
                    else:
                        value["classify"] = "Rất lớn"
                    print(f'Đã cập nhập giao dịch có mã {id_update}')
                    flag = True
                    break
            if not flag:
                print(f'Khong tìm thấy mã {id_update}')

        case "4":
            flag = False
            id_delete = input('Nhập vào mã giao dịch muốn xóa: ').strip().upper()
            for value in transaction:
                if value["id"] == id_delete:
                    del_submit = input('Bạn có chắc chắc muốn xóa giao dịch này không (Y/N)?: ').strip().upper()
                    flag = True
                    if del_submit == "Y":
                        transaction.remove(value)
                        print('Đã xóa giao dịch')
                        break
                    else:
                        print('Lựa chọn không xóa')

            if not flag:
                print(f'Không tìm thấy mã {id_delete}')
        case "5":
            print('chuc nang 5')
        case "6":
            print('chuc nang 6')
        case "7":
            print('chuc nang 7')
        case "8":
            print('Chương trình đã được thoát. Hẹn gặp lại !!')
            break
        case _:
            print('Lựa chọn không hợp lệ!!')
