# thought-analysis
The "cool" repo where I analyze all the blog posts I have written

### What is it?
I have tried to actually analyze the blog posts I have written in medium. The analysis is done using word2vec model (a type of word embedding).  
The embeddings for each and every word is calculated. The default dimension for each word vector is 300.  
So, I have tried using **PCA** to actually reduce the vectors to 2d and 3d space accordingly and then the vectors are visualized.  

The dataset for the analysis is done using my another "side-kick" project:  
https://github.com/NISH1001/medium-crawler

This crawling project gained its own repo while doing the extraction part for this analysis project.


### Tools
I have used: 
- scikit-learn
- numpy
- gensim
- matplotlib
