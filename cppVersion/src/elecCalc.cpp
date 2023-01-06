#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <regex>

using namespace std;
namespace fs = std::filesystem;

void getDirScanDir(); // for some reason I have to declare before main too

int main(){
    getDirScanDir();
    return 0;
}

// The code below first scans the execution dir and then, using regex changes from the src to the scripts folder.
// On the other hand, the for loop read the name of each file and prints to console
// Pendiente de cambios:
// Cambiar src a la carpeta final en la que estará, o en su defecto camiar el regex_replace por un concat 'scripts'.
void getDirScanDir(){
    cout << "Current path is " << fs::current_path() << '\n'; // (1)
    
    string path = fs::current_path();
    path = regex_replace(path, regex("src"), "scripts");

    int menuNumber = 0;

    for (const auto & file : fs::directory_iterator(path)) {
        string f = file.path();
        f = regex_replace(f, regex(path + "/"), "");
        cout << ++menuNumber << ". " <<  f << endl;
    }
}
