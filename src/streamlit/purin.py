from src.model.trainer.baseline import Trainer
from typing import Any

import pandas
from janome.tokenizer import Tokenizer
from sklearn.model_selection import train_test_split

import streamlit
st = streamlit  # type: Any


def purin():
    x, y = load_dataset()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    trainer = Trainer(x_train, y_train, x_test, y_test, tokenize=tokenize)
    trainer.train()

    text = st.text_input('入力', 'ピカチュウとプリンとニャースとピッピかわいい')
    if text:
        score = round(trainer.predict([text])[0][1] * 100)
        st.progress(score)
        st.metric('ポケモン度', f'{score}%')
        if score >= 50:
            st.write('ポケモンです')
        else:
            st.write('ポケモンではありません')


def load_dataset():
    # TODO: データの置き場所を指定できるように
    df = df = pandas.read_csv('/app/data/purin-tsv.tsv', sep='\t', skiprows=1, names=('id', 'tweet_id', 'text', 'url', 'label', 'keyword'))
    df = df.dropna(subset=['label'])
    print('length: ', len(df))
    return df['text'].values, df['label'].values


t = Tokenizer()


def tokenize(text):
    return t.tokenize(text, wakati=True)
