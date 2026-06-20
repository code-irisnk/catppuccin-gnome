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

- [python](https://docs.python.org/3)>=3.13
- [pip](https://github.com/pypa/pip)*
- [pipx](https://github.com/pypa/pipx)*
- [gnome](https://www.gnome.org/)>=50
- [user-themes](https://extensions.gnome.org/extension/19/user-themes/)*

## Usage

1. Clone the repo:  

   ```shell
   git clone --recurse-submodules https://github.com/code-irisnk/gnome-catppuccin.git && cd "gnome-catppuccin"
   ```

2. Prepare your Python environment:  

   ```shell
   pipx install pipenv && pipenv lock && pipenv install --deploy && pipenv shell
   ```

3. Pick a flavour and run the script:  

   ```shell
   ./build.py -t mocha
   ```
  
   This will place the theme in `~/.themes/`
4. Select and apply the shell theme.

## :gift_heart: Thanks to

- [Élise Souche](https://github.com/elisesouche)
- [Lia Nkrichronos](https://github.com/liavnk)

&nbsp;

<p align="center">
 <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
 Copyright &copy; 2025-present<br>Élise Souche, Iris Nkrichronos, and contributors</a>
</p>

<p align="center">
 <a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=1e1e2e&colorA=1e1e2e&colorB=cba6f7"/></a>
</p>
