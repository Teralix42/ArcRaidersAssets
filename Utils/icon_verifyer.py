import os

DIR_1 = r"D:\Path\To\Content\Pioneer\Items"
DIR_2 = os.getcwd()

PREFIX = "T_UI_Icon"
VALID_EXTS = {".png", ".json"}


def get_matching_files(root_dir):
	found = set()

	for root, _, files in os.walk(root_dir):
		for file in files:

			name, ext = os.path.splitext(file)

			if not name.startswith(PREFIX):
				continue

			if ext.lower() not in VALID_EXTS:
				continue

			# Store WITHOUT extension
			found.add(name.lower())

	return found


files_1 = get_matching_files(DIR_1)
files_2 = get_matching_files(DIR_2)

print(f"found {len(files_1)} in extract and {len(files_2)} in this dir")

missing_in_dir2 = sorted(files_1 - files_2)

print(f"\nMissing from current dir:\n")

for file in missing_in_dir2:
	print(file)

print(f"\nTotal missing: {len(missing_in_dir2)}")