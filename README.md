# **Stock Price Prediction using Reddit Sentiment Analysis and LSTM**
This project predicts stock price movements by combining sentiment analysis of Reddit discussions with historical stock data. An LSTM model is trained to analyze public sentiment and market trends for predicting stock price movements.

# Prerequisites
Before running the project, ensure you have the following dependencies installed:

**Dependencies:**
Python 3.x (recommended version: 3.7 or higher)

Install the required libraries using pip:
pip install -r requirements.txt

**Required Libraries:**
pandas: For data manipulation.
numpy: For numerical operations.
nltk: For text preprocessing and sentiment analysis.
requests: To interact with the Reddit and stock APIs.
PRAW: Python Reddit API Wrapper (for scraping Reddit).
yfinance: Yahoo Finance API (for stock data).
tensorflow: For LSTM model creation and training.
scikit-learn: For model evaluation and data preprocessing.

**Requirements:**

pandas==1.5.3

numpy==1.23.5

nltk==3.8.1

requests==2.28.1

praw==7.7.0

yfinance==0.2.18

tensorflow==2.11.0

scikit-learn==1.1.2


# Setup Instructions

1. **Clone the Repository**
Clone this GitHub repository to your local machine:
git clone https://github.com/yourusername/stock-price-prediction.git
cd stock-price-prediction

2. **Install Dependencies**
Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Then, install the required Python libraries:
pip install -r requirements.txt

3. **Get Reddit API Credentials**
You need to create a Reddit app to get your API credentials. Follow these steps:
* Go to RAPIDAPI
* Search Reddit Scraper
* Note the API Key

4. **Get Stock API Key**
This project uses Yahoo Finance API (via yfinance) to get stock price data. No API key is required for Yahoo Finance.
However, if you plan to use RapidAPI or any other API for sentiment analysis, you will need to sign up at RapidAPI and get your API key.

# Running the Code

1. **Data Scraping**
Run the script to scrape Reddit posts related to stock discussions:
python scrape_reddit.py
This will collect Reddit posts related to the stock, and analyze the sentiment using the configured sentiment analysis API.

2. **Data Preprocessing**
After scraping data, preprocess it to prepare for training:
python preprocess_data.py
This will clean the Reddit data and combine it with historical stock data from Yahoo Finance.

3. **Train the Model**
Train the LSTM model using the preprocessed data:
python building_ltsm_model.py
This will train the model on the sentiment and historical stock data and save the trained model to disk.

4. **Make Predictions**
After the model is trained, you can use it to predict stock price movements:
python sentiment_into_ltsm.py

# Evaluation
You can evaluate the performance of your model using the following:
python modeltraing_and_evaluation.py

#File Structure

stock-price-prediction/



├── Requirements.txt                                           # Python dependencies

├── scrape_reddit.py                                           # Script to scrape Reddit data

├── preprocess_data.py                                         # Data cleaning and preprocessing

├── building_ltsm_model.py                                     # Training LSTM model

├── sentiment_into_ltsm.py                                     # Predict stock price movements

├── hyperparametertuning_and_crossvalidation.py                # Predict stock price movements

├── modeltraing_and_evaluation.py                              # Model evaluation script

├── Stock_Movement_Analysis_Using_LTSM.ipynb                              # Model evaluation script

└── README.md                                                  # Project documentation (this file)


# Contributing
If you would like to contribute to the project, feel free to fork the repository, make changes, and submit a pull request.
Make sure to include tests and documentation for your changes.

# License
This project is licensed under the MIT License – see the LICENSE file for details.

**Contact**
If you have any questions or need further assistance, please contact me via krithiknaveen93@gmail.com .
