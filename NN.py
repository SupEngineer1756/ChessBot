import numpy as np
import chess
import os 
import pandas as pd 
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error

### Constants ###
FEN_STORAGE_DIR = "fen_storage"

### Labeling ###

def createTrainingData(fenDir):
    X_data=[]
    y_data=[]
    
    os.makedirs(fenDir, exist_ok=True)
    
    existing_files = os.listdir(fenDir)
    
    for file in existing_files:
        file_path = os.path.join(fenDir, file)
        df = pd.read_csv(file_path)
        X_data.append(df.loc[0].at["FEN"])
        total_games=df["FEN"].count()
        total_games_white_won=df[(df["Winner"]==1)].shape[0]
        y_data.append(total_games_white_won/total_games)
    
    X_=[]
    for fen_ in X_data:
        X_.append(fenToFeatures(fen_))
        
    y=pd.DataFrame(y_data)
    X=pd.DataFrame(X_)
    
    return X,y

### Feature engineering ###

def fenToBitboard(fen):
    board = chess.Board(fen)
    piece_symbols = "PNBRQKpnbrqk"
    bitboards = np.zeros((12, 64), dtype=np.uint8)

    for i, piece in enumerate(piece_symbols):
        for square in range(64):
            if board.piece_at(square) and board.piece_at(square).symbol() == piece:
                bitboards[i][square] = 1
                
    return bitboards.flatten()  # Shape (768,)

def encodeSideToMove(fen):
    return np.array([1 if " w " in fen else 0])

def encodeCastling(fen):
    rights = fen.split()[2]
    return np.array([
        1 if "K" in rights else 0,
        1 if "Q" in rights else 0,
        1 if "k" in rights else 0,
        1 if "q" in rights else 0
    ])
    
def encodeEnPassant(fen):
    en_passant = fen.split()[3]
    return np.array([0 if en_passant == "-" else 1])

def encodeMoveCounters(fen):
    halfmove, fullmove = map(int, fen.split()[4:6])
    return np.array([halfmove / 100, fullmove / 200])

def fenToFeatures(fen):
    bitboard_features = fenToBitboard(fen)
    side_to_move = encodeSideToMove(fen)
    castling_features = encodeCastling(fen)
    en_passant_feature = encodeEnPassant(fen)
    move_counters = encodeMoveCounters(fen)

    return np.concatenate([
        bitboard_features, side_to_move, castling_features,
        en_passant_feature, move_counters
    ])

### Neural network ###

def createModel():
    input_shape = (776,)

    model = keras.Sequential([
        keras.layers.Dense(8, activation="relu", input_shape=input_shape),
        keras.layers.Dense(8, activation="relu"),
        keras.layers.Dense(1, activation="relu")  
    ])
    return model
    
def trainModel(X,y, model):
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X, y, epochs=100, batch_size=64, validation_split=0.2)
    model.save("chessBotNN.keras")



### Train Model ###

model=createModel()
X,y=createTrainingData(FEN_STORAGE_DIR)
trainModel(X,y, model)