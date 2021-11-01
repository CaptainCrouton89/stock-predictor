# stock-predictor
Using neural networks to make stock predictions.

## Plan
- Use sentiment analysis on reddit + twitter
- Historical technical indicators: RSI, Momentum, Volume, a few more that "actually" work sometimes maybe
- Perform extensive backtesting on variety of stocks (must be GH for this somewhere)

### Sentiment Analysis
- https://www.reddit.com/r/stocks/comments/ll1h9n/any_well_documented_market_sentiment_analysis/
- Use glove, allow it to continue to train/fine-tune?
- Use pretrained sent. analyzer, fine tune
    - Needs to output stock and score for each ticker that appears in text
- Also takes in categorization for the source of information, threads vs comments vs headlines etc
- Scrape from non API websites
    - WSJ
    - SeekingAlpha
    - Check out reddit links to good sources
