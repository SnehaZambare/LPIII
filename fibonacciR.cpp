#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void non_recur(int n)
{
    int first = 0, second = 1;
    cout << first << " ";
    if (n == 1)
        return;
    while (n > 1)
    {
        cout << second << " ";
        int k = first + second;
        first = second;
        second = k;
        n--;
    }
}

void recur(int m)
{
    static int m1 = 0, m2 = 1, m3;
    if (m > 0)
    {
        m3 = m1 + m2;
        m1 = m2;
        m2 = m3;
        cout << m3 << " ";
        recur(m - 1);
    }
}

int main()
{
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Using non-recursive approach" << endl;
    non_recur(n);

    cout << "\nUsing recursive approach" << endl;
    vector<int> ans;
    if (n == 1)
    {
        cout << 0;
    }
    else if (n == 2)
    {
        cout << 0 << " " << 1;
    }
    else
    {
        cout << 0 << " " << 1 << " ";
        recur(n - 2);
    }
    return 0;
}