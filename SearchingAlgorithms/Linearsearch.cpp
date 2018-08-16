#include <iostream>
#include <string>
#include <vector>
//Linear Search Algorithm
int Linear_Search(std::vector<int> v,int key){
    for (int i = 0; i < v.size(); i++){
        if(v[i] == key){
            return i;
        }
    }
    return -1;
}

int main()
{
    std::vector<int> vect = {1,5,3,67,3,9,56,789,765,12,23,43,65,89};
    int k = 12;
    std::cout << Linear_Search(vect,k)<<std::endl;
    
}