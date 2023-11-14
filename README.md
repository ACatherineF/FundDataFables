# FundDataFables
This README will guide you through the project structure and usage.

This repo fetch Yahoo Financial data and perform some analysis on that data fetched for a given time range and stock.

In the second part of this repo, we extrapolate the dataset to study the correlation and perform some regression to predict future values.

## Project Structure

The project structure is as follows:

- `main.py`: 
- `dataset.py`: Contains the `Dataset` class, which fetch financial information from Yahoo and save it as a dataframe.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/FundDataFables.git
   ```

2. Activate your virtual environment:
      ```bash
   source {environment_name}/bin/activate
   ```
   or create it first if it does not exist:
      ```bash
   python -m venv {environment_name}
   ```
   
3. Install the requirements:
      ```bash
   pip install -r requirements.txt
   ```

4. Run the code:
      ```bash
   python main.py
   ```

5. Deactivate your virtual environment:
      ```bash
   deactivate
   ```