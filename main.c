#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <ctype.h>

#define BUF_SIZE 1024

int	is_valid_num(char c)
{
	return (c >= '1' && c <= '9');
}

int	is_valid_num_txt(int index, char *line)
{
	char	*numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	int		len_at_pos = strlen(&line[index]);
	int		value = 0;

	for (int i = 0; i < 9; i++)
	{
		int	num_len = strlen(numbers[i]);
		if (num_len > len_at_pos) // not enough characters left in line
			continue ;
		if (!strncmp(&line[index], numbers[i], num_len))
		{
			value = i + 1;
			break ;
		}
	}
	return value;
}

void	get_next_line(int fd, char *line)
{
	char	char_read;
	char	buf;
	int		i = 0;

	char_read = read(fd, &buf, 1);
	while (char_read != 0 && buf != '\n')
	{
		line[i++] = buf;
		char_read = read(fd, &buf, 1);
	}
}

int	get_first(char *line)
{
	int	val = 0;
	int	i = 0;
	int	found = 0;

	while (!found)
	{
		int	is_text = is_valid_num_txt(i, line);
		if (is_text)
		{
			val = is_text;
			found = 1;
		}
		else if (is_valid_num(line[i]))
		{
			val = line[i] - '0';
			found = 1;
		}
		i++;
	}
	return val;
}

int	get_last(char *line)
{
	int	val = 0;
	int	i = strlen(line) - 1;
	int	found = 0;

	while (!found)
	{
		int	is_text = is_valid_num_txt(i, line);
		if (is_text)
		{
			val = is_text;
			found = 1;
		}
		else if (is_valid_num(line[i]))
		{
			val = line[i] - '0';
			found = 1;
		}
		i--;
	}
	return val;
}

int	get_cal_value(char *line)
{
	int	first;
	int	last;

	first = get_first(line);
	last = get_last(line);

	return first * 10 + last;
}

int	calibrate(int fd)
{
	int		result = 0;
	char	line[BUF_SIZE];

	memset(line, 0, sizeof(char) * BUF_SIZE);

	get_next_line(fd, line);
	while (strlen(line) != 0)
	{
		result += get_cal_value(line);
		memset(line, 0, sizeof(char) * BUF_SIZE);
		get_next_line(fd, line);
	}

	return result;
}

int main(int argc, char **argv)
{
	if (argc != 2)
	{
		fprintf(stderr, "Enter file name as argument\n");
		return 1;
	}

	int	fd = open(argv[1], O_RDONLY);
	if (fd < 0)
	{
		fprintf(stderr, "Could not open file: %s\n", argv[1]);
		return 1;
	}

	printf("Calibration result: %d\n", calibrate(fd));

	close(fd);
	return 0;
}