def game(player1: str, player2: str, place1: list, place2: list, walls: list, turn: int, result: bool, game_ID: str):
    new_game_data = {
        game_ID: {   
            "player1": player1,
            "player2": player2,
            "place1": place1,
            "place2": place2,
            "walls": walls,
            "turn": turn,
            "result": result
        }
    }