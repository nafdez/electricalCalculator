#include "Help.h"
using namespace std;

int main() {	
	cout << "Hi, to add extra calculator funcionalities, you only need to download or program your own scripts!." << endl;
	cout << "Once you have done this, only you need to do is to paste the file on the \'/scripts\' folder." << endl;
	cout << "Thanks for using this program!" << endl;

	#ifdef __linux__
	cout << endl;
    system("read");
    #elif _WIN32
	cout << endl;
    system("pause");
    #endif
}