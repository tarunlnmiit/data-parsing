from PIL import Image, ImageFilter

image = Image.open('../../Pictures/img3.png')
blurryimage = image.filter(ImageFilter.GaussianBlur)
blurryimage.save('../../Pictures/blur_img.png')
blurryimage.show()