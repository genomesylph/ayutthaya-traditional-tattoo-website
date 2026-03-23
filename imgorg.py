import os

# กำหนดที่อยู่ของโฟลเดอร์
folder_path = r'C:\Users\pipat\Downloads\imgs'

# รายชื่อนามสกุลไฟล์ภาพที่ต้องการเปลี่ยนชื่อ (เพิ่มลดได้ตามจริง)
valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')

def rename_images():
    # ตรวจสอบว่า path มีอยู่จริงไหม
    if not os.path.exists(folder_path):
        print("ไม่พบโฟลเดอร์ตามที่ระบุ กรุณาเช็ก Path อีกครั้งครับ")
        return

    # ดึงรายชื่อไฟล์และกรองเฉพาะไฟล์ภาพ
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]
    
    # เรียงลำดับไฟล์ (เพื่อให้ tattoo001 เรียงตามชื่อเดิมที่มีอยู่)
    files.sort()

    count = 1
    for filename in files:
        # แยกนามสกุลไฟล์เดิมไว้ (เช่น .jpg)
        ext = os.path.splitext(filename)[1]
        
        # สร้างชื่อใหม่ในรูปแบบ tattoo001, tattoo002, ...
        # :03d หมายถึงให้เป็นเลข 3 หลัก ถ้าไม่ถึงให้เติม 0 ข้างหน้า
        new_name = f"tattoo{count:03d}{ext}"
        
        source = os.path.join(folder_path, filename)
        destination = os.path.join('imgs', new_name)

        # ทำการเปลี่ยนชื่อ
        try:
            os.rename(source, destination)
            print(f'เปลี่ยนแล้ว: {filename} -> {new_name}')
            count += 1
        except Exception as e:
            print(f'เกิดข้อผิดพลาดกับไฟล์ {filename}: {e}')

    print(f"\nเสร็จเรียบร้อย! เปลี่ยนชื่อไปทั้งหมด {count-1} ไฟล์")

if __name__ == "__main__":
    rename_images()