<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://www.gnome.org">Gnome</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
    <a href="https://github.com/code-irisnk/catppuccin-gnome/stargazers"><img src="https://img.shields.io/github/stars/code-irisnk/catppuccin-gnome?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/code-irisnk/catppuccin-gnome/issues"><img src="https://img.shields.io/github/issues/code-irisnk/catppuccin-gnome?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/code-irisnk/catppuccin-gnome/contributors"><img src="https://img.shields.io/github/contributors/code-irisnk/catppuccin-gnome?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
  <img src="assets/preview.webp"/>
</p>

## Previews

<details>
<summary>:sunflower: Latte</summary>
<img src="assets/latte.webp"/>
</details>
<details>
<summary>:potted_plant: Frappé</summary>
<img src="assets/frappe.webp"/>
</details>
<details>
<summary>:hibiscus: Macchiato</summary>
<img src="assets/macchiato.webp"/>
</details>
<details>
<summary>:herb: Mocha</summary>
<img src="assets/mocha.webp"/>
</details>

## Prerequisites

- [bash](https://www.gnu.org/software/bash/manual/bash.html)*
- [python](https://docs.python.org/3)>=3.13
- [pip](https://github.com/pypa/pip)*
- [pipx](https://github.com/pypa/pipx)*
- [gnome](https://www.gnome.org/)>=50
- [user-themes](https://extensions.gnome.org/extension/19/user-themes/)*

#### debian
`sudo su - && apt update && apt install python3-full python3-pip`

#### fedora
`sudo dnf install python3-pip`

#### arch
`sudo pacman -Sy python python-pip python-libsass python-diff-match-patch`

#### void
`sudo xbps-install -S python3 python3-pip`

## Usage

1. Clone the repo:  
   `export TMP=$(mktemp -d) && git clone --recurse-submodules -j2 https://github.com/code-irisnk/gnome-catppuccin.git "$TMP" && cd "$TMP"`
2. Prepare environment:  
   `pipenv lock && pipenv install --deploy && pipenv shell`
3. Pick a flavour and run the script:  
   `./build.py -t mocha`  
   _^ theme can be found in "~/.themes/"_
4. Select the theme in the extension.
5. We're done! Be happy! yay!

## 💝 Thanks to

- [Élise Souche](https://github.com/elisesouche)
- [Lia Nkrichronos](https://github.com/liavnk)

&nbsp;

<p align="center">
 <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
 Copyright &copy; 2025-present<br><a href="https://irisnk.me/" target="_blank">Iris Nkrichronos</a>, Élise Souche and contributors</a>
</p>

<p align="center">
 <a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
