# ================= บทที่ 3: Brute Force vs. Hash Map (Two Sum) ================= #
# โจทย์: กำหนดลิสต์ตัวเลข nums และค่าเป้าหมาย target
#       จงคืนค่า index ของเลข 2 ตัวที่บวกกันได้เท่ากับ target (ห้ามใช้ตำแหน่งเดิมซ้ำ)


# ------------------------------------------------------------------------------
# วิธีที่ 1: Brute Force (ลูปซ้อนลูป - ลองจับคู่ทุกคู่)
# Time Complexity: O(n^2) | Space Complexity: O(1)
# ------------------------------------------------------------------------------
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    # (1) เก็บจำนวนสมาชิกทั้งหมดไว้ใน n
    n = len(nums)

    # (2) ลูปนอก: เลือกตัวแรกที่ตำแหน่ง i
    for i in range(n):
        # (3) ลูปใน: เลือกตัวที่สองที่ตำแหน่ง j โดยเริ่มที่ i + 1
        #     * เริ่มที่ i + 1 เพื่อไม่ให้จับคู่กับตัวมันเอง และไม่ตรวจคู่ซ้ำย้อนหลัง
        for j in range(i + 1, n):
            # (4)-(5) ถ้าบวกกันเท่ากับ target คืน index ทั้งสองทันที
            if nums[i] + nums[j] == target:
                return [i, j]

    # (6) ลองครบทุกคู่แล้วไม่เจอ คืนลิสต์ว่าง
    return []


# ------------------------------------------------------------------------------
# วิธีที่ 2: Hash Map (dict ใน Python) - ระดับผ่านสัมภาษณ์!
# แนวคิด: เดินดูทีละตัว แล้วเช็กว่า "คู่ที่ขาดอยู่ (complement = target - num)"
#        เคยเดินผ่านมาแล้วหรือยังใน O(1)
# Time Complexity: O(n) | Space Complexity: O(n)  <-- Time-Space Trade-off!
# ------------------------------------------------------------------------------
def two_sum(nums: list[int], target: int) -> list[int]:
    # (1) สร้าง Dictionary ว่าง เก็บ {ค่าตัวเลข: index} ที่เคยเดินผ่านมาแล้ว
    seen = {}

    # (2) วนลูปทีละตัวด้วย enumerate เพื่อได้ทั้ง index (i) และค่า (num) พร้อมกัน
    for i, num in enumerate(nums):
        # (3) คำนวณหา "คู่ที่ขาดอยู่" ที่จะบวกกับ num แล้วได้ target
        complement = target - num

        # (4)-(5) เช็กใน dict (ใช้เวลา O(1)!) ว่าเคยเจอคู่ที่ขาดมาก่อนหรือไม่
        #         * สำคัญ: ต้องเช็กก่อนแล้วค่อยเก็บ เพื่อกันไม่ให้หยิบตัวเดิมมาจับคู่กับตัวเอง
        if complement in seen:
            return [seen[complement], i]

        # (6) ถ้ายังไม่เจอคู่ ให้จดค่าปัจจุบันและ index ไว้ใน seen รอจับคู่ในรอบถัดไป
        seen[num] = i

    # (7) เดินครบทั้งลิสต์แล้วไม่เจอคู่ที่ตรงเงื่อนไข คืนลิสต์ว่าง
    return []


# ------------------------------------------------------------------------------
# โบนัส: Hash Set (set ใน Python) - ใช้เช็กข้อมูลซ้ำใน O(n)
# เมื่อไม่จำเป็นต้องจำ index (จำแค่ว่า "เคยเห็นหรือยัง") ใช้ set จะสั้นและประหยัดกว่า dict
# ------------------------------------------------------------------------------
def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:   # ค้นหาใน set ใช้เวลา O(1)
            return True
        seen.add(num)
    return False


# --- ทดลองเรียกใช้งานและเทสต์ Edge Cases ---
if __name__ == "__main__":
    numbers = [2, 11, 7, 15]
    print("Brute Force [2, 11, 7, 15], target=9 :", two_sum_brute_force(numbers, 9))  # [0, 2]
    print("Hash Map    [2, 11, 7, 15], target=9 :", two_sum(numbers, 9))              # [0, 2]

    # Edge Case 1: มีเลขซ้ำที่บวกกันได้ target พอดี (3 + 3 = 6)
    print("Duplicate   [3, 3], target=6         :", two_sum([3, 3], 6))             # [0, 1]

    # Edge Case 2: เลขครึ่งหนึ่งของ target แต่มีตัวเดียว (ห้ามคืน [0, 0]!)
    print("Single half [3, 2, 4], target=6      :", two_sum([3, 2, 4], 6))          # [1, 2]

    # Edge Case 3: ไม่มีคำตอบ / ลิสต์ว่าง
    print("No solution [1, 2, 3], target=99     :", two_sum([1, 2, 3], 99))         # []
    print("Empty list  [], target=5             :", two_sum([], 5))                 # []

    # ทดสอบ Hash Set
    print("Has duplicate [1, 2, 3, 1]           :", has_duplicate([1, 2, 3, 1]))    # True
    print("Has duplicate [1, 2, 3, 4]           :", has_duplicate([1, 2, 3, 4]))    # False


# ================= สรุป Big-O และ Dry Run ================= #
# เปรียบเทียบ Time-Space Trade-off:
#   - Brute Force : Time O(n^2) | Space O(1)  -> ช้ามากเมื่อ n ใหญ่ (100,000 ตัว ~ 1 หมื่นล้านรอบ)
#   - Hash Map    : Time O(n)   | Space O(n)  -> เร็วมาก เดินรอบเดียว (100,000 ตัว = 100,000 รอบ)
#
# Dry Run สำหรับ two_sum([2, 11, 7, 15], target=9):
#   รอบที่ 1: i=0, num=2  -> complement=7  -> 7 อยู่ใน {} ไหม? ไม่  -> seen = {2: 0}
#   รอบที่ 2: i=1, num=11 -> complement=-2 -> -2 อยู่ใน seen? ไม่  -> seen = {2: 0, 11: 1}
#   รอบที่ 3: i=2, num=7  -> complement=2  -> 2 อยู่ใน seen? มี!   -> return [seen[2], 2] = [0, 2]
