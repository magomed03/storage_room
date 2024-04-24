// Алгоритм поиска Эйлерова цикла в графе.
#include <algorithm>
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

// Класс для неориентированного графа
class Graph {
    int V; // Номер вершин
    list<int>* adj; // Динамический массив списков смежности
public:
    // Конструктор и деструктор
    Graph(int V)
    {
        this->V = V;
        adj = new list<int>[V];
    }
    ~Graph() { delete[] adj; }

    // Функции для добавления и удаления вершин
    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    void rmvEdge(int u, int v);

    // Методы для Эйлерова пути
    void printEulerTour();
    void printEulerUtil(int s);

    // Эта функция возвращает количество достижимых вершин
    // Из V делает DFS
    int DFSCount(int v, bool visited[]);

    // эта функция для проверки допустимости следующего ребра u-v
    bool isValidNextEdge(int u, int v);
};

/* Основная функция, печатающая Эйлер. Сначала онa находит вершину нечетной степени (если есть), затем
    printEulerUtil() чтобы напечатать путь */
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
    // Рекурсивно для всех вершин, смежных с этой вершиной
    list<int>::iterator i;
    for (i = adj[u].begin(); i != adj[u].end(); ++i) {
        int v = *i;

        // Если ребро u-v не удалено и оно является допустимым
        if (v != -1 && isValidNextEdge(u, v)) {
            cout << u << "-" << v << "  ";
            rmvEdge(u, v);
            printEulerUtil(v);
        }
    }
}

// Функция проверки того, может ли ребро u-v рассматриваться как следующее ребро
bool Graph::isValidNextEdge(int u, int v)
{
    // Ребро u-v будет доступин в одном из следующих двух ситуации

    // 1) Если v единственная смежная вершина u
    int count = 0;
    list<int>::iterator i;
    for (i = adj[u].begin(); i != adj[u].end(); ++i)
        if (*i != -1)
            count++;
    if (count == 1)
        return true;


    // 2.a) количество вершин, достижимых из u
    bool visited[V];
    memset(visited, false, V);
    int count1 = DFSCount(u, visited);

    // 2.b) удалим ребро (u, v) и после удаление ребра, мы подсчитаем вершины достижимые из u
    rmvEdge(u, v);
    memset(visited, false, V);
    int count2 = DFSCount(u, visited);

    // 2.c) Добавим ребро обратно в граф
    addEdge(u, v);

    // 2.d) If count1 is greater, then edge (u, v) is a
    // bridge
    return (count1 > count2) ? false : true;
}

// эта функция удалит ребро u-v из графа. Она удаляет ребро, заменяя значение соседней вершины на -1.
void Graph::rmvEdge(int u, int v)
{
    //  Найдем u в списке смежности v и заменим его на -1
    list<int>::iterator iv
        = find(adj[u].begin(), adj[u].end(), v);
    *iv = -1;

    // Найдем u в списке смежности v и заменим его на -1
    list<int>::iterator iu
        = find(adj[v].begin(), adj[v].end(), u);
    *iu = -1;
}

// DFS основанная функция для подсчета достижимых вершин из v
int Graph::DFSCount(int v, bool visited[])
{
    // Отметить текущий узел как посещенный
    visited[v] = true;
    int count = 1;

    // Рекурсивно для всех вершин, смежных с этой вершиной
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (*i != -1 && !visited[*i])
            count += DFSCount(*i, visited);

    return count;
}

// Основная функция кода
int main()
{
    // Сначала создадим и протестируем график, показанные выше
    // Фигура
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
