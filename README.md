# diana-compiler

可以把 C 代码编译成然然的形状捏 🥰

使用方法：`python diana.py [-h] [-i INPUTS [INPUTS ...]]`

> 因为我本地的编译器不支持 unicode 变量名，所以代码未经充分测试，可能有不少 bug，请小心食用

# 示例

- 输入：

```c
#include <stdio.h>
#include <stdlib.h>
 
#define BUF_SIZE 10

void display(int array[], int maxlen)
{
    int i;
    for(i = 0; i < maxlen; i++)
    {
        printf("%-3d", array[i]);
    }
    printf("\n");
}

void QuickSort(int *arr, int low, int high)
{
    if (low < high)
    {
        int i = low;
        int j = high;
        int k = arr[low];
        while (i < j)
        {
            while(i < j && arr[j] >= k)     
            {
                j--;
            }
            if(i < j)
            {
                arr[i++] = arr[j];
            }
            while(i < j && arr[i] < k)      
            {
                i++;
            }
            if(i < j)
            {
                arr[j--] = arr[i];
            }
        }
        arr[i] = k;  
        QuickSort(arr, low, i - 1);     
        QuickSort(arr, i + 1, high);    
    }
}

int main()
{
    int array[BUF_SIZE] = {12,85,25,16,34,23,49,95,17,61};
    int maxlen = BUF_SIZE;
    
    display(array, maxlen);
    QuickSort(array, 0, maxlen-1);
    display(array, maxlen);
    return 0;
}
```

- 输出：

