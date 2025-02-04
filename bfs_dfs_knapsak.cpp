#include <bits/stdc++.h>
using namespace std;

struct Node {
    int index;
    int total_weight;
    int total_benefit;
    vector<int> items;
};

const int max_w = 420;
const int num_items = 11;
vector<int> benefit = {20, 40, 50, 36, 26, 64, 54, 18, 46, 28, 25};
vector<int> weight = {15, 32, 60, 80, 43, 120, 77, 6, 93, 35, 37};

void print_solution(const string& method, int max_benefit, const vector<int>& combination) {
    cout << method << " Result:\n";
    cout << "Max benefit: " << max_benefit << endl;
    cout << "Items: ";
    for (int item : combination) {
        cout << item + 1 << " ";
    }
    cout << "\nTotal weight: ";
    int total_w = 0;
    for (int item : combination) {
        total_w += weight[item];
    }
    cout << total_w << endl;
    cout << "Benefits: ";
    int total_b = 0;
    for (int item : combination) {
        total_b += benefit[item];
    }
    cout << total_b << endl << endl;
}

void dfs() {
    stack<Node> st;
    Node start = {-1, 0, 0, {}};
    st.push(start);
    int max_benefit = 0;
    vector<int> best_combination;
    
    while (!st.empty()) {
        Node head = st.top();
        st.pop();
        int next_index = head.index + 1;
        
        if (next_index >= num_items) {
            if (head.total_benefit > max_benefit) {
                max_benefit = head.total_benefit;
                best_combination = head.items;
            }
            continue;
        }
        
        //  exclude 
        Node exclude = {next_index, head.total_weight, head.total_benefit, head.items};
        st.push(exclude);
        
        // include 
        int new_weight = head.total_weight + weight[next_index];
        if (new_weight <= max_w) {
            Node include = head;
            include.index = next_index;
            include.total_weight = new_weight;
            include.total_benefit = head.total_benefit + benefit[next_index];
            include.items.push_back(next_index);
            st.push(include);
        }
    }
    
    print_solution("DFS", max_benefit, best_combination);
}

void bfs() {
    queue<Node> q;
    Node start = {-1, 0, 0, {}};
    q.push(start);
    int max_benefit = 0;
    vector<int> best_combination;
    
    while (!q.empty()) {
        Node head = q.front();
        q.pop();
        int next_index = head.index + 1;
        
        if (next_index >= num_items) {
            if (head.total_benefit > max_benefit) {
                max_benefit = head.total_benefit;
                best_combination = head.items;
            }
            continue;
        }
        
        //  excluding item
        Node exclude = {next_index, head.total_weight, head.total_benefit, head.items};
        q.push(exclude);
        
        // including item
        int new_weight = head.total_weight + weight[next_index];
        if (new_weight <= max_w) {
            Node include = head;
            include.index = next_index;
            include.total_weight = new_weight;
            include.total_benefit = head.total_benefit + benefit[next_index];
            include.items.push_back(next_index);
            q.push(include);
        }
    }
    
    print_solution("BFS", max_benefit, best_combination);
}

int main() {
    dfs();
    bfs();
    return 0;
}