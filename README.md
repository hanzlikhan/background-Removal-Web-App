# Background removal 

A Streamlit application that allows users to upload images and automatically remove background within them using the Faster MODNET model with necessary libraries.

## Features

- **Upload Image:** Users can upload images in PNG, JPG, or JPEG formats.
- **Real-Time backgorund rmoving:** Remove background exactly of any abject.
- **Visual Display:** Presents images with bounding boxes using Matplotlib for clear visualization.

## How It Works
 ![Ui image](Ui.png)
1. **Upload Image:** User uploads an image.
2.  ![Input Image](input.png)
3. **Preprocess Image:** Image is preprocessed to the required format.
4. **Make Prediction:** Removing background from the images.
5.  ![output](output.png)
6. **Display Results:** After removing background , you can download the image.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
