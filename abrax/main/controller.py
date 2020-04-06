from flask import Blueprint, render_template, redirect, flash

main = Blueprint(
    name='main',
    import_name=__name__,
    template_folder='templates',
    url_prefix='/'
)

@main.route('/')
def index():
    flash('Welcome to Abrax.Ka.Gallery','success')
    return render_template('index.html')

@main.route("/upload", methods=["POST"])
def upload():
    pass

@main.route('/upload/<filename>')
def send_image(filename):
    pass

@main.route('/gallery')
def get_gallery():
    try:
        images_source = [
            "https://source.unsplash.com/pWkk7iiCoDM/400x300",
            "https://source.unsplash.com/aob0ukAYfuI/400x300",
            "https://source.unsplash.com/EUfxH-pze7s/400x300",
            "https://source.unsplash.com/M185_qYH8vg/400x300",
            "https://source.unsplash.com/sesveuG_rNo/400x300",
            "https://source.unsplash.com/AvhMzHwiE_0/400x300",
            "https://source.unsplash.com/2gYsZUmockw/400x300",
            "https://source.unsplash.com/EMSDtjVHdQ8/400x300",
            "https://source.unsplash.com/8mUEy0ABdNE/400x300",
            "https://source.unsplash.com/G9Rfc1qccH4/400x300",
            "https://source.unsplash.com/aJeH0KcFkuc/400x300",
            "https://source.unsplash.com/p2TQ-3Bh3Oo/400x300",
        ]
        # images_source = None
        if len(images_source):
            flash('{} images in the gallery'.format(len(images_source)),'success')
            return render_template('display_gallery.html',images=images_source)
    except Exception as e:
        flash(e,'danger')
        return render_template('display_gallery.html',images=images_source)

@main.route('/gallery/<filename>')
def delete_image(filename):
    pass