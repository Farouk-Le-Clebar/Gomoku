NAME = pbrain-player1.exe
NAMEBIN = pbrain-gomoku-ai
SRC = src/pbrain_gomoku_ai.py
RM = rm -rf
SOURCE_FILES = $(wildcard src/**/*.py)
PYTHON_ENTRY = src/pbrain_gomoku_ai.py

all: $(NAMEBIN)

$(NAMEBIN):
	cp $(SRC) $(NAMEBIN)
	chmod +x $(NAMEBIN)

build: $(SOURCE_FILES)
	pyinstaller --onefile --name $(NAME) $(PYTHON_ENTRY)

exec :
	pyinstaller --onefile --name pbrain-player1 $(SRC)
	cp dist/pbrain-player1 ./$(NAME2)
	mv dist/pbrain-player1 ./$(NAME)

clean:
	$(RM) dist build *.spec __pycache__

fclean: clean
	$(RM) $(NAME) $(NAME2) $(NAMEBIN)

re: fclean all
