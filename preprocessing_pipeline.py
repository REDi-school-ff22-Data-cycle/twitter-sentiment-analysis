import re

contraction_patterns = [(r'won\'t', 'will not'), (r'can\'t', 'cannot'), (r'i\'m', 'i am'), (r'ain\'t', 'is not'),
                        (r'(\w+)\'ll', '\g<1> will'), (r'(\w+)n\'t', '\g<1> not'),
                        (r'(\w+)\'ve', '\g<1> have'), (r'(\w+)\'s', '\g<1> is'), (r'(\w+)\'re', '\g<1> are'),
                        (r'(\w+)\'d', '\g<1> would'), (r'&', 'and'), (r'dammit', 'damn it'), (r'dont', 'do not'),
                        (r'wont', 'will not')]


def removeUnicode(text):
    """ Removes unicode strings like "\u002c" and "x96" """
    text = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', text)
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    return text


def replaceURL(text):
    """ Replaces url address with "url" """
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'url', text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text


def replaceAtUser(text):
    """ Replaces "@user" with "atUser" """
    text = re.sub('@[^\s]+', 'atUser', text)
    return text


def removeHashtagInFrontOfWord(text):
    """ Removes hastag in front of a word """
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text


def removeNumbers(text):
    """ Removes integers """
    text = ''.join([i for i in text if not i.isdigit()])
    return text


def replaceMultiExclamationMark(text):
    """ Replaces repetitions of exlamation marks """
    text = re.sub(r"(\!)\1+", ' multiExclamation ', text)
    return text


def replaceMultiQuestionMark(text):
    """ Replaces repetitions of question marks """
    text = re.sub(r"(\?)\1+", ' multiQuestion ', text)
    return text


def replaceMultiStopMark(text):
    """ Replaces repetitions of stop marks """
    text = re.sub(r"(\.)\1+", ' multiStop ', text)
    return text


def replaceContraction(text):
    patterns = [(re.compile(regex), repl) for (regex, repl) in contraction_patterns]
    for (pattern, repl) in patterns:
        (text, count) = re.subn(pattern, repl, text)
    return text


def removeEmoticons(text):
    """ Removes emoticons from text """
    text = re.sub(
        ':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:',
        '', text)
    return text


# def preprocess_data(df):
#    df['tweets_preprocessed'] = df['message'].apply(lambda x: removeUnicode(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: replaceURL(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: replaceAtUser(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: removeHashtagInFrontOfWord(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: removeNumbers(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: replaceMultiExclamationMark(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: replaceMultiStopMark(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: replaceContraction(x))
#    df['tweets_preprocessed'] = df['tweets_preprocessed'].apply(lambda x: removeEmoticons(x))
#   return df

def preprocess_tweet(text: str):
    tweet_pp = removeUnicode(text)
    tweet_pp = replaceURL(tweet_pp)
    tweet_pp = replaceAtUser(tweet_pp)
    tweet_pp = removeHashtagInFrontOfWord(tweet_pp)
    tweet_pp = removeNumbers(tweet_pp)
    tweet_pp = replaceMultiExclamationMark(tweet_pp)
    tweet_pp = replaceMultiStopMark(tweet_pp)
    tweet_pp = replaceContraction(tweet_pp)
    tweet_pp = removeEmoticons(tweet_pp)
    return tweet_pp

