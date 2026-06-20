#!/usr/bin/env python3

import sass
import shutil, os, sys
from pathlib import Path
from diff_match_patch import diff_match_patch

FLAVOUR = ""

BUILD_PATH = "./_build"
THEMESRC_PATH = f"{BUILD_PATH}/themesrc"

OUT_PATH = f"{Path.home()}/.themes/catppuccin-"
OUT_GNOME_PATH = f"{OUT_PATH}/gnome-shell"
CSS_PATH = f"{OUT_GNOME_PATH}/gnome-shell.css"


def check_args():
  if sys.argv[1] != "-t":
    print("invalid argument")
    exit(0)
  if len(sys.argv) != 3:
    print("you need to specify a flavour")
    exit(0)
  if sys.argv[2] not in ("latte", "frappe", "macchiato", "mocha"):
    print("choose between latte, frappe, macchiato and mocha.")
    exit(0)
  global FLAVOUR, OUT_PATH, OUT_GNOME_PATH, CSS_PATH
  FLAVOUR = sys.argv[2]
  OUT_PATH = f"{Path.home()}/.themes/catppuccin-{FLAVOUR}"
  OUT_GNOME_PATH = f"{OUT_PATH}/gnome-shell"
  CSS_PATH = f"{OUT_GNOME_PATH}/gnome-shell.css"
  print(f"Selected flavour: {FLAVOUR}")


def mk_patch(file: str):
  dmp = diff_match_patch()
  with open(f"./gnome-shell/data/theme/gnome-shell-sass/_{file}.scss", "r") as old:
    with open(f"./{file}.scss", "r") as new:
      old = old.read()
      new = new.read()
      patches = dmp.patch_make(old, new)
      diff = dmp.patch_toText(patches)
      with open("{file}.scss.patch", "w") as p:
        p.write(diff)


def mk_all_patches():
  mk_patch("colors")
  mk_patch("default-colors")


def clean():
  try:
    shutil.rmtree(f"{BUILD_PATH}")
  except:
    pass


def mk_theme_dir():
  print("Creating output build directory...")
  clean()
  src_path = "./gnome-shell/data/theme/"
  shutil.copytree(src_path, THEMESRC_PATH)
  global OUT_PATH, OUT_GNOME_PATH
  os.makedirs(f"{OUT_PATH}", exist_ok=True)
  os.makedirs(f"{OUT_GNOME_PATH}", exist_ok=True)


def apply_patch(file: str):
  print(f"Patching {file}.scss...")
  dmp = diff_match_patch()
  colors_path = f"{THEMESRC_PATH}/gnome-shell-sass/_{file}.scss"
  colors_patch = f"./{file}.scss.patch"
  with open(colors_patch, "r") as p:
    p = p.read()
    patches = dmp.patch_fromText(p)
    with open(colors_path, "r") as cols:
      cols_t = cols.read()
      cols_t, _ = dmp.patch_apply(patches, cols_t)
    with open(colors_path, "w") as cols:
      cols.write(cols_t)


def edit_palette():
  print("Setting custom palette...")
  palette_path = f"{THEMESRC_PATH}/gnome-shell-sass/_palette.scss"
  palette_src = f"./palette.scss"
  shutil.copy(palette_src, palette_path)
  global FLAVOUR
  with open(palette_path, "a") as file:
    file.write(f"""
      $blue_1: ${FLAVOUR}-sky;
      $blue_2: ${FLAVOUR}-sapphire;
      $blue_3: ${FLAVOUR}-sapphire;
      $blue_4: ${FLAVOUR}-blue;
      $blue_5: ${FLAVOUR}-blue;
      $green_1: ${FLAVOUR}-teal;
      $green_2: ${FLAVOUR}-green;
      $green_3: ${FLAVOUR}-green;
      $green_4: ${FLAVOUR}-green;
      $green_5: ${FLAVOUR}-green;
      $yellow_1: ${FLAVOUR}-yellow;
      $yellow_2: ${FLAVOUR}-yellow;
      $yellow_3: ${FLAVOUR}-yellow;
      $yellow_4: ${FLAVOUR}-yellow;
      $yellow_5: ${FLAVOUR}-peach;
      $orange_1: ${FLAVOUR}-peach;
      $orange_2: ${FLAVOUR}-peach;
      $orange_3: ${FLAVOUR}-peach;
      $orange_4: ${FLAVOUR}-peach;
      $orange_5: ${FLAVOUR}-peach;
      $red_1: ${FLAVOUR}-red;
      $red_2: ${FLAVOUR}-red;
      $red_3: ${FLAVOUR}-red;
      $red_4: ${FLAVOUR}-red;
      $red_5: ${FLAVOUR}-red;
      $purple_1: ${FLAVOUR}-mauve;
      $purple_2: ${FLAVOUR}-mauve;
      $purple_3: ${FLAVOUR}-mauve;
      $purple_4: ${FLAVOUR}-mauve;
      $purple_5: ${FLAVOUR}-mauve;
      $brown_1: ${FLAVOUR}-maroon;
      $brown_3: ${FLAVOUR}-maroon;
      $brown_4: ${FLAVOUR}-maroon;
      $brown_5: ${FLAVOUR}-maroon;
      $light_1: ${FLAVOUR}-text;
      $light_2: ${FLAVOUR}-subtext1;
      $light_3: ${FLAVOUR}-subtext0;
      $light_4: ${FLAVOUR}-overlay2;
      $light_5: ${FLAVOUR}-overlay1;
      $dark_1: ${FLAVOUR}-surface2;
      $dark_2: ${FLAVOUR}-surface1;
      $dark_3: ${FLAVOUR}-surface0;
      $dark_4: ${FLAVOUR}-base;
      $dark_5: ${FLAVOUR}-crust;
    """)
  apply_patch("default-colors")
  apply_patch("colors")


def compile():
  css = sass.compile(filename=f"{THEMESRC_PATH}/gnome-shell-dark.scss")
  with open(CSS_PATH, "w") as output_css:
    output_css.write(css)


def build():
  print("Building CSS and finalizing theme build...")
  compile()
  global OUT_PATH
  shutil.copy("./index.theme", f"{OUT_PATH}/index.theme")


def main():
  check_args()
  mk_theme_dir()
  edit_palette()
  build()
  print("All done!")


if __name__ == "__main__":
  main()
