from pathlib import Path
import base64

html_path = Path('/home/ubuntu/sonic-canvas-full.html')
html = html_path.read_text()
assets = {
    '/manus-storage/sonic-hero_90c73dc0.jpg': '/home/ubuntu/webdev-static-assets/sonic-hero.jpg',
    '/manus-storage/sonic-gallery-01_717d4c4d.jpg': '/home/ubuntu/webdev-static-assets/sonic-gallery-01.jpg',
    '/manus-storage/sonic-gallery-02_529e3679.jpg': '/home/ubuntu/webdev-static-assets/sonic-gallery-02.jpg',
    '/manus-storage/sonic-gallery-03_9a451310.jpg': '/home/ubuntu/webdev-static-assets/sonic-gallery-03.jpg',
}
for old_path, asset_path in assets.items():
    encoded = base64.b64encode(Path(asset_path).read_bytes()).decode('ascii')
    html = html.replace(old_path, f'data:image/jpeg;base64,{encoded}')
html_path.write_text(html)
print(f'Wrote {html_path} ({html_path.stat().st_size:,} bytes)')
