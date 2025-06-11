# DeepLabCut-Kinovea

This project integrates motion tracking data from Kinovea (Excel-based coordinate exports) with [DeepLabCut](https://www.deeplabcut.org/) for biomechanical video analysis and deep learning-based pose estimation.

It is divided into two main components:

- `kinovea/`: Parses marker data from Kinovea `.xlsx` files.
- `deeplabcut/`: Handles DeepLabCut project training, testing, and video analysis.

---

## Project Structure
```
DeepLabCut-Kinovea/
├── deeplabcut/
│ ├── config.py
│ ├── main.py
│ ├── train.py
│ ├── test.py
│ └── utils.py
├── kinovea/
│ ├── main.py
│ ├── extractor.py
│ ├── utils.py
│ └── Data/
├── requirements.txt
└── README.md
```

---

## DeepLabCut Module

### Goal
Train, evaluate, and apply a deep neural network for animal/human pose estimation on videos using the DeepLabCut framework.

### Features

- Automatically locates `.mp4` videos from a specified folder.
- Trains a DeepLabCut model with configurable parameters.
- Analyzes videos to produce:
  - CSV files of predicted keypoints.
  - Labeled videos with overlayed keypoints.
  - Trajectory plots for visual validation.
  - Frame extraction for outlier correction.
- Modular design: training and testing steps can be toggled separately.
- Easy reconfiguration through `config.py`.

### Workflow

1. Define your project settings in `config.py`.
2. Run `main.py` to execute the pipeline.
3. Review outputs in the corresponding DeepLabCut project folder.

### Output

- A new project folder: `PROJECT_NAME-USER_NAME-DATE/`
- Inside it:
  - `config.yaml`: DeepLabCut project configuration
  - `labeled-data/`: Extracted frames for labeling
  - `training-datasets/`, `dlc-models/`: For training
  - Analysis results (`.csv`, `.h5`, `.mp4`, plots)

### Customization

All key parameters (project name, user, date, directories, whether to train/test) are configurable in `deeplabcut/config.py`:

```python
PROJECT_NAME = 'project-name'
USER_NAME = 'user-name'
DATE = 'YYYY-MM-DD'
WORKING_DIR = './working-directory'
VIDEO_FOLDER = 'video-folder'
DO_TRAIN = True
DO_TEST = True
```
## Kinovea Module

### Goal
Extract all marker blocks from `.xlsx` files exported by Kinovea, regardless of how many markers or their names.

### Features

- Parses all markers with `X`, `Y`, and `Time` columns dynamically.
- Merges marker blocks per file on `Time`.
- Adds optional metadata from filenames.
- Outputs a single `.csv` file for analysis or ML workflows.

# Clone this repository
```
git clone https://github.com/itziar-mengual/DeepLabCut-Kinovea.git
cd DeepLabCut-Kinovea
```
# Install dependencies
```
pip install -r requirements.txt
```

# Author
Itziar Mengual, 2025
