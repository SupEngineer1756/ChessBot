# ChessBot

A neural network based chessBot

## Overview

ChessBot is a Python-based project that leverages neural networks to analyze and generate chess moves. It includes modules for data preprocessing, FEN (Forsyth–Edwards Notation) string cleaning, and a pre-trained Keras model to evaluate chess positions. Whether you’re interested in AI-driven chess engines or exploring neural network applications in games, ChessBot offers a modular framework to build upon.

## Features

- **Neural Network Integration:**  
  Implements a custom neural network (see `NN.py`) for evaluating chess positions and predicting moves.

- **Data Preprocessing:**  
  The `Data preprocessing.py` script prepares chess game data for training and evaluation.

- **FEN String Processing:**  
  Utilizes `FenCleaning.py` to clean and standardize FEN strings for accurate board representations.

- **Pre-trained Model:**  
  Includes a Keras model (`chessBotNN.keras`) for immediate testing without the need for initial training.

- **Dataset Included:**  
  Provides a sample chess game dataset (`games.csv`) to help you get started.

- **Additional FEN Data:**  
  Contains extra FEN data in `fen_storage.zip` for extended experiments and model enhancements.

## Repository Structure

```plaintext
ChessBot/
├── Data preprocessing.py      # Script for preprocessing chess game data
├── FenCleaning.py             # Utility for cleaning FEN strings
├── NN.py                      # Neural network architecture and training routines
├── main.py                    # Main script to run the chessBot
├── chessBotNN.keras           # Pre-trained Keras model file
├── fen_storage.zip            # Archive containing FEN data
└── games.csv                  # Dataset of chess games
```

## Installation

### Prerequisites

- Python 3.x
- [TensorFlow](https://www.tensorflow.org/) (as the backend for Keras)
- [Keras](https://keras.io/)
- Other Python libraries (e.g., NumPy, Pandas)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SupEngineer1756/ChessBot.git
   cd ChessBot
   ```

2. **Install Dependencies**

   Install the necessary packages:

   ```bash
   pip install tensorflow keras numpy pandas
   ```

4. **Extract FEN Storage**

   Unzip the `fen_storage.zip` :

   ```bash
   unzip fen_storage.zip
   ```

## Usage

### Running the ChessBot

To start the chess bot, run the main script:

```bash
python main.py
```

This script will load the pre-trained model, process the necessary data, and run the chess engine, allowing the bot to evaluate chess positions and suggest moves.

### Training the Model

If you wish to train or fine-tune the model, follow these steps:

1. **Preprocess the Data**

   Run the data preprocessing script to prepare your chess game data from a .csv dataset containing games:

   ```bash
   python "Data preprocessing.py"
   ```

2. **Train the Neural Network**

   Adjust any training parameters in `NN.py` as needed, then run:

   ```bash
   python NN.py
   ```

## Contributing

Contributions are welcome! If you have improvements, bug fixes, or new ideas, feel free to open an issue or submit a pull request.

## License

This project is open-source.

## Contact

For any questions, issues, or suggestions, please open an issue in the repository or contact me.

