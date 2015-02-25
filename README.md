# Maltego

A collection of custom local transforms for the [Maltego](http://www.paterva.com/web6/products/maltego.php)
OSINT gathering tool.

## local_pull_aliases.py, local_pull_hashtags.py, local_pull_urls.py, local_tweet_to_words.py
Extracts entities from Tweets just like the built-in transforms, but faster as they
don't send the Tweets off the the remote servers, but extract the entities locally in code.

### Requirements:
Depends on [twitter-text-python](https://github.com/edburnett/twitter-text-python) which
can be installed with `pip install twitter-text-python`.

**local_tweet_to_words.py** also depends on [Natural Language Toolkit](http://www.nltk.org/)
which can be installed with `pip install nltk`. After installation, execute
`python -c "import nltk; nltk.download()"` in a terminal and download the `stopwords`
package under the Corpora tab.

## follow_redirects.py
URL transform that follows up to 15 HTTP redirects and returns the final URL.
Convenient if a transform returns a shortened or obfuscated URL.

**Note:** Running this transform will potentially engage target systems,
so if you're doing passive reconnaissance, this transform should not be used!
