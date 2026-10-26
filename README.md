# Duru Birinci · Fantage Town Portfolio

My portfolio as a little Fantage town. Walk the avatar around Downtown, Uptown, Fantage School and My Room, and click buildings to open my projects, experience, skills and contact info. A plain one-page resume sits below the game for anyone who wants to skip it.

## Run it

It is a static site with no build step. Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## Layout

- `index.html` is the site.
- `assets/` holds the scene backgrounds, the toolbar, the avatar and the nav icon.
- `src/index.template.html` is the same page with `{{name}}` image placeholders. `src/build_single_file.py` turns it into one self-contained file in `dist/`.

## Contact form

The Mail pop-up sends messages through [Web3Forms](https://web3forms.com). The access key in the page is a public key, so it is safe in client code. If a send fails, the form offers a mailto link instead.

## Credits

This is a fan tribute to Fantage. The Downtown art is by trixie-in-pastel on DeviantArt. The other scenes and the toolbar are screenshots from the Fantage Wiki, and the avatar was made on Fantage Archive. Fantage art and names belong to their original owners.
