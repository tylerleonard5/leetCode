#include <stdio.h>
#include <string.h>

char * intToRoman(int num){
    char* ans = malloc(100);
    int dig = 0;
    if (num == 1){
        return "I";
    }

    if (num == 5){
        return "V";
    }

    if (num == 10){
        return "X";
    }

    if (num == 50){
        return "L";
    }

    if (num == 100){
        return "C";
    }

    if (num == 500){
        return "D";
    }

    if (num == 1000){
        return "M";
    }

    while (num != 0){
        if(num >= 1000){
            num -= 1000;
            ans[dig] = 'M';
            dig++;
            continue;
        }
        if(num >= 900){
            num -= 900;
            ans[dig] = 'C';
            dig++;
            ans[dig] = 'M';
            dig++;
            continue;
        }
        if(num >= 500){
            num -= 500;
            ans[dig] = 'D';
            dig++;
            continue;
        }
        if(num >= 400){
            num -= 400;
            ans[dig] = 'C';
            dig++;
            ans[dig] = 'D';
            dig++;
            
            continue;
        }
        if(num >= 100){
            num -= 100;
            ans[dig] = 'C';
            dig++;

            continue;
        }
        if(num >= 90){
            num -= 90;
            ans[dig] = 'X';
            dig++;
            ans[dig] = 'C';
            dig++;
            
            continue;
        }
        if(num >= 50){
            num -= 50;
            ans[dig] = 'L';
            dig++;
            
            continue;
        }
        if(num >= 40){
            num -= 40;
            ans[dig] = 'X';
            dig++;
            ans[dig] = 'L';
            dig++;
            
            continue;
        }
        if(num >= 10){
            num -= 10;
            ans[dig] = 'X';
            dig++;
            
            continue;
        }
        if(num >= 9){
            num -= 9;
            ans[dig] = 'I';
            dig++;
            ans[dig] = 'X';
            dig++;
           
            continue;
        }
        if(num >= 5){
            num -= 5;
            ans[dig] = 'V';
            dig++;
            
            continue;
        }
        if(num >= 4){
            num -= 4;
            ans[dig] = 'I';
            dig++;
            ans[dig] = 'V';
            dig++;
            
            continue;
        }
        if(num >= 1){
            num -= 1;
            ans[dig] = 'I';
            dig++;
            
            continue;
        }
    }
    char *final = malloc(dig+1);
    for (int i = 0; i < dig; i++){
        
        final[i] = ans[i];
    }
    free(ans);
    ans = NULL;
    final[dig] = '\0';
    
    return final;
}