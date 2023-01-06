#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <regex>
#include <cstdlib>

using namespace std;
namespace fs = std::filesystem;

// The code below first scans the execution dir and then, using regex changes from the src to the scripts folder.
// On the other hand, the for loop read the name of each file and prints to console
// Pendiente de cambios:
// Cambiar src a la carpeta final en la que estará, o en su defecto camiar el regex_replace por un concat 'scripts'.
string scriptSelector()
{
    string path = fs::current_path().string();
    path = regex_replace(path, regex("src"), "scripts");

    int menuNumber = 0;
    vector<string> files;

    for (const auto &file : fs::directory_iterator(path))
    {
        files.push_back(file.path().string());
        string fileWithoutPath = regex_replace(files.at(menuNumber), regex(path + "/"), "");
        cout << ++menuNumber << ". " << fileWithoutPath << endl;
    }

    cout << "\nWhich program do you want to run?" << endl;

    int option;

    cin >> option;
    option = option - 1;

    return regex_replace(files.at(option), regex(path + "/"), "");
}

void scriptLauncher(string filePath)
{
    filePath = filePath.insert(0, "./");
    system(("cd ../scripts && ./" + filePath).c_str());
    cout << "hola";
}

int main()
{
    cout << "Hello! Welcome to this shitty program!\nDo you need some help?\nYou have these options:\n"
         << endl;
    scriptLauncher(scriptSelector());
    return 0;
}
