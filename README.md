Cricket result prediction and sentiment analysis

Dataset Description :

*) Dataset consists of ball-to-ball cricket commentary of 100 overs of the 2011 world cup finals between Indian and Sri Lanka.
*) Data set was extracted from cricbuzz.com using JSoup (java library for data extraction from web)
*) Using the extracted data we classify the players based on their performance
*) Also, prediction of the match (who is going to win) in second innings



Data extraction : Data set was extracted from cricbuzz.com using JSoup (java library for data extraction from web)

Pre-processing :

*) Noise and stop words were removed from the dataset
*) Text to numeric conversion is done (from four to 4)
*) A score card was prepared to extract the score of each bowler and batsman
*) Each bowler's economy rate and each batsman's strike rate is calculated

Classification -
Rule based classification :

*) To classify the players based on their performance.
*) This is done by calculating the rating of a player by obtaining statistics about their performance at different stages of the match, with weightage given to each stage
*) A seperating point on the rating is calculated to classify
