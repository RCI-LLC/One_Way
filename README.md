# One-Way ATV Repair — Website (HTML + CSS + Python)

A simple 4-page website for One-Way ATV Repair, open since 2025.
All files sit in one flat folder — no subfolders.

## Files
```
index.html      # Home page
about.html      # About page
photos.html     # Photo gallery page
contact.html    # Contact page (with a working form)
style.css       # Shared stylesheet (monochrome/grayscale palette)
app.py          # Python (Flask) server
```

## Setup

1. Make sure you have Python 3.8+ installed.
2. Install Flask:
   ```
   pip install flask
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser to:
   ```
   http://127.0.0.1:5000
   ```

## Notes

- These are plain `.html` files (no template syntax), so they'll also look
  correct if you double-click and open them directly in a browser — the
  contact form just won't submit anywhere without the Python server running.
- **Photos**: drop image files into this same folder (e.g. `photo1.jpg`) and
  replace the placeholder `<div class="placeholder-photo">` tiles in
  `photos.html` with `<img src="photo1.jpg">` tags.
- **Contact form**: submissions are printed to your terminal when the Flask
  server is running. Extend the `submit()` function in `app.py` to save them
  to a file, a database, or send an email instead.
- **Colors**: all color values are CSS variables at the top of `style.css`
  under `:root` — change them there to restyle the whole site at once.
