# Road to the Solution
When I first read the challenge and what it asked, my immediate solution was to find an API that had the ability to quantify the connotation of different words. I came across several that could do so, but the text file was a little large and most of these API's were more accurate with short inputs. 

From there, I could have done two things:
    1. Call the API so that it would create a score for each sentence and then average these scores.
    2. Continue researching for an API that could do a better job with large inputs.

Given that I had the time this weekend I continued researching and found Twinword INC.. Twinword has their own sentiment analysis and emotion analysis API's. They created these API's by adding to their past product that found keywords based on patterns, popularity, and user intent. So this API works great with large inputs because it only uses the keywords to generate a score for the text.



## API's
[This](https://rapidapi.com/twinword/api/sentiment-analysis/) is the API I used for creating a score for sentiment analysis. 

[This](https://rapidapi.com/twinword/api/emotion-analysis/) is the API I used for generating scores for the different emotions invoked in the text.



This is how the creaters of the API, Twinword INC. calculates their score and ratio.
### Calculating score for sentiment analysis
The score indicates how negative or positive the overall text analyzed is. Anything below a score of -0.05 is tagged as negative and anything above 0.05 is tagged as positive. Anything in between inclusively, is tagged as neutral.

### Calculating ratio for sentiment analysis
The ratio is the combined total score of negative words compared to the combined total score of positive words, ranging from -1 to 1.

Let’s say we are analyzing words A, B, C and D.

    Scenario 1) If words A and B are negative words having a combined total score of -5.0 and words C and D are positive words having a combined total score of 5.0, then the ratio would be 0 (or 1:1) as both sides are balanced.
    Scenario 2) If negative words have a total combined score of -5.0 while positive words have a total combined score of 2.5, then the ratio would be -0.667 (or 2:1).
    Scenario 3) If negative words total -5.0 and positive words total 0.0, then the ratio would be -1 (or 1:0).