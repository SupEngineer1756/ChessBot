from kaggle_environments import make

from Chessnut import Game
import random
import math
import pandas as pd
from collections import defaultdict
import tensorflow as tf
from tensorflow import keras
from NN import fenToFeatures

def modelEvaluateBoard(fen):
    model=tf.keras.models.load_model("chessBotNN.keras")
    X=pd.DataFrame([fenToFeatures(fen)])
    return model.predict(X)[0]
    
def getMove(game, color):
    best_score=0 if color=="w" else 10 
    best_move=None
    for move in game.get_moves(color):
        print("move=", move)
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        score=modelEvaluateBoard(game_copy.get_fen())
        print("score=", score)
        if color=="w":
            print("color=", color)
            if score > best_score:
                best_score=score
                best_move=move
                print("best_core_now=", best_score)
                print("best_move_now=", best_move)
        if color=="b":
            print("color=", color)
            if score < best_score:
                best_score=score
                best_move=move
                print("best_core_now_b=", best_score)
                print("best_move_now_b=", best_move)
    print("best_move=", best_move)
    print("best_score=", best_score)
    return best_move
    
def chessBot(fen):
    game = Game(fen)
    color=game.state.player
    return getMove(game, color)



startingFen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

game=Game(startingFen)
gameHistory=''
while not (game.status == Game.CHECKMATE or game.status == Game.STALEMATE):
    fen=game.get_fen()
    move=chessBot(fen)
    gameHistory+=' '+str(move)
    game.apply_move(move)

print(game.fen_history)
