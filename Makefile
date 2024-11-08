NAME = pbrain-player1.exe
SRC = src/pbrain_gomoku_ai.py
RM = rm -rf

all: $(NAME)

$(NAME): $(SRC)
	pyinstaller --onefile --name pbrain-player1 $(SRC)
	mv dist/pbrain-player1 ./$(NAME)

clean:
	$(RM) dist build *.spec __pycache__

fclean: clean
	$(RM) $(NAME)

re: fclean all
