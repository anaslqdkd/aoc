#include <stdlib.h>
#include <stdio.h>
#define MAX_LEN 100000
/* #ifdef PART1 */

int hash(char *string){
    int current = 0;
    if (string == NULL){
        return current;
    }
    while (*string != '\0'){
        int ascii_code = (int)*string;
        current += ascii_code;
        current *= 17;
        current %= 256;
        string ++;
    }
    return current;
}

int len_word(char *string){
    if (string == NULL){
        return 0;
    }
    int len = 0;
    while (*string != ',' && *string != '\0'){
        len ++;
        string ++;
    }
    return len;
}

int len_string(char *string){
    if (string == NULL){
        return 0;
    }
    int len = 0;
    while (*string != '\0'){
        len ++;
        string ++;
    }
    return len;
}
char *recup_word(char *string){
    if (string == NULL){
        return NULL;
    }
    int len = len_word(string);
    char *word = (char *)malloc((len+1) * sizeof(char));
    for (int i = 0; i<len; i++){
        word[i] = *string;
        string ++;
    }
    word[len] = '\0';
    return word;
}

char *recup_string(char *string){
    if (string == NULL){
        return NULL;
    }
    int len_mot= len_word(string);
    int n = len_mot;
    int len_rem_string = len_string(string) - len_mot;
    int i = 0;
    /* char *deb = string; */
    /* while (*deb != ','){ */
    /*     deb ++; */
    /* } */
    char *rem_string = (char *)malloc((len_rem_string + 1) * sizeof(char));
    while (n != 0 && *string != '\0'){
        string ++;
        n --;
    }
    string ++;
    while (*string != '\0'){
        rem_string[i] = *string;
        string ++;
        i ++;
    }
    rem_string[len_rem_string] = '\0';
    /* deb ++; */ 
    return rem_string;
}

int count(char *string){
    int c = 0;
    if (string == NULL || *string == '\0'){
        return 0;
    }
    char *mot = recup_word(string);
    c += hash(mot);
    string = recup_string(string);
    free(mot);
    c += count(string);
    /* free(string); */
    return c;
}


int main(int argc, char **argv){
    if (argc <= 1){
        puts("Error: Not enough arguments");
        exit(1);
    }
    FILE *file = fopen(argv[1], "r");
    if (file == NULL){
        EXIT_FAILURE;
    }
    char buffer[MAX_LEN];
    char *test_string = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7";
    char *line_l = fgets(buffer, MAX_LEN, file);
    int line_l_len = len_string(line_l);
    line_l[line_l_len-1] = '\0';
    printf("%d\n", count(line_l));
    return 0;
}
/* #endif */
