# organoid_size_measurement
A little project to create a script that can take in a brightfield image of organoids, and then return an (average) size of the organoids.

### 16 July 2024
I have a lot I still need to figure out:
  - I'm encountering an issue where in images with a lighter background, the organoids in the image don't get contoured.
  - Image segmentation using TensorFlow?
  - Figuring out how to output size, or average size of organoids
