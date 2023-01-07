#include "src-headers/ElectricalCalculator.h"

using namespace std;
namespace fs = std::filesystem;

string SplitFilename(const string str)
{
    size_t found = str.find_last_of("/\\");
    return str.substr(found + 1);
}

// The code below first scans the execution dir and then, using regex changes from the src to the scripts folder.
// On the other hand, the for loop read the name of each file and prints to console
// Pendiente de cambios:
// Cambiar src a la carpeta final en la que estará, o en su defecto camiar el regex_replace por un concat 'scripts'.
string scriptSelector(string SystemName, string path)
{
    int menuNumber = 0;
    vector<string> files;

    for (const auto &file : fs::directory_iterator(path))
    {
        files.push_back(file.path().string());
        string fileWithoutPath = SplitFilename(files.at(menuNumber));
        cout << ++menuNumber << ". " << fileWithoutPath << endl;
    }

    cout << "\nWhich program do you want to run?" << endl;

    int option;

    cin >> option;
    option = option - 1;

    string filePath;

    if (SystemName == "Windows")
    {
        filePath = (files.at(option) + "/" + SplitFilename(files.at(option)) + ".exe");
    }
    else if (SystemName == "Linux")
    {
        filePath = (files.at(option) + "/" + SplitFilename(files.at(option)));
    }

    return filePath;
}

void scriptLauncher(string filePath)
{
#ifdef __linux__
    system(("chmod +x " + filePath + " && cd ../scripts/Linux && ./" + SplitFilename(filePath)).c_str());
#elif _WIN32
    system((filePath).c_str());
#endif
}

int main()
{

    string path = fs::current_path().string();
#ifdef __linux__
#define SO "Linux"
    cout << "Your SO: " << SO << endl;
    cout << "Hello! Welcome to this shitty program!\nDo you need some help?\nYou have these options:\n"
         << endl;
    path = regex_replace(path, regex("src"), "scripts");
    scriptLauncher(scriptSelector("Linux", path));
#elif _WIN32
#define SO "Windows"
    cout << "Your SO: " << SO << endl;
    cout << "Hello! Welcome to this shitty program!\nDo you need some help?\nYou have these options:\n"
         << endl;
    path = path + "\\scripts";
    scriptLauncher(scriptSelector("Windows", path));
#endif
    return 0;
}
