import os
import sys
import librosa
import soundfile as sf
from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift, Shift

def load_wav(file_path):
    data, sample_rate = librosa.load(file_path, sr=None)
    return data, sample_rate

def save_wav(data, sample_rate, file_path):
    sf.write(file_path, data, sample_rate)


def main(input_dir, output_dir, augmentations):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            data, sample_rate = load_wav(input_path)
            augmented_data = augmentations(data)
            save_wav(augmented_data, sample_rate, output_path)
            print(f"Processed and saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_dir> <output_dir> <augmentation_type1> <augmentation_type2> ...")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    augmentation_types = sys.argv[3:]

    augmentations = Compose()

    for augmentation_type in augmentation_types:
        augmentation_type = augmentation_type.lower()
        if augmentation_type == "noise":
            augmentations.add(AddGaussianNoise(min_amplitude=0.001, max_amplitude=0.015))
        elif augmentation_type == "stretch":
            augmentations.add(TimeStretch(min_rate=0.8, max_rate=1.25))
        elif augmentation_type == "pitch":
            augmentations.add(PitchShift(min_semitones=-4, max_semitones=4))
        elif augmentation_type == "shift":
            augmentations.add(Shift(min_fraction=-0.5, max_fraction=0.5))
        else:
            print(f"Invalid augmentation type: {augmentation_type}. Available types: noise, stretch, pitch, shift")
            sys.exit(1)

    print(f"Using augmentations: {augmentations}")
    main(input_dir, output_dir, augmentations)
