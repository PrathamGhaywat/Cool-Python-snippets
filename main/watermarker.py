from PIL import Image #pip install pillow

def add_watermark(image_path, watermark_path, output_path):
    # Open the original image
    base_image = Image.open(image_path).convert("RGBA")

    # Open the watermark image (must be RGBA)
    watermark = Image.open(watermark_path).convert("RGBA")

    # Ensure the watermark image is the same size as the original image
    if watermark.size != base_image.size:
        watermark = watermark.resize(base_image.size)

    # Create a new, empty image with the same size and 'RGBA' format as the original image
    combined = Image.new('RGBA', base_image.size)

    # Paste the original image onto the new image
    combined.paste(base_image, (0, 0))

    # Paste the watermark image onto the new image, using the watermark image itself as the mask
    combined.paste(watermark, (0, 0), watermark)

    # Save the result
    combined.save(output_path)
#usage: 1.image 2.watermark 3.output path
add_watermark("", "", "")

#IMPORTANT!: Please note that the opacity of the watermark must be set by yourself, since the code above does not do that!
