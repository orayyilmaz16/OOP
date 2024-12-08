#include <iostream>

using std::string;
using namespace std;

class Vehicle{
    public:
        string manufacturer;
    

};

int main(void){
    
    Vehicle item1 = Vehicle();
    item1.manufacturer = "TOGG";
    std::cout << "Vehicle " << item1.manufacturer << std::endl; 


    return 0;
}