```c
#define 然然 void
#define 🤤 display
#define 🥵 (
#define 然然然然 int
#define 然然🤤 array
#define 然然🥵 [],
#define 🤤然然 maxlen
#define 🤤🤤 )
#define 🤤🥵 {
#define 🥵然然 i
#define 🥵🤤 ;
#define 🥵🥵 for
#define 然然然然然然 =
#define 然然然然🤤 0
#define 然然然然🥵 <
#define 然然🤤然然 ++)
#define 然然🤤🤤 printf
#define 然然🤤🥵 "%-3d"
#define 然然🥵然然 ,
#define 然然🥵🤤 [
#define 然然🥵🥵 ]);
#define 🤤然然然然 }
#define 🤤然然🤤 "\n"
#define 🤤然然🥵 );
#define 🤤🤤然然 return
#define 🤤🤤🤤 QuickSort
#define 🤤🤤🥵 *
#define 🤤🥵然然 arr
#define 🤤🥵🤤 low
#define 🤤🥵🥵 high
#define 🥵然然然然 if
#define 🥵然然🤤 j
#define 🥵然然🥵 k
#define 🥵🤤然然 ];
#define 🥵🤤🤤 while
#define 🥵🤤🥵 ]
#define 🥵🥵然然 >=
#define 🥵🥵🤤 --;
#define 🥵🥵🥵 ++]
#define 然然然然然然然然 ++;
#define 然然然然然然🤤 --]
#define 然然然然然然🥵 -
#define 然然然然🤤然然 1
#define 然然然然🤤🤤 +
#define 然然然然🤤🥵 main
#define 然然然然🥵然然 ()
#define 然然然然🥵🤤 BUF_SIZE
#define 然然然然🥵🥵 12
#define 然然🤤然然然然 85
#define 然然🤤然然🤤 25
#define 然然🤤然然🥵 16
#define 然然🤤🤤然然 34
#define 然然🤤🤤🤤 23
#define 然然🤤🤤🥵 49
#define 然然🤤🥵然然 95
#define 然然🤤🥵🤤 17
#define 然然🤤🥵🥵 61
#define 然然🥵然然然然 };
#include <stdio.h>
#include <stdlib.h>
#define BUF_SIZE 10
然然 🤤🥵然然然然 然然🤤然然🥵 然然然然 🤤然然🤤🤤
🤤🥵
然然然然 🥵然然🥵🤤
🥵🥵🥵🥵然然 然然然然然然 然然然然🤤🥵🤤 🥵然然 然然然然🥵 🤤然然🥵🤤 🥵然然然然🤤然然
🤤🥵
然然🤤🤤🥵然然🤤🥵然然🥵然然 然然🤤然然🥵🤤🥵然然然然🥵🥵
🤤然然然然
然然🤤🤤🥵🤤然然🤤🤤然然🥵
🤤🤤然然 🥵🤤
🤤然然然然
然然 🤤🤤🤤🥵然然然然 🤤🤤🥵🤤🥵然然然然🥵然然 然然然然 🤤🥵🤤然然🥵然然 然然然然 🤤🥵🥵🤤🤤
🤤🥵
🥵然然然然 🥵🤤🥵🤤 然然然然🥵 🤤🥵🥵🤤🤤
🤤🥵
然然然然 🥵然然 然然然然然然 🤤🥵🤤🥵🤤
然然然然 🥵然然🤤 然然然然然然 🤤🥵🥵🥵🤤
然然然然 🥵然然🥵 然然然然然然 🤤🥵然然然然🥵🤤🤤🥵🤤🥵🤤然然
🥵🤤🤤 🥵🥵然然 然然然然🥵 🥵然然🤤🤤🤤
🤤🥵
🥵🤤🤤🥵🥵然然 然然然然🥵 🥵然然🤤  🤤🥵然然然然🥵🤤🥵然然🤤🥵🤤🥵 🥵🥵然然 🥵然然🥵🤤🤤
🤤🥵
🥵然然🤤🥵🥵🤤
🤤然然然然
🥵然然然然🥵🥵然然 然然然然🥵 🥵然然🤤🤤🤤
🤤🥵
🤤🥵然然然然🥵🤤🥵然然🥵🥵🥵 然然然然然然 🤤🥵然然然然🥵🤤🥵然然🤤🥵🤤然然
🤤然然然然
🥵🤤🤤🥵🥵然然 然然然然🥵 🥵然然🤤  🤤🥵然然然然🥵🤤🥵然然🥵🤤🥵 然然然然🥵 🥵然然🥵🤤🤤
🤤🥵
🥵然然然然然然然然然然
🤤然然然然
🥵然然然然🥵🥵然然 然然然然🥵 🥵然然🤤🤤🤤
🤤🥵
🤤🥵然然然然🥵🤤🥵然然🤤然然然然然然🤤 然然然然然然 🤤🥵然然然然🥵🤤🥵然然🥵🤤然然
🤤然然然然
🤤然然然然
🤤🥵然然然然🥵🤤🥵然然🥵🤤🥵 然然然然然然 🥵然然🥵🥵🤤
🤤🤤🤤🥵🤤🥵然然然然🥵然然 🤤🥵🤤然然🥵然然 🥵然然 然然然然然然🥵 然然然然🤤然然🤤然然🥵
🤤🤤🤤🥵🤤🥵然然然然🥵然然 🥵然然 然然然然🤤🤤 然然然然🤤然然然然🥵然然 🤤🥵🥵🤤然然🥵
🤤然然然然
🤤然然然然
然然然然 然然然然🤤🥵然然然然🥵然然
🤤🥵
然然然然 然然🤤然然🥵🤤然然然然🥵🤤🥵🤤🥵 然然然然然然 🤤🥵然然然然🥵🥵然然🥵然然然然🤤然然然然然然🥵然然然然🤤然然🤤然然🥵然然然然🤤然然🥵然然🥵然然然然🤤🤤然然然然🥵然然然然🤤🤤🤤然然🥵然然然然🤤🤤🥵然然🥵然然然然🤤🥵然然然然🥵然然然然🤤🥵🤤然然🥵然然然然🤤🥵🥵然然🥵然然然然
然然然然 🤤然然 然然然然然然 然然然然🥵🤤🥵🤤
🤤🥵然然🤤然然🥵然然 🤤然然🤤然然🥵
🤤🤤🤤🥵然然🤤然然🥵然然 然然然然🤤然然🥵然然 🤤然然然然然然然然🥵然然然然🤤然然🤤然然🥵
🤤🥵然然🤤然然🥵然然 🤤然然🤤然然🥵
🤤🤤然然 然然然然🤤🥵🤤
🤤然然然然
```

