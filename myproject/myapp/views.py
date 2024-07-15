import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'webp']

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

def home(request):
    return render(request, 'home.html')

def remback(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file and allowed_file(file.name):
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            input_path = fs.path(filename)
            rembg_img_name = os.path.splitext(filename)[0] + "_rembg.png"
            output_path = os.path.join(fs.location, rembg_img_name)
            remove_background(input_path, output_path)
            return render(request, 'home.html', {
                'org_img_name': fs.url(filename),
                'rembg_img_name': fs.url(rembg_img_name)
            })
    return render(request, 'home.html')

