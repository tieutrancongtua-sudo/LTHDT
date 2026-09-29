from employee import Employee


class SoftwareEngineer(Employee):

    def __init__(self, id, fullName, *args):
        # 1. Xác định các giá trị dựa trên số lượng args
        if len(args) == 1:
            primaryLanguage = args[0]
            baseSalary = 0.0
            technicalAllowance = 0.0
        elif len(args) == 3:
            baseSalary = args[0]
            primaryLanguage = args[1]
            technicalAllowance = args[2]
        else:
            raise TypeError("Số lượng tham số không hợp lệ (phải là 1 hoặc 3).")

        # 2. Kiểm tra ràng buộc riêng của lớp con
        if not primaryLanguage or not str(primaryLanguage).strip():
            raise ValueError("Ngôn ngữ lập trình chính không được rỗng.")
        if technicalAllowance < 0:
            raise ValueError("Phụ cấp kỹ thuật không được âm.")

        # 3. Gọi constructor lớp cha để gán _id, _fullName, _baseSalary
        super().__init__(id, fullName, baseSalary)

        # 4. Gán thuộc tính riêng của lớp con
        self._primaryLanguage = str(primaryLanguage).strip()
        self._technicalAllowance = float(technicalAllowance)

    @property
    def primaryLanguage(self):
        return self._primaryLanguage

    @property
    def technicalAllowance(self):
        return self._technicalAllowance

    def calculateMonthlyCost(self):
        return self._baseSalary + self._technicalAllowance

    def displayInfo(self):
        print(
            f"[SoftwareEngineer] Mã: {self._id} | "
            f"Họ tên: {self._fullName} | "
            f"Lương CB: {self._baseSalary:.2f} | "
            f"Ngôn ngữ: {self._primaryLanguage} | "
            f"Phụ cấp: {self._technicalAllowance:.2f} | "
            f"Chi phí tháng: {self.calculateMonthlyCost():.2f}"
        )

    def __del__(self):
        print(f"-> Destructor SoftwareEngineer: {self._id} - {self._fullName}")