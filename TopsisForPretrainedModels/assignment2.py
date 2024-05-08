import pandas as pd
from transformers import pipeline
from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer
from nltk.tokenize import word_tokenize
import nltk
from topsis import helper

nltk.download('punkt')


models = [
    "facebook/bart-large-cnn",
    "philschmid/bart-large-cnn-samsum",
    "Falconsai/text_summarization",
    "sshleifer/distilbart-cnn-12-6",
    "knkarthick/MEETING_SUMMARY",
]

main_df = pd.DataFrame(columns=["Text", 'Model', 'ROUGE-1', 'ROUGE-2', 'ROUGE-L', 'ROUGE-Lsum', 'BLEU', 'Topsis Score', 'Rank'])



summarizers = [pipeline("summarization", model=model) for model in models]

for i in range(1,4):

    text_filename = f"sports_article{i}.txt"
    summary_filename = f"summary{i}.csv"
    output_filename = f"output{i}.csv"

    with open(text_filename, "r") as f:
        text = f.read()

    rouge_scorer_instance = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)


    # Create an empty dataframe
    columns = ["Text",'Model', 'ROUGE-1', 'ROUGE-2', 'ROUGE-L', 'ROUGE-Lsum', 'BLEU']
    df = pd.DataFrame(columns=columns)

    # Loop through each model
    for model_name in models:
        # Initialize the summarization pipeline
        summarizer = pipeline("summarization", model=model_name)
        
        # Generate summary
        summary = summarizer(text, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)[0]['summary_text']

        # Calculate ROUGE scores
        rouge_scores = rouge_scorer_instance.score(summary, text)

        # Calculate BLEU score
        bleu_score = corpus_bleu([[text.split()]], [summary.split()])

        # Calculate METEOR score
        

        # Add values to the dataframe
        df = df._append({
            "Text":i,
            'Model': model_name,
            'ROUGE-1': rouge_scores['rouge1'].fmeasure,
            'ROUGE-2': rouge_scores['rouge2'].fmeasure,
            'ROUGE-L': rouge_scores['rougeL'].fmeasure,
            'ROUGE-Lsum': rouge_scores['rougeLsum'].fmeasure,
            'BLEU': bleu_score
        }, ignore_index=True)

    # Save the dataframe to CSV
    df.to_csv(summary_filename, index=False)

    helper(summary_filename,output_filename)

    processed_df = pd.read_csv(output_filename, header=None)
    processed_df.columns = ["Text",'Model', 'ROUGE-1', 'ROUGE-2', 'ROUGE-L', 'ROUGE-Lsum', 'BLEU', 'Topsis Score', 'Rank']
    processed_df_without_first_row = processed_df[1:]

# Append the sliced dataframe to main_df
    main_df = main_df._append(processed_df_without_first_row)

print(main_df)

model_rank_sums = main_df.groupby('Model')['Rank'].sum().sort_values(ascending=True)
best_model = model_rank_sums.index[0]

print(f"Best model based on sum of ranks: {best_model}")
main_df.to_csv("sports.csv")


