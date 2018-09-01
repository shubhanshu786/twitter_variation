# twitter_variation

Almost every machine learning developer has faced issue with variation characters used over social media. e.g., **_ṦϦừɓℏ_** is my name but due to the use of variation latters, it can not be treated as **_Shubh_**.

To solve this issue i compiled an extensive list of variations for english language so that social media can also be understood easily by machines.

## Installation

```
pip install twitter_variation
```


## Usage

This is a very nominal package with just one function name **variation_to_english(sent='')** which expect sentences/data(whole data is also fine) and returns cleaned data after converting all variation words into english letters.

```
>>>import twitter_variation
>>>twitter_variation.variation_to_english('ṦϦừɓℏ')
>>>shubh
```
## Note

Perform this operation after taking care of **@users_mention** on twitter data since **@** will be converted to **a** if used before.
