# IQSPred-PLM: An Interpretable Quorum Sensing Peptides Prediction Model Based on Protein Language Model

Quorum sensing regulates cooperative behaviors in bacteria through the accumulation and detection of signaling molecules. This process plays a crucial role in various biological functions, including biofilm formation, antibiotic production, regulation of virulence factors, and immune modulation.Within this framework, quorum sensing peptides (QSPs) serve as essential signaling molecules that mediate bacterial communication both within and between species, making them critical to understanding quorum sensing and its regulatory functions. Here, we propose IQSPred-PLM, a robust and interpretable deep learning model for accurate QSP prediction.

![图形摘要2](https://github.com/user-attachments/assets/1d67d778-d009-4f31-8687-768a5f50fa12)

IQSPred-PLM relies on a large-scale pre-trained protein language models: ESM-2. For detailed guidance on generating protein embedding representations, please refer to the official documentation available at the following websites:

- ESM-2:https://github.com/facebookresearch/esm

## Package requirement
```
pytorch==2.1.0  
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
```

## Test on the model

### 1. Prepare Test Data and Labels
- Before running the testing script:

Ensure your test data and corresponding labels are ready and match the required input format for the model. You can set them up in the `getdata.py` script.

### 2. Download the Model Weights
The model weights are not included in this repository. Please download the weights from the following link and place them in the specified directory:
- [Download Model Weights](#) *(replace `#` with the actual URL)*

After downloading, place the weights in the `weights/` directory or update the path in the script accordingly.

### 3. Run the Test Script
To test the model, run the following command:
```bash
python test.py


