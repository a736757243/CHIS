# CHIS
A new Character-level Hybrid-granularity Identifier Splitting approach

First, you need to use the code in BPE.txt in the Pre-Process file to obtain the morphemes in the training set.

Second, you need to use BMES.py in the Pre-Process file to label the identifiers in the training set using the BMES sequence labeling method.

Thirdly, you need to input the labeled identifiers into the BERT-CRF network, the code for the step is in the BERT-CRF file. Specially, we do not upload the pre-training model of BERT base here because it is too large, you need to download the pre-training model of BERT base by yourself.

Finally, the BERT-CRF network will output the first round of splitting results, and you need to use all the first round of splitting results for the post-processing component. the Post-Process file contains Merge.py and Split.py, you need to execute Merge.py, Split.py, Merge.py respectively to get the final results.
