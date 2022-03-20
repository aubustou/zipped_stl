import shutil
from pathlib import Path
from zipfile import ZipFile

DOWNLOAD_FOLDER = Path("G:\Téléchargements")
THREED_STUFF_FOLDER = Path("G:") / "3D"


def recursive_rename(src: Path, dst: Path, iteration: int = 1) -> None:
    if not dst.exists():
        print(str(dst))
        shutil.move(str(src), dst)
        return

    renamed_dst = dst.parent / (dst.stem + f".{iteration}" + dst.suffix)

    if renamed_dst.exists():
        recursive_rename(src, dst, iteration + 1)
    else:
        shutil.move(str(src), renamed_dst)
        print(str(renamed_dst))

def move_stls():
    for file_ in DOWNLOAD_FOLDER.iterdir():
        if file_.suffix.lower() == ".zip":
            files = ZipFile(file_).namelist()
            if any(x.lower().endswith(".stl") for x in files) or any(x.lower().endswith(".obj") for x in files):
                #print(str(file_))
                recursive_rename(file_, THREED_STUFF_FOLDER / file_.name)


                #shutil.move(str(file_), THREED_STUFF_FOLDER / file_.name)





if __name__ == '__main__':
    move_stls()

