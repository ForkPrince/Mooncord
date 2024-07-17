import os
import shutil
import subprocess
import json

directory = os.path.dirname(__file__)

def getPlugins(source, output = "custom", plugins = None, folder = "plugins"):
    temp = "./temp"

    folder = os.path.join(directory, "../src/", output)

    os.makedirs(folder, exist_ok=True)

    try:
        subprocess.run(["git", "clone", source, temp], check=True)
        for plugin in plugins:
            src_path = os.path.join(temp, "src", folder, plugin)
            dest_path = os.path.join(folder, plugin)

            if os.path.exists(src_path):
                shutil.move(src_path, dest_path)
                print(f"Moved {plugin} to {dest_path}")

    finally:
        shutil.rmtree(temp)

if __name__ == "__main__":
    with open(f"{directory}/sources.json", "r") as file:
        config = json.load(file)

    for source in config:
        getPlugins(source.get("source"), source.get("output"), source.get("plugins"), source.get("folder"))
