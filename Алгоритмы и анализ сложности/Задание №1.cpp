/* Задача №1. (09.11.2021)
Ввести свой номер студ. билета и записать наоборот, так же найти 
минимальную и максимальную цифру в данном студ. билете*/
#include <iostream>
using namespace std;
int main()
{
    int const n = 10;
    int x, min, max, a[n];
    x = 1032205725; //студ билет
    for(int i = 0; i < n; i ++)
    {
        a[i] = x % 10;
        x = x / 10;
        cout << a[i];
    }
    max = min = a[0];
    for(int i = 1; i < n; i ++)
    {
        if(a[i] < min)
        {
            min = a[i];
        }
        if(a[i] > max)
        {
            max = a[i];
        }
    }
    cout << "\n max = " << max;
    cout << "\n min = " << min;
    return 0;
}