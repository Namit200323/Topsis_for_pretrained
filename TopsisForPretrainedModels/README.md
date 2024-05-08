# Performance Evaluation of Pretrained Models for Text Summarization Using TOPSIS

This project investigates the effectiveness of various pretrained models for text summarization tasks, employing the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) multi-criteria decision-making method for comprehensive evaluation.

## Abstract

Automatic text summarization has gained significant traction in recent years, finding applications in various domains like news, research articles, and social media. Effective summarization requires accurate extraction of key information and concise presentation while preserving the original text's essence. Evaluating the performance of different summarization models poses a complex challenge due to the subjective nature of text quality and the need to consider various evaluation metrics.

This project tackles this challenge by leveraging TOPSIS, a method that helps identify the optimal solution from a set of alternatives based on their proximity to an ideal solution (maximizing positive criteria) and distance from a negative ideal solution (minimizing negative criteria).

## Methodology

### 1. Model Selection

Five pretrained models with diverse architectures and training datasets were chosen:

* `facebook/bart-large-cnn`
* `philschmid/bart-large-cnn-samsum`
* `Falconsai/text_summarization`
* `sshleifer/distilbart-cnn-12-6`
* `knkarthick/MEETING_SUMMARY`

### 2. Data Collection

A collection of text articles from various sources was prepared, ensuring diversity in topics and lengths.

### 3. Summarization and Evaluation

- Each model generated summaries for each article.
- ROUGE and BLEU scores were calculated to assess the summaries' readability and faithfulness to the original text.
- TOPSIS was employed to determine the optimal model based on:
    - ROUGE (higher is better): ROUGE-1, ROUGE-2, ROUGE-L, ROUGE-Lsum
    - BLEU (higher is better)
    - TOPSIS Score (higher is better)

## Results

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BLEU  | TopSIS Score | Rank |
|-----------------|---------|---------|---------|-----------|-------|----------------|-------|
| facebook/bart-large-cnn | 0.2046 | 0.1439 | 0.1688 | 0.1841 | 0.0007 | 0.7457 | 2     |
| philschmid/bart-large-cnn-samsum | 0.3882 | 0.2500 | 0.2706 | 0.2470 | 0.0243 | 0.0000 | 5     |
| Falconsai/text_summarization | 0.4581 | 0.3277 | 0.3687 | 0.4022 | 0.0722 | 0.7049 | 2     |
| sshleifer/distilbart-cnn-12-6 | 0.4973 | 0.3497 | 0.4757 | 0.4757 | 0.0853 | 1.0000 | 1     |
| knkarthick/MEETING_SUMMARY | 0.3953 | 0.2588 | 0.3488 | 0.3721 | 0.0355 | 0.2904 | 3     |

The table represents the average scores across all texts.

## Analysis and Conclusion

- **sshleifer/distilbart-cnn-12-6** emerged as the top-performing model based on the TOPSIS score, indicating its effectiveness in balancing different evaluation criteria.
- **Falconsai/text_summarization** and **facebook/bart-large-cnn-samsum** followed closely, demonstrating robust performance.
- **philschmid/bart-large-cnn-samsum** showed the lowest overall performance.



## Further Work

Future work could explore:

- Applying TOPSIS with different weightings for different evaluation metrics.
- Investigating other multi-criteria decision-making methods.

