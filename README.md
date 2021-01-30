# cnn-infill-optimization
Recreation of "Determination of an infill well placement using a data-driven multi-modal convolutional neural network".

The repository contains python files to 
- Run open porous media (OPM) reservoir simulator for varying infill well locations : `data_collect.py`
- Training and Testing of neural network model (based on pytorch) to predict total oil production after 20 years given any infill well location : `Training/training.ipynb`, `Testing/testing.ipynb`
- Compare CNN production heat map with the reference production heat map (Ground truth) : `Reference/reference_comparison.ipynb`

### Production Heatmaps for Reference and CNN model
![image](Reference/cnn_results_1.JPG "Comparisons")