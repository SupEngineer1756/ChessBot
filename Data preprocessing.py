import os
import pandas as pd
import chess
import chess.pgn
import uuid
from tqdm import tqdm
import re

FEN_STORAGE_DIR = "fen_storage"
os.makedirs(FEN_STORAGE_DIR, exist_ok=True)

def clean_fen(fen):
    
    fen = re.split(r"[-]", fen, maxsplit=1)[0].strip()
    fen = fen.replace("/", "0")
    return fen

def generate_fen_history(moves):
    
    board = chess.Board()
    fen_history = []
    
    for move in moves:
        board.push_san(move)  
        fen_history.append(board.fen())  
    
    return fen_history

def process_game(game_moves, winner, total_moves):
    fen_list = generate_fen_history(game_moves)
    
    for move_index, fen in enumerate(fen_list):
        print("processing move = ", move_index)
        moves_remaining = total_moves - move_index
        result = 1 if winner == "white" else 0
        fen_filename = os.path.join(FEN_STORAGE_DIR, clean_fen(fen)+".csv")
        existing_files = os.listdir(FEN_STORAGE_DIR)
        for file in existing_files:
            file_path = os.path.join(FEN_STORAGE_DIR, file)
            if os.path.isfile(file_path):
                df = pd.read_csv(file_path)
                if fen in df["FEN"].values:
                    df.loc[df["FEN"] == fen, "Winner"].apply(lambda x: f"{x},{result}")
                    df.loc[df["FEN"] == fen, "Moves_Left"].apply(lambda x: f"{x},{moves_remaining}")
                    df.to_csv(file_path, index=False)
                    break
        else:
                df = pd.DataFrame({"FEN": [fen], "Winner": [result], "Moves_Left": [moves_remaining]})
                df.to_csv(fen_filename, index=False)
                print("file added")

def main(input_csv):
    
    df = pd.read_csv(input_csv)
    for index, row in tqdm(df.iterrows(), total=100):
        print("processing game = ", index)
        game_moves = row["moves"].split()
        winner = row["winner"]
        total_moves = row["turns"]
        process_game(game_moves, winner, total_moves)

if __name__ == "__main__":
    input_csv = "games.csv"  
    main(input_csv)
