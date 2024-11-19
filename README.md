### IQSPred-PLM: An Interpretable Quorum Sensing Peptides Prediction Model Based on Protein Language Model

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

You can test the model using the provided 'test.py'. Before running it, ensure that the test data and labels are prepared, and the weight files are downloaded.


