import tomlkit
from argparse import ArgumentParser
from pathlib import Path

def main() -> None:
    parse = ArgumentParser(
            prog="Alatheme",
            description='Makes it easier to switch between themes in alacritty'
            )
    parse.add_argument('name', action='store')
    theme = parse.parse_args()
    theme = theme.name
    fileopened: bool = False
    try:
        path = str(Path.home())+"/.config/alacritty/alacritty.toml"
        with open(path, "r+") as f:
            fileopened = True
            toml = tomlkit.parse(f.read().strip())
    except FileNotFoundError:
        pass
    if fileopened is False:
        try:
            path = str(Path.home())+"/appdata/local/alacritty.toml"
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
        elif Path(str(Path.home())+"/appdata/local/alacritty/themes/"+theme+".toml").is_file():
            toml['import'] = "~/appdata/local/alacritty/themes/"+theme+".toml"
            with open(path, "w+") as f:
                f.write(tomlkit.dumps(toml))
        else:
            raise FileNotFoundError("Unable to find"+theme+".toml")
    print("Successful edited file")

