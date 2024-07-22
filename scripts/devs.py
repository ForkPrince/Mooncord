import os
import re
import subprocess
import shutil

# NOTE: This is the worst code I've ever written, but it works.
def clone_repo(repo_url, clone_dir):
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    subprocess.run(["git", "clone", repo_url, clone_dir], check=True)

def find_object_in_file(file_path, object_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = re.compile(rf'export const {object_name} = Object\.freeze\((.+?) satisfies Record<string, Dev>\);', re.DOTALL)
    match = pattern.search(content)

    if match:
        return match.group(0), match.group(1)
    else:
        raise ValueError(f"Object {object_name} not found in {file_path}")

def update_file_with_new_object(target_file_path, object_name, new_object_content):
    with open(target_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = re.compile(rf'export const {object_name} = Object\.freeze\((.+?) satisfies Record<string, Dev>\);', re.DOTALL)
    updated_content = pattern.sub(f'export const {object_name} = Object.freeze({new_object_content} satisfies Record<string, Dev>);', content)

    with open(target_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def main():
    repo_url = "https://github.com/Equicord/Equicord.git"
    object_file_path = "src/utils/constants.ts"
    target_file_path = "./src/utils/constants.ts"
    object_name = "EquicordDevs"

    clone_dir = "./temp/devs"

    clone_repo(repo_url, clone_dir)

    full_object_path = os.path.join(clone_dir, object_file_path)
    _, new_object_content = find_object_in_file(full_object_path, object_name)

    update_file_with_new_object(target_file_path, object_name, new_object_content)

    shutil.rmtree("./temp")

    print(f"Successfully updated {object_name} in {target_file_path}")

if __name__ == "__main__":
    main()
