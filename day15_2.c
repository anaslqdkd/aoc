#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_LEN 100000

struct _Data{
    char *mot;
    char *symbol;
    int *number;
};
typedef struct _Data Data;

struct _Pair{
    char *mot;
    int number;
};
typedef struct _Pair Pair;

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


Data *recup_list(char *string){
    Data *res;
    res = (Data *)malloc(sizeof(Data));
    int len_mot = 0;
    char *deb = string;
    while (*string != '=' && *string != '-' && *string != '\0'){
        string ++;
        len_mot ++;
    }
    res->mot = (char *)malloc((len_mot + 1) * sizeof(char));
    for (int i = 0; i<len_mot; i ++){
        res->mot[i] = *deb;
        deb ++;
    }
    res->mot[len_mot] = '\0';
    res->symbol = (char *)malloc(sizeof(char) + 1);
    res->symbol[0] = *string;
    res->symbol[1] = '\0';
    res->number = (int *)malloc(sizeof(int));
    string ++;
    res->number[0] = *string - '0';
    return res;
}

void print_dict(Pair (*dict)[10], int size_i, int size_j){
    for (int i = 0; i<256; i++){
        for (int j = 0; j<10; j++){
            printf("Array [%d][%d]: Key: %s, Value: %d\n", i, j, dict[i][j].mot, dict[i][j].number);
        }
    }
}


char **key_list(Pair (*dict)[10], int box){
    char **res = malloc(sizeof(char *) * 10);
    int count = 0;
    for (int i = 0; i < 10; i++){
        if (dict[box][i].mot != NULL){
            res[count ++] = dict[box][i].mot;
        }
    }
    res[count] = NULL;
    return res;
}

int in_keylist(Pair (*dict)[10], int box, char *mot){
    char **keys = key_list(dict, box);
    int i = 0;
    /* printf("keys[i]: %s\n", keys[i]); */
    while (keys[i] != NULL){
        if (strcmp(keys[i], mot) == 0){      /* bizarre avec == on a le printf qui s'affiche mais ça ne renvoie pas 0 */
            /* printf("keys[i]: %s\n", keys[i]); */
            return 0;
        }
        i ++;
    }
    return 1;
}

void print_string_array(char **strings) {
    for (int i = 0; strings[i] != NULL; i++) {
        printf("%s\n", strings[i]); 
    }
}

void append(Pair (*dict)[10], int box, Data *data){
    int i = 0;
    int current_len = 0;
    char *mot = data->mot;
    int *number = data->number;
    while (dict[box][i].mot != NULL){
        current_len ++;
        i ++;
    }
    if (current_len < 10){
        dict[box][current_len].mot = malloc(sizeof(char) * strlen(mot) + 1);
        strcpy(dict[box][current_len].mot, mot);
        dict[box][current_len].number = *data->number;
        /* printf("current_len: %d\n", current_len); */
        /* printf("dict[box][current_len].mot: %s\n", dict[box][current_len].mot); */
    }else {
        puts("Error: idk");
        exit(1);
    }
}

int indice(Pair (*dict)[10], int box, char *string){
    int i = 0;
    while (strcmp(dict[box][i].mot, string) != 0){
        i ++;
    }
    return i;
}

void delete_element(Pair *array, int index) {
    free(array[index].mot); 
    memmove(&array[index], &array[index + 1], (10 - index - 1) * sizeof(Pair)); 
    array[10 - 1].mot = NULL;
}

void insert_val(Pair (*dict)[10], char *string){
    Data *tpl_string = recup_list(string);
    int box = hash(tpl_string->mot);
    if ((strcmp(tpl_string->symbol, "=") == 0) && in_keylist(dict, box, tpl_string->mot) == 1){
        /* printf("insert_val"); */
        append(dict, box, tpl_string);
    }
    if ((strcmp(tpl_string->symbol, "=") == 0) && in_keylist(dict, box, tpl_string->mot) == 0){
        int index = indice(dict, box, tpl_string->mot);
        dict[box][index].number = *tpl_string->number;
    }
    if ((strcmp(tpl_string->symbol, "-") == 0) && in_keylist(dict, box, tpl_string->mot) == 0){
        int index = indice(dict, box, tpl_string->mot);
        delete_element(dict[box], index);
        /* recuperer l'indice de l'element et effacer la lentille */
    }
}

int count(Pair (*dict)[10], int box){
    int i = 0;
    int len = 0;
    int res = 0;
    while (dict[box][i].mot != NULL){
        i ++;
        len ++;
        printf("%d\n", len);
    }
    for (int j = 0; j <= len; j ++){
        res += (box + 1)*(j + 1)*dict[box][j].number;
    }
    return res;
}


int main(){

    FILE *file = fopen("input.txt", "r");
    if (file == NULL){
        puts("Error opening file");
        exit(1);
    }

    char buffer[MAX_LEN];
    char *file_line = fgets(buffer, MAX_LEN, file);
    if (file_line == NULL){
        puts("Error opening line");
        exit(1);
    }
    int len_line = strlen(file_line);
    file_line[len_line] = '\0';

    Pair dict[256][10];
    for (int i = 0; i < 256; i++){
        for (int j = 0; j < 10; j++){
            dict[i][j].mot = NULL; 
            dict[i][j].number = 0;
        }
    }

    char *token;
    char str[] = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7" ;

    char *newline = strchr(file_line, '\n');
    if (newline != NULL){
        *newline = '\0';
    }

    token = strtok(file_line, ",");
    while (token != NULL){
        /* printf("%s\n", token); */
        insert_val(dict, token);
        token = strtok(NULL, ",");
    }
    print_dict(dict, 256, 10);
    printf("count function: %d\n", count(dict, 1));
    int c = 0;
    for (int i = 0; i<256; i++){
        c += count(dict, i);
    }
    printf("%d\n", c);
    /* insert_val(dict, "rararrarr=1"); */
    /* print_dict(dict, 256, 10); */
    /* printf("hash: %d\n", hash("rararrarr")); */
    /* print_string_array(key_list(dict, 95)); */
    /* printf("in key_list: %d\n", in_keylist(dict, 95, "rararrarr")); */
    /* char *s = "gaga=2,cm-"; */
    /* Data *data = recup_list(s); */
    /* printf("data: %d\n", *data->number); */
    /* append(dict, 95, data); */
    /* print_dict(dict, 256, 10); */
    /* insert_val(dict, "re=5"); */
    /* char *f = "gaga=3"; */
    /* append(dict, 103, recup_list(f)); */
    /* print_dict(dict, 256, 10); */
    /* printf("hash: %d\n", hash("re")); */
    /* delete_element(dict[103], 0); */
    /* print_dict(dict, 256, 10); */
    /* printf("%d\n", indice(dict, 103, "gaga")); */
    /* insert_val(dict, "rn=1"); */
    /* insert_val(dict, "cm-"); */
    /* insert_val(dict, "qp=3"); */
    /* insert_val(dict, "cm=2"); */
    /* insert_val(dict, "qp-"); */
    /* insert_val(dict, "pc=4"); */
    /* insert_val(dict, "ot=9"); */
    /* insert_val(dict, "ab=5"); */
    /* insert_val(dict, "pc-"); */
    /* insert_val(dict, "pc=6"); */
    /* insert_val(dict, "ot=7"); */
    /* print_dict(dict, 256, 10); */

    return 0;
}
