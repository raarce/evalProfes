#include <vector>
#include <list>
#include <iostream>
using namespace std;

const int QTY = 100000;

void insert_vector() {
  vector<int> V;

  for(int i=0; i<QTY; i++)
    V.insert(V.begin(), rand());
}

void insert_list() {
  list<int> L;

  for(int i=0; i<QTY; i++)
    L.insert(L.begin(), rand());
}

void insert_list() {
  list<int> L;

  for(int i=0; i<QTY; i++)
    L.insert(L.begin(), rand());
}


int main() {
  insert_list();
  //insert_vector();
}
