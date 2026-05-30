import os
import random
import shutil

# Paths
image_dir = "train/images"
label_dir = "train/labels"

valid_image_dir = "valid/images"
valid_label_dir = "valid/labels"

test_image_dir = "test/images"
test_label_dir = "test/labels"

# Create folders if not exist
os.makedirs(valid_image_dir, exist_ok=True)
os.makedirs(valid_label_dir, exist_ok=True)
os.makedirs(test_image_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)

# Get all image files
images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Shuffle images
random.shuffle(images)

# Split percentages
total = len(images)

valid_count = int(total * 0.15)
test_count = int(total * 0.10)

valid_images = images[:valid_count]
test_images = images[valid_count:valid_count + test_count]

# Function to move files
def move_files(image_list, target_image_dir, target_label_dir):

    for image_file in image_list:

        base_name = os.path.splitext(image_file)[0]

        label_file = base_name + ".txt"

        # Source paths
        src_image = os.path.join(image_dir, image_file)
        src_label = os.path.join(label_dir, label_file)

        # Destination paths
        dst_image = os.path.join(target_image_dir, image_file)
        dst_label = os.path.join(target_label_dir, label_file)

        # Move image
        if os.path.exists(src_image):
            shutil.move(src_image, dst_image)

        # Move label
        if os.path.exists(src_label):
            shutil.move(src_label, dst_label)

# Move validation files
move_files(valid_images, valid_image_dir, valid_label_dir)

# Move test files
move_files(test_images, test_image_dir, test_label_dir)

print("Dataset split completed successfully!")