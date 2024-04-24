// �������� ������ �������� ����� � �����.
#include <algorithm>
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

// ����� ��� ������������������ �����
class Graph {
    int V; // ����� ������
    list<int>* adj; // ������������ ������ ������� ���������
public:
    // ����������� � ����������
    Graph(int V)
    {
        this->V = V;
        adj = new list<int>[V];
    }
    ~Graph() { delete[] adj; }

    // ������� ��� ���������� � �������� ������
    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    void rmvEdge(int u, int v);

    // ������ ��� �������� ����
    void printEulerTour();
    void printEulerUtil(int s);

    // ��� ������� ���������� ���������� ���������� ������
    // �� V ������ DFS
    int DFSCount(int v, bool visited[]);

    // ��� ������� ��� �������� ������������ ���������� ����� u-v
    bool isValidNextEdge(int u, int v);
};

/* �������� �������, ���������� �����. ������� ��a ������� ������� �������� ������� (���� ����), �����
    printEulerUtil() ����� ���������� ���� */
void Graph::printEulerTour()
{

    int u = 0;
    for (int i = 0; i < V; i++)
        if (adj[i].size() & 1) {
            u = i;
            break;
        }

    printEulerUtil(u);
    cout << endl;
}

void Graph::printEulerUtil(int u)
{
    // ���������� ��� ���� ������, ������� � ���� ��������
    list<int>::iterator i;
    for (i = adj[u].begin(); i != adj[u].end(); ++i) {
        int v = *i;

        // ���� ����� u-v �� ������� � ��� �������� ����������
        if (v != -1 && isValidNextEdge(u, v)) {
            cout << u << "-" << v << "  ";
            rmvEdge(u, v);
            printEulerUtil(v);
        }
    }
}

// ������� �������� ����, ����� �� ����� u-v ��������������� ��� ��������� �����
bool Graph::isValidNextEdge(int u, int v)
{
    // ����� u-v ����� �������� � ����� �� ��������� ���� ��������

    // 1) ���� v ������������ ������� ������� u
    int count = 0;
    list<int>::iterator i;
    for (i = adj[u].begin(); i != adj[u].end(); ++i)
        if (*i != -1)
            count++;
    if (count == 1)
        return true;


    // 2.a) ���������� ������, ���������� �� u
    bool visited[V];
    memset(visited, false, V);
    int count1 = DFSCount(u, visited);

    // 2.b) ������ ����� (u, v) � ����� �������� �����, �� ���������� ������� ���������� �� u
    rmvEdge(u, v);
    memset(visited, false, V);
    int count2 = DFSCount(u, visited);

    // 2.c) ������� ����� ������� � ����
    addEdge(u, v);

    // 2.d) If count1 is greater, then edge (u, v) is a
    // bridge
    return (count1 > count2) ? false : true;
}

// ��� ������� ������ ����� u-v �� �����. ��� ������� �����, ������� �������� �������� ������� �� -1.
void Graph::rmvEdge(int u, int v)
{
    //  ������ u � ������ ��������� v � ������� ��� �� -1
    list<int>::iterator iv
        = find(adj[u].begin(), adj[u].end(), v);
    *iv = -1;

    // ������ u � ������ ��������� v � ������� ��� �� -1
    list<int>::iterator iu
        = find(adj[v].begin(), adj[v].end(), u);
    *iu = -1;
}

// DFS ���������� ������� ��� �������� ���������� ������ �� v
int Graph::DFSCount(int v, bool visited[])
{
    // �������� ������� ���� ��� ����������
    visited[v] = true;
    int count = 1;

    // ���������� ��� ���� ������, ������� � ���� ��������
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (*i != -1 && !visited[*i])
            count += DFSCount(*i, visited);

    return count;
}

// �������� ������� ����
int main()
{
    // ������� �������� � ������������ ������, ���������� ����
    // ������
    Graph g1(11);
    g1.addEdge(1, 5);
    g1.addEdge(1, 8);
    g1.addEdge(2, 3);
    g1.addEdge(2, 4);
    g1.addEdge(2, 6);
    g1.addEdge(2, 7);
    g1.addEdge(3, 5);
    g1.addEdge(4, 11);
    g1.addEdge(6, 7);
    g1.addEdge(6, 8);
    g1.addEdge(6, 9);
    g1.addEdge(7, 8);
    g1.addEdge(7, 10);
    g1.addEdge(8, 9);
    g1.addEdge(10, 11);
    g1.printEulerTour();

    return 0;
}
