from employee import Employee
class Node:
    #Nút trong danh sách liên kết đơn (dùng nội bộ cho ProjectTeam).
    def __init__(self, employee: Employee):
        self.employee = employee
        self.next = None


class ProjectTeam:
   
   # Lớp nhóm dự án.
   # Quản lý trưởng nhóm và danh sách thành viên (liên kết đơn).
    
    def __init__(self, projectCode: str, projectName: str, leader: Employee = None):
        if not projectCode or not str(projectCode).strip():
            raise ValueError("Mã dự án không được rỗng.")
        if not projectName or not str(projectName).strip():
            raise ValueError("Tên dự án không được rỗng.")
        self._projectCode = str(projectCode).strip()
        self._projectName = str(projectName).strip()
        self._leader = None
        self._head = None  # head của danh sách liên kết
        if leader is not None:
            self._leader = leader
            # Tự động đưa trưởng nhóm vào danh sách thành viên
            self._addNode(leader)

    # ---------- Nội bộ danh sách liên kết ----------
    def _findNode(self, employeeId: str):
        cur = self._head
        while cur:
            if cur.employee.id == employeeId:
                return cur
            cur = cur.next
        return None

    def _addNode(self, employee: Employee):
        new_node = Node(employee)
        if self._head is None:
            self._head = new_node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def _removeNode(self, employeeId: str) -> bool:
        cur = self._head
        prev = None
        while cur:
            if cur.employee.id == employeeId:
                if prev is None:
                    self._head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    # ---------- Thuộc tính ----------
    @property
    def projectCode(self):
        return self._projectCode

    @property
    def projectName(self):
        return self._projectName

    @property
    def leader(self):
        return self._leader

    # ---------- Nạp chồng addMember ----------
    def addMember(self, employee: Employee) -> bool:
        return self._addMemberInternal(employee, False)

    def addMemberAsLeader(self, employee: Employee) -> bool:
        return self._addMemberInternal(employee, True)

    def _addMemberInternal(self, employee: Employee, makeLeader: bool) -> bool:
        # Không thêm trùng nhân sự
        if self.contains(employee.id):
            print(f"Không thể thêm: Nhân sự {employee.id} đã tồn tại trong nhóm.")
            return False
        self._addNode(employee)
        if makeLeader:
            # Trưởng nhóm cũ vẫn là thành viên nếu đã có trong nhóm
            self._leader = employee
        return True

    # ---------- Các phương thức khác ----------
    def removeMember(self, employeeId: str) -> bool:
        if self._leader is not None and self._leader.id == employeeId:
            print(f"Không thể xóa trưởng nhóm {employeeId} khi chưa chọn trưởng nhóm thay thế.")
            return False
        return self._removeNode(employeeId)

    def changeLeader(self, employee: Employee):
        # Trưởng nhóm mới phải được thêm vào nhóm nếu chưa phải thành viên
        if not self.contains(employee.id):
            self._addNode(employee)
        self._leader = employee

    def contains(self, employeeId: str) -> bool:
        return self._findNode(employeeId) is not None

    def calculateTotalMonthlyCost(self) -> float:
        total = 0.0
        cur = self._head
        while cur:
            total += cur.employee.calculateMonthlyCost()
            cur = cur.next
        return total

    def displayTeam(self):
        print(f"\n===== Nhóm dự án: {self._projectCode} - {self._projectName} =====")
        if self._leader:
            print(f"Trưởng nhóm: {self._leader.id} - {self._leader.fullName}")
        else:
            print("Trưởng nhóm: (chưa có)")
        print("Danh sách thành viên:")
        cur = self._head
        if cur is None:
            print("  (trống)")
        while cur:
            # Gọi đa hình displayInfo()
            cur.employee.displayInfo()
            cur = cur.next
        print(f"Tổng chi phí tháng: {self.calculateTotalMonthlyCost():.2f}")
        print("=" * 50)

    def __del__(self):
        # Chỉ hủy cấu trúc danh sách liên kết nội bộ, không hủy Employee
        code = getattr(self, "_projectCode", "<không xác định>")
        name = getattr(self, "_projectName", "<không xác định>")
        print(f"-> Destructor ProjectTeam: {code} - {name} (giải phóng danh sách liên kết)")
        cur = getattr(self, "_head", None)
        while cur:
            nxt = cur.next
            cur.next = None
            cur = nxt
        self._head = None
        self._leader = None

