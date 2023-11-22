# Bloom Filter

## Overview

This Python script implements a Bloom filter to efficiently check the presence of words in a dataset of comments, particularly focusing on Trump's tweets over a 10-month period. The Bloom filter is a probabilistic data structure that allows for quick membership tests with a controlled false-positive rate.

## Project Structure

1. **`bloom_filter.py`:**
   - The main script that creates a Bloom filter, loads a dataset of comments (e.g., Trump's tweets from a CSV file), and checks if a given word is likely to be present in the comments.

2. **`comments.csv`:**
   - The dataset containing comments, especially focusing on Trump's tweets over a 10-month period.

3. **`requirements.txt`:**
   - Lists the required dependencies, including `pybloom-live` and `csv`.

4. **`README.md`:**
   - The README file you are currently reading, providing an overview of the project and instructions on how to run the script.

## Getting Started

Follow these steps to set up and run the Trump Tweets Bloom Filter project:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/trump-tweets-bloom-filter.git
   cd trump-tweets-bloom-filter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a CSV file named `comments.csv` with the appropriate data (Trump's tweets over 10 months).

4. Run the Bloom filter script:
   ```bash
   python bloom_filter.py
   ```

   Follow the prompts to enter a word and check its presence in the comments.

## Dataset Information

The `comments.csv` file contains comments, with a focus on Trump's tweets, spanning over a 10-month period. You can replace this dataset with your own as needed.

## Contributing

Contributions are welcome! If you have suggestions, find issues, or want to enhance the project, please feel free to open issues or submit pull requests.


