import os
import stat
import uuid
from pathlib import Path

# ====== CẤU HÌNH ======
ROOT_PATH = "D:/"  

# Chọn chế độ: 1, 2 hoặc 3
#   1 = Viết Hoa Chữ Cái Đầu Mỗi Từ
#   2 = Chỉ viết hoa chữ cái đầu của tên
#   3 = Viết Hoa Chữ Cái Đầu Mỗi Từ
#   4 = VIẾT HOA TOÀN BỘ TÊN
CHE_DO = 4


GIU_NGUYEN = ["HĐND", "UBND", "TTPVHCC", "TTHC", "CNTT", "TTDVTH", "ĐU", "CAT"]


BO_QUA = ["Code", "System Volume Information", "$RECYCLE.BIN"]
# ======================

CAC_CHE_DO = {
    1: ("title", False),
    2: ("cau", False),
    3: ("title", False),
    4: ("upper", False),
}

if CHE_DO not in CAC_CHE_DO:
    raise SystemExit("CHE_DO chỉ được là 1, 2 hoặc 3.")
KIEU, DRY_RUN = CAC_CHE_DO[CHE_DO]

GIU_NGUYEN_SET = {w.upper() for w in GIU_NGUYEN}
BO_QUA_SET = {n.lower() for n in BO_QUA}


def tao_ten_moi(name: str) -> str:
    if KIEU == "upper":
        return " ".join(
            w.upper() if w.upper() in GIU_NGUYEN_SET else w.upper()
            for w in name.split(" ")
        )

    kq = []
    for w in name.lower().split(" "):
        if w == "":
            kq.append(w)
        elif w.upper() in GIU_NGUYEN_SET:
            kq.append(w.upper())
        elif KIEU == "title":
            kq.append(w[0].upper() + w[1:])
        else:
            kq.append(w)

    s = " ".join(kq)
    if KIEU == "cau" and s:
        s = s[0].upper() + s[1:]
    return s


def la_thu_muc_he_thong(p: Path) -> bool:
    """True nếu là thư mục hệ thống/ẩn hoặc tên bắt đầu bằng '$'."""
    if p.name.startswith("$"):
        return True
    try:
        attrs = os.stat(p).st_file_attributes  
    except AttributeError:
        return False
    except OSError:
        return True 
    return bool(attrs & (stat.FILE_ATTRIBUTE_HIDDEN | stat.FILE_ATTRIBUTE_SYSTEM))


def thu_thap_thu_muc(root: Path) -> list[Path]:
    ket_qua = []
    for dirpath, dirnames, _ in os.walk(root):
        giu = []
        for d in dirnames:
            p = Path(dirpath) / d
            if d.lower() in BO_QUA_SET or la_thu_muc_he_thong(p):
                continue
            giu.append(d)
            ket_qua.append(p)
        dirnames[:] = giu  
    return ket_qua


def main():
    root = Path(ROOT_PATH)
    if not root.is_dir():
        print(f"Không tìm thấy thư mục: {root}")
        return

    thu_muc = thu_thap_thu_muc(root)
    thu_muc.sort(key=lambda p: len(str(p)), reverse=True)

    for p in thu_muc:
        ten_cu = p.name
        ten_moi = tao_ten_moi(ten_cu)
        if ten_moi == ten_cu:
            continue

        if DRY_RUN:
            print(f"{ten_cu}  -->  {ten_moi}")
            continue

        tmp = p.parent / f"{ten_cu}_tmp_{uuid.uuid4().hex[:6]}"
        try:
            p.rename(tmp)
            tmp.rename(p.parent / ten_moi)
            print(f"Đã đổi: {ten_cu}  -->  {ten_moi}")
        except OSError as e:
            print(f"Lỗi khi đổi '{ten_cu}': {e}")
            if tmp.exists() and not p.exists(): 
                tmp.rename(p)


if __name__ == "__main__":
    main()