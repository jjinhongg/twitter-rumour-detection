# Rumour Detection and COVID-19 Rumour Analysis

## Project Overview

This repository presents a research project conducted by Jin Hong Yong as part of an academic study. The project focuses on the detection of rumors and the analysis of COVID-19-related rumors using natural language processing techniques and state-of-the-art transformer models. The primary goal is to identify and analyze rumors on social media platforms, particularly Twitter, and gain insights into the content, sentiment, and characteristics of these rumors.

## Objectives

The key objectives of this project include:

- Developing a binary content-based classification approach for rumor detection.
- Utilizing transformer models, including Longformer, BERT, and RoBERTa, to detect rumors.
- Preprocessing Twitter data, including the concatenation of tweets and reply tweets.
- Conducting topic analysis, hashtag analysis, and sentiment analysis to gain insights into rumor content.
- Analyzing and comparing the results of different transformer models and hyperparameters.

## Methodology

The project's methodology involves:

### Data Preprocessing

- Cleaning the data by removing redundant information such as URLs, emojis, mentions, and numbers-only tweets.
- Ordering tweets in chronological order to capture the progression of discussions.
- Truncating tweet sequences to a specified maximum length.

### Transformer Models

- Leveraging transformer architectures with self-attention mechanisms for capturing structural information within tweet threads.

#### Transformer Models Used

1. **BERT (Bidirectional Encoder Representations from Transformers)**
2. **RoBERTa (Robustly Optimized BERT Approach)**
3. **Longformer (Optimized for Processing Long Documents)**

### Experiments and Results

- Evaluating the performance of transformer models by varying the maximum sequence length.
- Analyzing the F1 score, precision, and recall for different model configurations.
- Conducting topic analysis to identify underlying topics in rumor and non-rumor threads.
- Analyzing hashtags to understand their effectiveness in rumor detection.
- Performing sentiment analysis to determine the emotional tone of rumors.

## Findings and Analysis

The project's findings and analysis include:

- The superior performance of RoBERTa over BERT in rumor detection.
- The limited effectiveness of longer sequences (Longformer) in improving rumor detection accuracy.
- Insights into the content of rumors through topic analysis.
- Limited effectiveness of hashtags in distinguishing rumors from non-rumors.
- Differences in sentiment distribution between rumors and non-rumors, with rumors tending to convey more negative sentiments.

## Conclusion

In conclusion, this project highlights the importance of rumor detection in the age of social media and disinformation. It demonstrates the potential of transformer models like RoBERTa in accurately identifying rumors. The analysis of topics, hashtags, and sentiments provides valuable insights into the characteristics of rumors.

## Discussion

The project also discusses the limitations of the methods used, such as the inability of Longformer to significantly improve rumor detection. Further research may explore alternative approaches to enhance rumor detection accuracy.

## References

The following academic references were used in this project:

- [Hunt Allcott and Matthew Gentzkow. 2017. Social media and fake news in the 2016 election.](#)
- [Iz Beltagy, Matthew E Peters, and Arman Cohan. 2020. Longformer: The long-document transformer.](#)
- [Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. Bert: Pre-training of deep bidirectional transformers for language understanding.](#)
- [Richard Gunther, Paul A Beck, and Erik C Nisbet. 2018. Fake news did have a significant impact on the vote in the 2016 election: Original full-length version with methodological appendix.](#)
- [Ling Min Serena Khoo, Hai Leong Chieu, Zhong Qian, and Jing Jiang. 2020. Interpretable rumor detection in microblogs by attending to user interactions.](#)
- [Sumeet Kumar and Kathleen M Carley. 2019. Tree lstms with convolution units to predict stance and rumor veracity in social media conversations.](#)
- [Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A robustly optimized bert pretraining approach.](#)
- [Jing Ma, Wei Gao, and Kam-Fai Wong. 2018. Rumor detection on twitter with tree-structured recursive neural networks.](#)
- [Kenneth Rapoza. 2017. Can ‘fake news’ impact the stock market? by Forbes.](#)
- [Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need.](#)

For detailed information and findings, please refer to the full academic report.
