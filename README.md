# Maltego

A collection of custom local transforms for the [Maltego](http://www.paterva.com/web6/products/maltego.php)
OSINT gathering tool.

## local_pull_aliases.py, local_pull_hashtags.py, local_pull_urls.py, local_tweet_to_words.py
I got tired of Maltego's flaky transforms for extracting entities out of Tweets
and thought it was unecessary to send tweets to a remote API endpoint to do
these simple tasks, so I created a collection of local transforms that do the same
in code instead.

### Requirements:
Depends on [twitter-text-python](https://github.com/edburnett/twitter-text-python) which
can be installed with `pip install twitter-text-python`.

**local_tweet_to_words.py** also depends on [Natural Language Toolkit](http://www.nltk.org/)
which can be installed with `pip install nltk`. After installation, execute
`python -c "import nltk; nltk.download()"` in a terminal and download the `stopwords`
package under the Corpora tab.
