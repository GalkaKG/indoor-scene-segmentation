# Indoor Scene Segmentation and Room Style Classification

This repository contains work on **indoor scene segmentation** and **room style classification** using deep learning. The project is still a **work in progress** and requires further development and refinement.

## Project Structure

- **`notebooks/`**

  - The core work on segmentation is in **`01_Segmentation.ipynb`** and **`02_Segmentation.ipynb`**.
  - Data exploration and modeling for room style classification are in **`04_DataExploration.ipynb`** and **`05_StyleClassification.ipynb`**.

- **`models/`**

  - Contains trained models for both segmentation and room style classification.

- **`data/splits/`**

  - Contains the dataset splits for training, validation, and testing.
  - `annotations.csv` maps RGB images to their corresponding label/mask.

- **`scripts/`**
  - Contains a script to generate a mesh from an image.

## Dataset Information

### Scene Segmentation Dataset

The dataset for indoor scene segmentation is **SUNRGBD**, which can be downloaded from:  
🔗 **[SUNRGBD Dataset](https://rgbd.cs.princeton.edu/)**

- In the **Data and Annotation** section, download:
  - **SUNRGBD V1**
  - **SUNRGBDtoolbox**

The metadata and labels for the **37 classes** used in training were taken from:  
🔗 **[SUNRGBD Meta Data](https://github.com/ankurhanda/sunrgbd-meta-data/tree/master?tab=readme-ov-file)**

### Room Style Classification Dataset

The repository also includes a **scraped dataset** containing images of rooms with different styles and types. The corresponding exploration and model training are in **notebooks `04` and `05`**.

## Work in Progress

🚧 This project is **not yet finished** and still requires further improvements. 🚧  
Future work includes:

- Refining the segmentation model
- Improving room style classification
- Optimizing dataset processing
- **Experimenting with 2D image restructuring to 3D representations**

## Usage

To be added soon...

---

Stay tuned for updates! 🚀
