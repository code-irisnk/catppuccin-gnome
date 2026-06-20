# gnome-catppuccin

This script edits the standard GNOME Shell stylesheets to apply the [Catppuccin](https://catppuccin.com) colorscheme. It generates a theme to be used with the [User Themes](https://extensions.gnome.org/extension/19/user-themes) shell extension.

## NixOS

The original maintainer packages this theme for Nix. **If** you run NixOS or its derivatives, **please** use [elisesouche/gnome-catppuccin/default.nix](https://github.com/elisesouche/gnome-catppuccin/blob/main/default.nix).

## Distro-agnostic usage

You need Python 3.13 with the libraries `libsass` and `diff_match_patch`.

### Clone this repository

```bash
git clone --recurse-submodules https://github.com/code-irisnk/catppuccin-gnome
cd gnome-catppuccin
```

### Installing dependencies

#### Option 1: Pipenv + Pipfile.lock

```bash
pip install pipenv
pipenv install --deploy
pipenv shell
```

#### Option 2: venv + requirements.txt

```bash
python3.13 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### Build:

```bash
./build.py
```

The theme is built in `./_build/theme`.

### Installing the theme

You can simply copy the contents of `./_build/theme` or symlink them to a folder in `~/.themes/` like `~/.themes/catppuccin-gnome` (or some other name). Then you can apply the theme like any regular GNOME shell theme!
