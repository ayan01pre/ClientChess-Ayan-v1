import chess
import chess.engine

# ---------------- CONFIG ----------------

BOT_NAME = "ClientChess Ayan v1"

STOCKFISH_PATH = r"C:\Users\hp\OneDrive\Desktop\stockfish-windows-x86-64-avx2 (1)\stockfish\stockfish-windows-x86-64-avx2.exe"

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

board = chess.Board()

print("=" * 40)
print(f"♟️ {BOT_NAME}")
print("Powered by the ClientChess Project")
print("=" * 40)

# ---------------- COLOR CHOICE ----------------

color = input("Choose color (white/black): ").strip().lower()

if color == "white":
    HUMAN = chess.WHITE
else:
    HUMAN = chess.BLACK

print("\nCommands:")
print("board  -> show board")
print("hint   -> get best move suggestion")
print("eval   -> evaluate position")
print("fen    -> show FEN")
print("resign -> resign game\n")

# ---------------- GAME LOOP ----------------

while not board.is_game_over():

    print("\n" + str(board) + "\n")

    if board.turn == HUMAN:

        command = input("Your move or command: ").strip().lower()

        # ---------- COMMANDS ----------

        if command == "resign":
            print("🏳️ You resigned.")
            break

        elif command == "board":
            print(board)
            continue

        elif command == "fen":
            print("\nFEN:")
            print(board.fen())
            continue

        elif command == "hint":
            hint = engine.play(board, chess.engine.Limit(time=0.5))
            print(f"💡 Suggested move: {hint.move}")
            continue

        elif command == "eval":
            info = engine.analyse(board, chess.engine.Limit(depth=12))
            print("📊 Evaluation:", info["score"])
            continue

        # ---------- MOVE ----------

        try:
            move = chess.Move.from_uci(command)

            if move not in board.legal_moves:
                print("❌ Illegal move")
                continue

            board.push(move)

        except:
            print("❌ Invalid input")
            continue

    else:

        print(f"♟️ {BOT_NAME} thinking...")

        result = engine.play(
            board,
            chess.engine.Limit(time=0.5)
        )

        print(f"♟️ {BOT_NAME} plays:", result.move)

        board.push(result.move)

# ---------------- GAME END ----------------

print("\n🏁 GAME OVER")

if board.is_checkmate():

    if board.turn == HUMAN:
        print(f"☠️ Checkmate! {BOT_NAME} wins.")
    else:
        print("🔥 Checkmate! You win.")

elif board.is_stalemate():
    print("🤝 Draw by stalemate.")

elif board.is_insufficient_material():
    print("🤝 Draw by insufficient material.")

elif board.is_repetition():
    print("🤝 Draw by repetition.")

engine.quit()
