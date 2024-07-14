Audio augmentation utilizing the audiomentations module(https://github.com/iver56/audiomentations).

Alowe using command line inputs to process .WAV files. Four operations are provided:

- Gaussian Noise: Run the `AddGaussianNoise` operation to add Gaussian noise to the audio. The amplitude of the noise was randomly selected between `min_amplitude=0.001` and `max_amplitude=0.015`. This makes the audio sound slightly noisy, similar to the effect of recording in a noisy environment.

- Stretch: Using `TimeStretch` changes the time stretch rate of the audio. The drawing rate was randomly selected between `min_rate=0.8` and `max_rate=1.25`. This makes the audio play slower or faster, but does not change the pitch.

- Pitch: Use `PitchShift` to change the pitch of the audio. The pitch variations were randomly selected between `min_semitones=-4` and `max_semitones=4`. This causes the pitch of the audio to rise or fall, similar to the effect of using a pitch converter.

- Shift: Using `Shift` changes the time position of the audio. The time shift was randomly selected between `min_fraction=-0.5` and `max_fraction=0.5`. This moves parts of the audio forward or backward, similar to positional adjustments when editing audio.

User can specify the input and output directories, as well as the number of augmented files to generate for each input file. The output directory will be created if it does not exist.

Example usage:

    python_augments.py -i input_dir -o output_dir <noise> <stretch> <pitch> <shift>

This will process all.WAV files in the "input_directory" and generate 10 augmented files in the "output_directory".