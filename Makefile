NAME = pbrain-player1.exe
NAME2 = pbrain-player2.exe
NAMEBIN = pbrain-gomoku-ai
SRC = src/pbrain_gomoku_ai.py
RM = rm -rf

all: $(NAMEBIN)

$(NAMEBIN):
	cp $(SRC) $(NAMEBIN)
	chmod +x $(NAMEBIN)

exec :
	pyinstaller --onefile --name pbrain-player1 $(SRC)
	cp dist/pbrain-player1 ./$(NAME2)
	mv dist/pbrain-player1 ./$(NAME)

clean:
	$(RM) dist build *.spec __pycache__

fclean: clean
	$(RM) $(NAME) $(NAME2) $(NAMEBIN)

re: fclean all
