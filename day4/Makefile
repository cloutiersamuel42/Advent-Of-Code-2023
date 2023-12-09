
NAME := day4.jar

SRC := Main.kt

all: $(NAME)

$(NAME): $(SRC)
	kotlinc $(SRC) -include-runtime -d $(NAME)

run:
	@kotlin $(NAME)