# Sentiment & Emotion Analysis
The main aim of this project is to extract data from the e-commerce websites such as Amazon, Flipkart etc.

Sentiment Analysis
------
Let's Take the following example
```
"This is an example of good documentation."
```
Now obviously, we can tell that this is a positive sentence because it was written as such and we can
comprehend what is being conveyed.
But this might prove tough for a machine, figuring out wether the sentence has been said in a good
way or a bad way.Sentiment Analysis is the process of computationally identifying and categorizing opinions expressed in a piece of text, especially in order to determine whether the writer's attitude towards a particular topic, product, etc. is positive, negative, or neutral.

## Emotion Analysis
------
Emotion Analysis scores the given statement based on 8 emotions

* Joy
* Anticipation
* Trust
* Surprise
* Sadness
* Disgust
* Fear
* Anger

and scores the sentence in these parameters.The Scores for the previous sentence should look something like this:

|Joy   |  Anticipation|  Trust|  Surprise|  Sadness|  Disgust|  Fear|  Anger|
|-----:|-------------:|------:|---------:|--------:|--------:|-----:|------:|
|7     |  2           |  4    |  6       |  1      |  0      |  3   |  0    |

## Web Scraping
------
This was done using [Scrapy](https://scrapy.org/), by making web spiders that crawled e-commerce websites like amazon to get user opinion such as comments and reviews.
There were other Parameters such as date and Number of stars(out of five) which will be present in the refference dataset.
