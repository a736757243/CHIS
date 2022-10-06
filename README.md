# Split
A new Character-level Hybrid-granularity Identifier Splitting approach.

First, you need to use the code in BPE.txt in the Pre-Process file to obtain the morphemes in the training set.

Second, you need to use BMES.py in the Pre-Process file to label the identifiers in the training set using the BMES sequence labeling method.

Thirdly, you need to input the labeled identifiers into the BERT-CRF network, the code for the step is in the BERT-CRF file. Specially, we do not upload the pre-training model of BERT base here because it is too large, you need to download the pre-training model of BERT base by yourself.

Finally, the BERT-CRF network will output the first round of splitting results, and you need to use all the first round of splitting results for the post-processing component. the Post-Process file contains Merge.py and Split.py, you need to execute Merge.py, Split.py, Merge.py respectively to get the final results.
# Expansion
A Deep Learning-Based Identifier Expansion Method.

Preprocess the dataset through dataprocess.py.
Train the model from NER and SIM files.
The files have detailed data processing steps.
After training the ner and sim models, you can predict the extended identifier through the predict_pro.py file.
# Datasets
We have uploaded the datasets used for this study to the datasets file, where BT11, Jhotdraw, Binkley, Lynx are the split study datasets. abbreviation_expansions_data is the expansion study dataset.
# Plug-in
The Plug-in file holds the plugin development source code. We only provide the plug-in development code, to use the plug-in, you need to train a deep learning model for the identifier splitting and extension of the domain you need by yourself following the steps above.
