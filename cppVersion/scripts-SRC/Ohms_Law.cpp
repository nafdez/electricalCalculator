#include <iostream>
using namespace std;

int voltageOhm(){
    int R, I;
    cout << "What is the resistance value?:" << endl;
    cin >> R;
    cout << "And the current value?" << endl;
    cin >> I;

    return R*I;
}
int resistanceOhm(){
    int V, I;
    cout << "What is the voltage value?:" << endl;
    cin >> V;
    cout << "And the current value?" << endl;
    cin >> I;

    return V/I;
}
int currentOhm(){
    int V, R;
    cout << "What is the voltage value?:" << endl;
    cin >> V;
    cout << "And the resistance value?" << endl;
    cin >> R;

    return V/R;
}

int main(){
    cout << "Do you want to calculate the voltage(1), the resistance(2), or the current(3)?: " << endl;

    int option;
    cin >> option;
    
    switch (option)
    {
    case 1:
        cout << "Your choice: Voltage\n" << endl;
        cout << voltageOhm() << " V" << endl;
        break;
    case 2:
        cout << "Your choice: Resistance\n" << endl;
        cout << resistanceOhm() << " R" << endl;
        break;
    case 3:
        cout << "Your choice: Current\n" << endl;
        cout << currentOhm() << " A" << endl;
        break;
    
    default:
        cout << "I\'m sorry, that option isn\'t ready yet" << endl;
        break;
    }

    return 0;
}
