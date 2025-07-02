import yaml
import os

def create_data_yaml(dataset_root):
    """
    Creates YOLOv5-compatible data.yaml file based on the dataset structure.
    
    Expects:
    - classes.txt in dataset_root
    - train/images/, validation/images/ folders in dataset_root
    """
    dataset_root = os.path.abspath(dataset_root)

    classes_path = os.path.join(dataset_root, 'classes.txt')
    train_images = os.path.join(dataset_root, 'train', 'images')
    val_images = os.path.join(dataset_root, 'validation', 'images')
    data_yaml_path = os.path.join(dataset_root, 'data.yaml')

    # ✅ Check if required files exist
    if not os.path.exists(classes_path):
        print(f'❌ classes.txt not found at: {classes_path}')
        return
    if not os.path.exists(train_images):
        print(f'❌ train/images/ folder not found at: {train_images}')
        return
    if not os.path.exists(val_images):
        print(f'❌ validation/images/ folder not found at: {val_images}')
        return

    # ✅ Read class names
    with open(classes_path, 'r') as f:
        class_names = [line.strip() for line in f if line.strip()]

    # ✅ Create data.yaml dictionary
    data = {
        'train': train_images.replace("\\", "/"),
        'val': val_images.replace("\\", "/"),
        'nc': len(class_names),
        'names': class_names
    }

    # ✅ Write to data.yaml
    with open(data_yaml_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)

    print(f'✅ data.yaml created at: {data_yaml_path}')


# ✅ Example usage:
# Assume you're running this script from inside your project directory:
# python generate_data_yaml.py
if __name__ == "__main__":
    create_data_yaml(dataset_root='dataset')

