/*
Hello this is a ractivity test
*/

#include <iostream>
#include <map>
using namespace std;

int main(){
    int userSelection;
    string userSelectionS;
    map<string, pair<int, string>> racks;

    racks.insert({"AR-29",{47,"Brocade 7450-48 OOB"}});
    racks.insert({"AR-29",{46,"Brocade 7450-48 OOB"}});

    cout << "Hello, and welcome to Racktivity \n";
    cout << "    What would you like to do?   \n";
    cout << "-------------------------------- \n";
    cout << "| 1) View rack                  | \n";
    cout << "-------------------------------- \n";
    //
    cin >> userSelection;

    userSelection = 0;
    if(userSelection == 1){
        cout << " What rack would you like to view\n";
        for (const auto &elem: racks)
            cout << elem.first << "\n";        
    }
    cout << "Format rack then row EX: (AR-29 48)\n";
    cin >> userSelectionS >> userSelection;
    //51
    //cout << racks[userSelectionS][userSelection] <<"\n";

}
