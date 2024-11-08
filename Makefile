NAME = pbrain-gomoku-ai
SRC = src/pbrain_gomoku_ai.py
RM = rm -rf

all: $(NAME)

$(NAME): $(SRC)
	echo '#!/bin/sh' > $(NAME)
	echo 'exec python3 $(SRC)' >> $(NAME)
	chmod +x $(NAME)

clean:
	$(RM) *.pyc __pycache__

fclean: clean
	$(RM) $(NAME)

re: fclean all