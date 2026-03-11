#include <stdio.h>
#include <conio.h>

int main()
{
    int allocation[10][5], max[10][5], need[10][5];
    int available[5];
    int flag[10], sq[10];
    int n, r;
    int i, j, k;
    int count, count1 = 0;

    clrscr();

    printf("\nInput the number of processes running (<10): ");
    scanf("%d", &n);

    printf("\nInput the number of resources (<5): ");
    scanf("%d", &r);

    for(i = 0; i < 10; i++)
        flag[i] = 0;

    printf("\nInput the allocation matrix for the processes:\n");

    for(i = 0; i < n; i++)
    {
        printf("\nProcess %d\n", i);
        for(j = 0; j < r; j++)
        {
            printf("Resource %d: ", j);
            scanf("%d", &allocation[i][j]);
        }
    }

    printf("\nInput the maximum matrix:\n");

    for(i = 0; i < n; i++)
    {
        printf("\nProcess %d\n", i);
        for(j = 0; j < r; j++)
        {
            printf("Resource %d: ", j);
            scanf("%d", &max[i][j]);
        }
    }

    printf("\nInput available resources:\n");
    for(i = 0; i < r; i++)
    {
        printf("Resource %d: ", i);
        scanf("%d", &available[i]);
    }

    printf("\nNeed Matrix:\n");

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < r; j++)
        {
            need[i][j] = max[i][j] - allocation[i][j];
            printf("%d ", need[i][j]);
        }
        printf("\n");
    }

    do
    {
        for(k = 0; k < n; k++)
        {
            for(i = 0; i < n; i++)
            {
                if(flag[i] == 0)
                {
                    count = 0;

                    for(j = 0; j < r; j++)
                    {
                        if(available[j] >= need[i][j])
                            count++;
                    }

                    if(count == r)
                    {
                        flag[i] = 1;
                        sq[count1] = i;
                        count1++;

                        for(j = 0; j < r; j++)
                        {
                            available[j] = available[j] + allocation[i][j];
                        }
                    }
                }
            }
        }

        if(count1 != n)
        {
            printf("\nIT IS UNSAFE STATE\n");
            break;
        }

    } while(count1 != n);

    if(count1 == n)
    {
        printf("\nIT IS SAFE STATE\n");
        printf("Safe Sequence:\n");

        for(i = 0; i < n; i++)
        {
            printf("P%d ", sq[i]);
        }

        printf("\nAvailable Resources:\n");

        for(i = 0; i < r; i++)
        {
            printf("%d ", available[i]);
        }
    }

    getch();
    return 0;
}
