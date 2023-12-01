NAME := trebuchet
CC := gcc
CFLAGS := -Wall -Werror -Wextra

SRC := main.c

all: $(NAME)

$(NAME): $(SRC)
	gcc $(CFLAGS) $(SRC) -o $(NAME)

fclean:
	rm $(NAME)