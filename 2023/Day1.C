#include <stdio.h>
#include <stdlib.h>
#include <ctype.h> 
#include <string.h>

typedef struct {
    char *word;
    int value;
} NumberWord;

int findNumberWord(const char *str, const NumberWord *words, int wordCount) {
    for (int i = 0; i < wordCount; ++i) {
        if (strcmp(str, words[i].word) == 0) {
            return words[i].value;
        }
    }
    return -1; // Return -1 or some other value to indicate 'not found'
}

int main() {
    NumberWord words[] = {
        {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, 
        {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}
    };
    int wordCount = sizeof(words) / sizeof(words[0]);

    const char *filepath = "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/Day1Input.txt";
    FILE *file = fopen(filepath, "r");

    if (file == NULL)
    {
        printf("Failed to open the file.\n");
        return 1;
    }

    char line[100];
    int vectors[1000] = {0};
    int counter = 0;
    while (fgets(line, sizeof(line), file) != NULL)
    {
        char numbers[100] = "";
        int j = 0;
        char *token = strtok(line, " ,.!?");

        while (token != NULL) {
            int num = findNumberWord(token, words, wordCount);
            if (num != -1) {
                printf("Found number: %d\n", num);
            }
            token = strtok(NULL, " ,.!?");
        }

        //plocka bort all som inte är nummer och löser uppgiften
        for (int i = 0; line[i] != '\0'; ++i) {
            if (isdigit((unsigned char)line[i])) {
                numbers[j++] = line[i];
            }
        }
        
        if (numbers[1] == 0) {
            vectors[counter] = (numbers[0] - '0')*10 + numbers[0] - '0';
        }
        else {
            int lastNumber = 0;
            for (int i = 0; i < 100; i++)
            {
                if (numbers[i] != 0)
                {
                    lastNumber = numbers[i] - '0';
                }
                else if(numbers[i] == 0) {
                    vectors[counter] = (numbers[0] - '0')*10 + lastNumber;
                }
            }
        }
    counter++;
    }
    

    fclose(file);
}