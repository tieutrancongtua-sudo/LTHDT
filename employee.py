class Employee:
    
   # Lớp nhân sự thông thường.
   #Trách nhiệm: Quản lý thông tin cơ bản của nhân sự (mã, họ tên, lương cơ bản).

    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", baseSalary=0.0):
        # Ràng buộc: id và fullName không rỗng, baseSalary không âm
        if not id or not str(id).strip():
            raise ValueError("Mã nhân sự không được rỗng.")
        if not fullName or not str(fullName).strip():
            raise ValueError("Họ tên không được rỗng.")
        if baseSalary < 0:
            raise ValueError("Lương cơ bản không được âm.")
        self._id = str(id).strip()
        self._fullName = str(fullName).strip()
        self._baseSalary = float(baseSalary)

    # Getter
    @property
    def id(self):
        return self._id

    @property
    def fullName(self):
        return self._fullName

    @property
    def baseSalary(self):
        return self._baseSalary

    # Nạp chồng increaseSalary
    def increaseSalary(self, value: float, byPercentage: bool = False):
        """
        Nếu byPercentage=False (mặc định): tăng cố định.
        Nếu byPercentage=True: tăng theo %.
        """
        if value <= 0:
            raise ValueError("Giá trị tăng phải dương.")
        if byPercentage:
            self._baseSalary += self._baseSalary * (value / 100.0)
        else:
            self._baseSalary += value

    def calculateMonthlyCost(self) -> float:
       # Mặc định bằng lương cơ bản.
        return self._baseSalary

    def displayInfo(self):
        print(f"[Employee] Mã: {self._id} | Họ tên: {self._fullName} | "
              f"Lương cơ bản: {self._baseSalary:.2f} | Chi phí tháng: {self.calculateMonthlyCost():.2f}")

    def __del__(self):
        emp_id = getattr(self, "_id", "<không xác định>")
        emp_name = getattr(self, "_fullName", "<không xác định>")
        print(f"-> Destructor Employee: {emp_id} - {emp_name}")

    def __str__(self):
        return f"{self._id} - {self._fullName}"