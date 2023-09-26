import pandas as pd
import json
import functools
import seaborn as sns
import datetime
import math
import numpy as np
import preprocessor as p


def preprocess_data(data_path, max_sequence_length):
    """
    Preprocess original jsonl data. Sorts tweets in chronological order, joins tweets in a thread into a single block of string. Finally truncates each string to max_sequence_length.

    Args:
        path (str): path to data. 
        max_sequence_length (int): maximum sequence length used for longformer.

    Returns:
        list: list of strings, where each string represents a twitter thread.
    """

    # --------------- LOAD DATA AND LABELS-----------------
    data : pd.DataFrame = pd.read_json(data_path, lines=True)

    # --------------- SORT BY TIME -------------------
    data_sorted = data.apply(fn_sortTweetsChronological, axis=1)
    data_sorted = data_sorted.where(pd.notnull(data_sorted), None)

    # --------------- GET CORRESPONDING SOURCE TWEET ID ------------------
    sourceIds = list(map(lambda x: x.get("id_str"), data_sorted.iloc[:,0]))

    # --------------- GET TEXT FROM TWITTER DICT AND CONCATENATE --------------------
    text_df = data_sorted.apply(fn_extractTxt, axis=1)
    text_df_concatenate = pd.DataFrame(text_df.apply(fn_concatTweet, axis=1), columns=["text"])

    # --------------- CLEAN AND TRUNCATE COMBINED TWEET -------------------
    text_df_concatenate_cleaned = pd.DataFrame(clean_thread(text_df_concatenate.text), columns=["text"])
    text_concatenate_cleaned_final = truncate(text_df_concatenate_cleaned.text, max_sequence_length)

    return text_concatenate_cleaned_final, sourceIds


def convert_label(label):
    if label == "rumour":
        return 1
    elif label == "non-rumour":
        return 0
    else:
        raise Exception("label classes must be 'rumour' or 'non-rumour'")


def get_dataset_and_labels(data_path, label_path, max_sequence_length):

    with open(label_path) as f:
        labels = json.load(f)

    text_concatenate_cleaned_final, sourceIds = preprocess_data(data_path, max_sequence_length)
    corresponding_labels = [labels[id] for id in sourceIds]
    numeric_labels = [convert_label(label) for label in corresponding_labels]

    return text_concatenate_cleaned_final, numeric_labels


# ----------------- HELPER FUNCTIONS -----------------------

def get_labels(label_path):
    with open(label_path) as f:
        labels = json.load(f)
    corresponding_labels = [labels[id] for id in sourceIds]
    numeric_labels = [convert_label(label) for label in corresponding_labels]

    return numeric_labels


def fn_extractTxt(series: pd.Series):
    texts = []
    for dictionary in series:
        if dictionary is not None:
            texts.append(dictionary.get("text"))
        else:
            texts.append(None)
    return pd.Series(texts)


def fn_sortTweetsChronological(series: pd.Series):
    time_created_list = []
    series_len = len(series)

    for dictionary in series:
        if dictionary is not None:
            time_created_str = dictionary.get("created_at")
            time_created = datetime.datetime.strftime(datetime.datetime.strptime(time_created_str,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
            time_created_list.append(time_created)
    
    ind_time_created_list_sorted = sorted(range(len(time_created_list)), key=lambda k: time_created_list[k])
    new_series = series[ind_time_created_list_sorted]
    return new_series


def fn_concatTweet(series: pd.Series):
    filtered_series = filter(None,series)
    concatTweet = ''.join(filtered_series)
    return concatTweet


def clean_thread(series: pd.Series):
    p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER, p.OPT.MENTION)
    cleaned_thread_list = []
    for thread in series:

        # Clean URL, EMOJI, SMILEY, NUMBER, MENTION
        cleaned_thread_first = p.clean(thread)
        cleaned_thread_list.append(cleaned_thread_first)
    
    return pd.Series(cleaned_thread_list)


def truncate(series: pd.Series, max_sequence_length=512):
    truncated_thread_list = []
    for thread in series:
        if len(thread) > max_sequence_length:
            truncated_thread_list.append(thread[:int(max_sequence_length/2)] + thread[:-int(max_sequence_length/2)])
        else:
            truncated_thread_list.append(thread)
    
    return truncated_thread_list