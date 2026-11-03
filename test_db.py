from database import get_crop

crop = get_crop("Maize")

if crop:
    print("Crop found! ✅")
    print("Name:", crop["crop_name"])
    print("Description:", crop["description"])
else:
    print("Crop not found ❌")