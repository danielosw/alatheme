import tomlkit
from argparse import ArgumentParser
from pathlib import Path
from os import listdir
from os.path import isfile, join
import sys
def main() -> None:
    parse = ArgumentParser(
            prog="Alatheme",
            description='Makes it easier to switch between themes in alacritty'
            )
    parse.add_argument('name', action='store')
    theme = parse.parse_args()
    theme = theme.name
    fileopened: bool = False
    if theme == "complete_fish":
        print(list())
        sys.exit()
    try:
        path = str(Path.home())+"/.config/alacritty/alacritty.toml"
        with open(path, "r+") as f:
            fileopened = True
            toml = tomlkit.parse(f.read().strip())
    except FileNotFoundError:
        pass
    if fileopened is False:
        try:
            path = str(Path.home())+"\\appdata\\roaming\\alacritty\\alacritty.toml"
            with open(path, "r+") as f:
                fileopened = True
                toml = tomlkit.parse(f.read().strip())
        except FileNotFoundError:
            pass
    if fileopened is False:
        raise FileNotFoundError("Unable to find alacritty.toml")
    else:
        if Path(str(Path.home())+"/.config/alacritty/themes/"+theme+".toml").is_file():
            toml['import'] = ['~/.config/alacritty/themes/'+theme+'.toml']
            with open(path, "w+") as f:
                f.write(tomlkit.dumps(toml))
        elif Path(str(Path.home())+"\\appdata\\roaming\\alacritty\\themes\\"+theme+".toml").is_file():
            toml['import'] = [str(Path.home())+"\\appdata\\roaming\\alacritty\\themes\\"+theme+".toml"]
            with open(path, "w+") as f:
                f.write(tomlkit.dumps(toml))
        else:
            raise FileNotFoundError("Unable to find "+theme+".toml")
    print("Successful edited file")
def list() -> str:
    try:
        path = str(Path.home())+"/.config/alacritty/themes/"
        themes = [f for f in listdir(path) if isfile(join(path, f))]
    except FileNotFoundError:
        try:
            path = str(Path.home())+"\\appadata\\roaming\\alacritty\\themes\\"
            themes = [f for f in listdir(path) if isfile(join(path, f))]
        except FileNotFoundError:
            raise FileNotFoundError("Can't find themes")
 
    themesstr: str = ""
    for theme in themes:
        themesstr+=theme.strip().replace(".toml","")+"\n"
    return themesstr

if __name__ == "__main__":
    main()
