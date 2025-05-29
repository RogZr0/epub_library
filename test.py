from ebooklib import epub,ITEM_IMAGE,ITEM_COVER

book = epub.read_epub("books/48 Laws of Power.epub")

cover_image = None
cover_image_name = None

for item in book.get_items():
    print(item)
    if item.get_type() == "cover":
        print('TRUE')

# Iterate through all items to find the cover image
for item in book.get_items():
    # Cover image is usually of type IMAGE
    if item.get_type() == ITEM_COVER:
        # Heuristic: check if 'cover' is in the file name or id
        if 'cover' in item.file_name.lower() or 'cover' in item.id.lower():
            cover_image = item.get_content()
            cover_image_name = item.file_name
            break

# If cover image found, save it to a file
if cover_image:
    # Determine extension from file name
    ext = cover_image_name.split('.')[-1]
    with open(f'cover_image.{ext}', 'wb') as f:
        f.write(cover_image)
    print(f'Cover image saved as cover_image.{ext}')
else:
    print('Cover image not found')
