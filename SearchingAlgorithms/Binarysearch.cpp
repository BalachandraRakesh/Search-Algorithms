#include <iostream>
#include <string>
#include <vector>
using namespace std;

//Binary Search Algorithm

int Binary_Search(vector<int>vect,int key,int high,int low){
    while(low <= high){
        int mid = low + (high - low)/2;
        if(vect[mid] == key){
            return  mid;
        }
        else if(vect[mid] < key){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    return low-1;
}
int main()
{
    vector<int> vect = {1,2,3,4,5,6,7,8,9,10,11,13,14,15};
    int k = 12;
    cout << Binary_Search(vect,k,vect.size()-1,0)<<endl;
    
}