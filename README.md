## mil-impozitionezi

Basic saddle-stitch impositioning that just works(TM)

Setup:
```
git clone git@github.com:trupples/mil-impozitionezi.git
cd mil-impozitionezi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Usage:
```
source .venv/bin/activate
python3 mil-impozitionezi.py INPUT.pdf OUTPUT.pdf
```

Feature(s):
- Imposition bleed-less H x W pages into H x 2W signatures

TODO:
- Imposition pages with bleed (H+t+b x W+l+r) into H+t+b x 2W+l+r signatures, cutting out middle bleed
- Add global margin
- Resize pages (for global margin + fit inside A4, for example)

Motivation: The [TUCN](https://utcluj.ro) typography refuses to imposition booklets and demand that clients do the impositioning themselves. This, of course, is a #%!& show and has given both me and fellow students many headaches.

