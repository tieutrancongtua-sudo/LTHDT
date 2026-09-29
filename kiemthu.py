
from employee import Employee
from software_engineer import SoftwareEngineer
from project_team import ProjectTeam 

# CHƯƠNG TRÌNH KIỂM THỬ THEO KỊCH BẢN
def main():
    print("========== BẮT ĐẦU KIỂM THỬ ==========\n")

    # 1. Tạo hai Employee bằng hai constructor khác nhau
    e1 = Employee()  # mặc định
    e2 = Employee("E002", "Nguyễn Văn A", 1000.0)
    print("1. Đã tạo 2 Employee:")
    e1.displayInfo()
    e2.displayInfo()

    # 2. Tạo hai SoftwareEngineer bằng hai constructor khác nhau
    se1 = SoftwareEngineer("SE001", "Trần Thị B", "Python")
    se2 = SoftwareEngineer("SE002", "Lê Văn C", 1500.0, "C++", 300.0)
    print("\n2. Đã tạo 2 SoftwareEngineer:")
    se1.displayInfo()
    se2.displayInfo()

    # 3. Tăng lương một nhân sự bằng số tiền cố định
    print("\n3. Tăng lương e2 thêm 200 (cố định):")
    e2.increaseSalary(200)
    e2.displayInfo()

    # 4. Tăng lương một nhân sự khác theo phần trăm
    print("\n4. Tăng lương se2 thêm 10%:")
    se2.increaseSalary(10, True)
    se2.displayInfo()

    # 5. Tạo nhóm dự án không có trưởng nhóm
    team1 = ProjectTeam("P001", "Dự án Alpha")
    print("\n5. Đã tạo nhóm không có trưởng nhóm:")
    team1.displayTeam()

    # 6. Thêm một nhân sự vào nhóm bằng addMember(employee)
    print("\n6. Thêm e2 vào nhóm:")
    team1.addMember(e2)
    team1.displayTeam()

    # 7. Thêm một kỹ sư bằng addMember(employee, true) để đặt làm trưởng nhóm
    print("\n7. Thêm se2 làm trưởng nhóm:")
    team1.addMember(se2, True)
    team1.displayTeam()

    # 8. Thử thêm lại một thành viên đã tồn tại
    print("\n8. Thử thêm lại e2 (đã tồn tại):")
    team1.addMember(e2)

    # 9. Hiển thị danh sách bằng lời gọi đa hình
    print("\n9. Hiển thị danh sách (đa hình):")
    team1.displayTeam()

    # 10. Tính tổng chi phí nhân sự hằng tháng
    print(f"\n10. Tổng chi phí tháng của nhóm: {team1.calculateTotalMonthlyCost():.2f}")

    # 11. Thử xóa trưởng nhóm hiện tại và kiểm tra thao tác bị từ chối
    print("\n11. Thử xóa trưởng nhóm se2:")
    team1.removeMember(se2.id)

    # 12. Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm
    print("\n12. Đổi trưởng nhóm sang e2, rồi xóa se2:")
    team1.changeLeader(e2)
    team1.removeMember(se2.id)
    team1.displayTeam()

    # 13. Tạo nhóm thứ hai và thêm một nhân sự đã có ở nhóm thứ nhất
    print("\n13. Tạo nhóm thứ hai và thêm e2 (đã ở nhóm 1):")
    team2 = ProjectTeam("P002", "Dự án Beta")
    team2.addMember(e2)
    team2.displayTeam()

    # 14. Hủy nhóm thứ hai bằng cách kết thúc một khối lệnh cục bộ
    print("\n14. Hủy nhóm thứ hai (kết thúc khối lệnh cục bộ):")
    del team2

    # 15. Chứng minh nhân sự của nhóm thứ hai vẫn tồn tại sau khi nhóm bị hủy
    print("\n15. Kiểm tra e2 vẫn tồn tại sau khi nhóm 2 bị hủy:")
    e2.displayInfo()
    print("=> e2 vẫn hoạt động bình thường.")

    print("\n========== KẾT THÚC KIỂM THỬ ==========")


if __name__ == "__main__":
    main()