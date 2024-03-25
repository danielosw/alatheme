# Alatheme
A simple python program that manages alacritty themes.
Currently it only works under the following assumptions:
Your alacritty config is at ~/.config/alacritty/alicritty.toml or ~/appdata/local/alicritty.toml
Your themes are toml files and are in ~/.config/alacritty/themes/ or ~/appdata/local/themes/
And that you only you the ['import'] toml table is only used for your theme.
WARNING: If you run it with the first two conditions met, but not the last one, then your ['import'] table will get overwrite permently.
Their is also a helper function to make it easier to setup auto complete for fish. To use it, run python -m alatheme complete_fish.
