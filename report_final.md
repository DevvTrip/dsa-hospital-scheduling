# PBL Progress Report - Final

**Program and Branch Name:** B.Tech CSE (AI)

| Field | Details |
|---|---|
| Course Name | Data Structures and Algorithms - II |
| Course Code | BCSE0401 |
| Faculty Name | Mr Vikas Tripathi |
| Assignment Type | Individual Assignment |
| Student(s) Name | Devvrat Tripathi |
| ERP ID / Roll No. | 250133150078 |
| Team/Group No. | N/A (Individual Assignment) |
| Problem Statement / Project Title | Designing an Algorithmically Efficient Data Management and Processing System for an AI-Based Hospital Appointment Scheduling System |
| SDG(s) | SDG 3 - Good Health and Well-being |
| Reporting Month | Month 3 - Final |

## Student Declaration

I certify that this assignment is my own work, with all sources appropriately acknowledged. I understand that a 0% mark and further academic penalties may apply if the content is found to be plagiarised or inappropriately AI-generated.

Student Name & Signature(s): Devvrat Tripathi  
Date: ____________________

## 2. Student Details / Team Details

| S.No. | Student Name | ERP ID / Roll No. | Role / Contribution |
|---|---|---|---|
| 1 | Devvrat Tripathi | 250133150078 | All five modules: algorithm selection, C coding, testing and report writing |

## 3. Executive Summary

This assignment builds a hospital scheduling system with DSA-II concepts. My C program stores patients in a BST, queues them in a heap, finds shortest paths with Dijkstra, plans theatre time with knapsack DP, and packs free slots with backtracking. This gives fast lookup, urgent patients first, and better theatre use.

## 4. Introduction

Hospitals handle hundreds of appointments every day. If records are stored in plain lists, every search takes time proportional to the number of patients, and theatre plans are often made by hand. This course teaches better tools: trees, graphs, dynamic programming, backtracking and advanced indexing. I used one tool from each unit in a single C program. The aim is to show that the right data structure turns a slow manual process into a fast and clear one.

## 5. Problem Definition

Problem: manage hospital appointments and resources efficiently. Input: patients with ID, name, disease and severity (1 to 10), a campus map with 10 departments, 8 pending surgeries with durations and priorities, and leftover appointment requests. Output: instant patient lookup, an urgency-ordered queue, the fastest route between departments, a maximum-priority theatre plan for an 8-hour day, and an exact packing of a free slot. Users are reception staff, doctors and administrators. Constraints: sample data, C language, terminal only, no external libraries. Success means O(log n) search, correct shortest paths and optimal theatre use. The work supports SDG 3 (Good Health and Well-being).

## 6. Industry / Application Overview

Hospitals already use computers for this work. Big hospital systems store records in indexed databases, apps like Practo and Zocdoc book appointments, and ambulance services use shortest path searches for routing. These products are closed, so a student cannot see the data structures inside them. This project builds a small open version where each decision can be traced to one algorithm from the syllabus. That makes it useful for learning and easy to explain.

## 7. Module 1: Tree-Based Data Management (BST and Heap)

This module uses binary search trees, heaps and heap sort (Unit 1). A BST keeps smaller IDs on the left and larger ones on the right, so each comparison removes half of the remaining records. A heap keeps every parent larger than its children, so the most urgent patient sits at the root. I stored records in a BST keyed by ID, the queue in a max-heap by severity, and used heap sort for ordered printing. Output: Arjun Rao (severity 9) prints first, Neha Gupta (2) last. Lesson: a plain BST turns into a linked list if IDs arrive in order, so an AVL tree is safer at scale.

| Rank | Patient | Disease | Severity |
|---|---|---|---|
| 1 | Arjun Rao | Cardiac | 9 |
| 2 | Priya Singh | Fracture | 7 |
| 3 | Sara Khan | Asthma | 6 |

*Figure 1: First three pops of the heap appointment queue.*

## 8. Module 2: Graph Modeling and Network Optimization (Dijkstra)

This module applies graph modelling and Dijkstra's shortest path algorithm (Unit 2) [1][4]. Dijkstra settles the nearest unvisited department first and relaxes its neighbours, which is correct because all corridor times are positive. I modelled the campus as a weighted undirected graph with 10 departments and 14 corridors in an adjacency matrix, then ran Dijkstra for the fastest route between any two departments. Output: ER to OT costs 7 minutes through ICU, better than 8 on the direct corridor. Lesson: an adjacency matrix is easy to read for a small campus; BFS and DFS check connectivity, and Prim and Kruskal both give a 34-minute spanning tree for cabling.

| From | To | Cost | Route |
|---|---|---|---|
| ER | OT | 7 min | ER - ICU - OT |
| Reception | Cafeteria | 7 min | Reception - Pharmacy - Cafeteria |

*Figure 2: Key shortest path results from the program.*

## 9. Module 3: Dynamic Programming for Optimization (0/1 Knapsack)

This module uses 0/1 knapsack dynamic programming (Unit 3). DP fits this problem because the same smaller questions repeat: the best plan for 480 minutes is built from the best plans for smaller capacities. I treated each surgery as an item with duration as weight and priority as value. The table dp[i][c] holds the best priority using the first i surgeries within c minutes, and tracing back gives the chosen list. Output: six surgeries with total priority 41, using all 480 minutes. Greedy by priority per minute reaches only 39, so the DP plan wins. Lesson: DP runs in O(n x C) time and space. LCS fits symptom matching, resource allocation DP fits doctor distribution, and matrix chain multiplication does not fit this problem.

| Surgery | Duration (min) | Priority |
|---|---|---|
| Gallbladder removal | 120 | 9 |
| Angioplasty | 150 | 10 |
| Hernia repair | 75 | 7 |
| Tonsillectomy | 60 | 6 |
| Cataract | 45 | 5 |
| Biopsy | 30 | 4 |

*Figure 3: Chosen surgeries from the DP plan (priority 41, 480 min used).*

## 10. Module 4: Backtracking and Branch and Bound (Sum of Subsets)

This module applies backtracking over a state space tree (Unit 4). The algorithm builds a solution one request at a time. At each step it tries to include the request, and it drops that branch as soon as the sum crosses the target, so all 32 subsets are not checked. I used it to fill a free slot of 80 minutes from leftover requests {30, 45, 60, 20, 35}, and it found {45, 35}. Lesson: the worst case is still exponential, but pruning keeps it fast for short lists. I also compared related problems: shift rostering like N-Queens, graph coloring to send overlapping surgeries to different theatres, and branch and bound with a reduced cost matrix for the ambulance route [2].

```
                 [ ] sum = 0
                /         \
          take 45           skip 45
          sum = 45          sum = 0
         /        \             ...
    take 35      skip 35
    sum = 80     sum = 45
   FOUND {45, 35}
```

*Figure 4: Search tree for the 80-minute slot (pruned branches not shown).*

## 11. Module 5: Advanced Data Structures (B+ Tree)

This module studies B+ trees and advanced heaps (Unit 5) [5]. In a B+ tree all records sit in the leaves and internal nodes hold only separators; the leaves are linked, so a range query walks from one leaf to the next instead of returning to the root. I compared Red-Black trees, B-Trees, B+ trees, binomial heaps and Fibonacci heaps for a hospital storing lakhs of records. The B+ tree suits the patient index best because it matches disk blocks and handles date ranges. My worked example indexes 12 records by appointment day, and the query for days 8 to 20 returns 6 records in one leaf scan. For queues, Fibonacci heaps give O(1) amortized decrease-key for Dijkstra at large scale, while a binary heap is enough here.

```
                     [ 20 ]
                   /        \
          [ 8 | 12 ]          [ 25 ]
         /    |    \          /    \
  [1 3 5]  [8 10]  [12 15 18]  [20 22]  [25 28]
```

*Figure 5: B+ tree indexing 12 records by appointment day (linked leaves).*

## 12. Final Integrated Solution / Testing and Validation

The C program ties all five modules together in one terminal menu. When a patient is added, the record goes into both the BST and the heap. The queue always pops the most urgent patient, Dijkstra answers route questions, the knapsack planner prints the theatre list, and subset search fills a free slot. I tested each option on its own first and then together, with sample data and some wrong inputs. Missing IDs return not found, bad department numbers are rejected, and duplicate IDs are refused. The five main test cases are listed in Figure 6 and all results matched hand calculations. The source is standard C99 with no external libraries, so it compiles with gcc or any online C compiler.

| Test | Input | Expected | Actual | Status |
|---|---|---|---|---|
| 1. Search hit | ID 105 | Arjun Rao found | Found, severity 9 | Pass |
| 2. Search miss | ID 999 | Not found | Not found | Pass |
| 3. Shortest path | ER to OT | 7 min via ICU | 7 min via ICU | Pass |
| 4. DP vs greedy | 480 min, 8 surgeries | DP >= greedy | 41 vs 39 | Pass |
| 5. Slot packing | Target 80 | Exact subset | {45, 35} | Pass |

*Figure 6: Test case summary.*

## 13. Expected Benefits / Learning Outcomes

Benefits: staff can find a patient in O(log n) steps instead of scanning a register, urgent cases move ahead automatically, and the theatre plan uses the full day at the highest possible priority. Learning: I now know when a tree is needed and when a heap is enough, why DP beats greedy here, how pruning makes backtracking practical, and why large systems index records with B+ trees. I also practised writing and explaining complexity analysis for each module.

## 14. Challenges Faced

Some parts were harder than expected. Fitting five units into one small program forced me to pick one clear algorithm per unit instead of many half-done ones. I also learnt that a BST is fast only while it stays balanced, and my first heap test printed the wrong order because I compared severity in the wrong direction. I fixed it by checking the pop order against a sorted list. Fixed-size arrays and the missing GUI are known limits of this prototype, listed under future work.

## 15. Future Improvements

Next steps: replace the BST with an AVL or B+ tree, save records to a file or database, predict severity with machine learning, use real corridor distances, and add a simple GUI.

## 16. Conclusion

The project delivers a working hospital scheduling program in C that touches all five units of DSA-II. The BST registry and heap queue cover trees, Dijkstra handles routing, knapsack DP builds the theatre plan, backtracking packs free slots, and the report explains why a B+ tree is the right index at full scale. Every test passed. The biggest takeaway is that standard data structures solve real hospital problems well when each one is matched to the job it does best.

## 17. References

1. T. H. Cormen, C. E. Leiserson, R. L. Rivest and C. Stein, Introduction to Algorithms, 3rd ed. Cambridge, MA: MIT Press, 2009.
2. E. Horowitz, S. Sahni and S. Rajasekaran, Fundamentals of Computer Algorithms, 2nd ed. Hyderabad: Universities Press, 2008.
3. T. Cayirli and E. Veral, "Outpatient scheduling in health care: A review of literature," Production and Operations Management, vol. 12, no. 4, pp. 519-549, 2003.
4. GeeksforGeeks, "Dijkstra's Shortest Path Algorithm," 2026. [Online]. Available: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/. [Accessed: Oct. 28, 2026].
5. GeeksforGeeks, "Introduction of B+ Tree," 2026. [Online]. Available: https://www.geeksforgeeks.org/introduction-of-b-tree-2/. [Accessed: Oct. 28, 2026].
6. NPTEL, "Data Structures and Algorithms," IIT. [Online]. Available: https://nptel.ac.in/courses/106102064. [Accessed: Oct. 28, 2026].

## 18. Appendix (Source Code)

Full file: hospital_system.c. Compile: `gcc hospital_system.c -o hospital_system`.

```c
/*
    AI-Based Hospital Appointment Scheduling System
    DSA-II Individual Assignment (BCSE0401), terminal app, no GUI.

    Compile : gcc hospital_system.c -o hospital_system
    Run     : ./hospital_system      (Windows: hospital_system.exe)

    Unit 1 : BST patient registry + max-heap appointment queue + heap sort
    Unit 2 : Dijkstra shortest path on the hospital campus graph
    Unit 3 : 0/1 Knapsack DP for operation theatre slot allocation
    Unit 4 : Sum of subsets backtracking for exact free-slot packing
    Unit 5 : B+ tree indexing is discussed in the report.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATIENTS 100
#define N_NODES 10
#define INF 999999
#define MAX_SURG 8
#define MAX_CAP 480

typedef struct {
    int id;
    char name[30];
    char disease[30];
    int severity;
} Patient;

Patient patient_list[MAX_PATIENTS];
int patient_count = 0;

/* ================= Unit 1: BST patient registry ================= */
typedef struct BSTNode {
    Patient p;
    struct BSTNode *left, *right;
} BSTNode;
BSTNode *root = NULL;

BSTNode *bst_insert(BSTNode *node, Patient p) {
    if (node == NULL) {
        BSTNode *n = (BSTNode *)malloc(sizeof(BSTNode));
        n->p = p;
        n->left = NULL;
        n->right = NULL;
        return n;
    }
    if (p.id < node->p.id)
        node->left = bst_insert(node->left, p);
    else if (p.id > node->p.id)
        node->right = bst_insert(node->right, p);
    return node;
}

Patient *bst_search(BSTNode *node, int id) {
    while (node != NULL) {
        if (id == node->p.id)
            return &node->p;
        if (id < node->p.id)
            node = node->left;
        else
            node = node->right;
    }
    return NULL;
}

void bst_inorder(BSTNode *node) {
    if (node == NULL)
        return;
    bst_inorder(node->left);
    printf("   ID %-4d %-15s %-13s severity %d\n", node->p.id, node->p.name, node->p.disease, node->p.severity);
    bst_inorder(node->right);
}

/* ================= Unit 1: max-heap priority queue ================= */
void heap_push(Patient h[], int *size, Patient p) {
    int i = *size;
    h[i] = p;
    (*size)++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        Patient tmp;
        if (h[i].severity <= h[parent].severity)
            break;
        tmp = h[i];
        h[i] = h[parent];
        h[parent] = tmp;
        i = parent;
    }
}

Patient heap_pop(Patient h[], int *size) {
    Patient top = h[0];
    int i = 0;
    (*size)--;
    h[0] = h[*size];
    while (1) {
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        int big = i;
        Patient tmp;
        if (l < *size && h[l].severity > h[big].severity)
            big = l;
        if (r < *size && h[r].severity > h[big].severity)
            big = r;
        if (big == i)
            break;
        tmp = h[i];
        h[i] = h[big];
        h[big] = tmp;
        i = big;
    }
    return top;
}

/* ================= Unit 2: hospital campus graph + Dijkstra ================= */
char *nodes[N_NODES] = {"Reception", "OPD", "ER", "ICU", "OT",
                        "Pharmacy", "Pathology", "Radiology", "GeneralWard", "Cafeteria"};
int graph[N_NODES][N_NODES];

void init_graph() {
    int edges[][3] = {
        {0,1,3}, {0,2,5}, {0,5,4}, {1,6,6}, {1,7,7},
        {2,3,4}, {2,4,8}, {3,4,3}, {3,8,5}, {4,8,4},
        {6,5,5}, {7,5,6}, {8,9,2}, {5,9,3}
    };
    int m = sizeof(edges) / sizeof(edges[0]);
    int i, j;
    for (i = 0; i < N_NODES; i++)
        for (j = 0; j < N_NODES; j++)
            graph[i][j] = (i == j) ? 0 : INF;
    for (i = 0; i < m; i++) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        graph[u][v] = w;
        graph[v][u] = w;
    }
}

void dijkstra(int src, int dst) {
    int dist[N_NODES], prev[N_NODES], visited[N_NODES], path[N_NODES];
    int i, count, v, len = 0;
    for (i = 0; i < N_NODES; i++) {
        dist[i] = INF;
        prev[i] = -1;
        visited[i] = 0;
    }
    dist[src] = 0;
    for (count = 0; count < N_NODES; count++) {
        int u = -1, best = INF;
        for (i = 0; i < N_NODES; i++) {
            if (visited[i] == 0 && dist[i] < best) {
                best = dist[i];
                u = i;
            }
        }
        if (u == -1)
            break;
        visited[u] = 1;
        for (v = 0; v < N_NODES; v++) {
            if (visited[v] == 0 && graph[u][v] != INF) {
                int nd = dist[u] + graph[u][v];
                if (nd < dist[v]) {
                    dist[v] = nd;
                    prev[v] = u;
                }
            }
        }
    }
    if (dist[dst] == INF) {
        printf("   No path found.\n");
        return;
    }
    for (v = dst; v != -1; v = prev[v])
        path[len++] = v;
    printf("   Shortest path %s -> %s = %d minutes\n", nodes[src], nodes[dst], dist[dst]);
    printf("   Route: ");
    for (i = len - 1; i >= 0; i--)
        printf("%s%s", nodes[path[i]], (i == 0) ? "\n" : " -> ");
}

/* ================= Unit 3: 0/1 knapsack DP for OT slots ================= */
typedef struct {
    char name[25];
    int duration;
    int priority;
} Surgery;

void knapsack_ot() {
    Surgery s[MAX_SURG] = {
        {"Appendectomy", 90, 8}, {"Knee replacement", 180, 10},
        {"Gallbladder removal", 120, 9}, {"Cataract", 45, 5},
        {"Hernia repair", 75, 7}, {"Angioplasty", 150, 10},
        {"Biopsy", 30, 4}, {"Tonsillectomy", 60, 6}
    };
    int dp[MAX_SURG + 1][MAX_CAP + 1];
    int i, c;
    memset(dp, 0, sizeof(dp));
    for (i = 1; i <= MAX_SURG; i++) {
        for (c = 0; c <= MAX_CAP; c++) {
            dp[i][c] = dp[i - 1][c];
            if (s[i - 1].duration <= c) {
                int take = dp[i - 1][c - s[i - 1].duration] + s[i - 1].priority;
                if (take > dp[i][c])
                    dp[i][c] = take;
            }
        }
    }
    printf("   OT capacity = 480 min (8 hours)\n");
    printf("   Max total priority (DP) = %d\n", dp[MAX_SURG][MAX_CAP]);
    printf("   Selected surgeries:\n");
    c = MAX_CAP;
    for (i = MAX_SURG; i >= 1; i--) {
        if (dp[i][c] != dp[i - 1][c]) {
            printf("   - %-20s %4d min, priority %d\n", s[i - 1].name, s[i - 1].duration, s[i - 1].priority);
            c = c - s[i - 1].duration;
        }
    }
}

/* ================= Unit 4: sum of subsets backtracking ================= */
int found;

void subset_search(int a[], int n, int idx, int sum, int target, int chosen[], int len) {
    int i;
    if (found == 1)
        return;
    if (sum == target) {
        printf("   Subset found: {");
        for (i = 0; i < len; i++) {
            if (i > 0)
                printf(", ");
            printf("%d", chosen[i]);
        }
        printf("} = %d min\n", target);
        found = 1;
        return;
    }
    if (idx == n || sum > target)
        return;
    chosen[len] = a[idx];
    subset_search(a, n, idx + 1, sum + a[idx], target, chosen, len + 1);
    subset_search(a, n, idx + 1, sum, target, chosen, len);
}

/* ================= sample data and menu ================= */
void load_sample_data() {
    Patient list[] = {
        {104, "Aman Verma", "Fever", 3}, {101, "Priya Singh", "Fracture", 7},
        {107, "Rohit Das", "Migraine", 4}, {103, "Sara Khan", "Asthma", 6},
        {109, "Kunal Mehta", "Diabetes", 5}, {102, "Neha Gupta", "Cough", 2},
        {105, "Arjun Rao", "Cardiac", 9}
    };
    int n = sizeof(list) / sizeof(list[0]);
    int i;
    for (i = 0; i < n; i++) {
        root = bst_insert(root, list[i]);
        patient_list[patient_count] = list[i];
        patient_count++;
    }
}

void add_patient() {
    Patient p;
    printf("   Enter patient ID, name, disease, severity (1-10):\n   ");
    scanf("%d %s %s %d", &p.id, p.name, p.disease, &p.severity);
    if (bst_search(root, p.id) != NULL) {
        printf("   Patient ID already exists.\n");
        return;
    }
    root = bst_insert(root, p);
    patient_list[patient_count] = p;
    patient_count++;
    printf("   Patient added to registry and appointment queue.\n");
}

void show_heap(int sort_only) {
    Patient h[MAX_PATIENTS];
    int size = 0, i;
    for (i = 0; i < patient_count; i++)
        heap_push(h, &size, patient_list[i]);
    if (sort_only == 1)
        printf("   Heap sort by severity, O(n log n):\n");
    else
        printf("   Appointment queue, most urgent first:\n");
    while (size > 0) {
        Patient p = heap_pop(h, &size);
        if (sort_only == 1)
            printf("   ID %-4d %-15s severity %d\n", p.id, p.name, p.severity);
        else
            printf("   ID %-4d %-15s %-13s severity %d\n", p.id, p.name, p.disease, p.severity);
    }
}

void dijkstra_menu() {
    int src, dst, i;
    printf("   Departments:\n");
    for (i = 0; i < N_NODES; i++)
        printf("   %d = %s\n", i, nodes[i]);
    printf("   Enter source and destination indices: ");
    scanf("%d %d", &src, &dst);
    if (src < 0 || src >= N_NODES || dst < 0 || dst >= N_NODES) {
        printf("   Invalid department index.\n");
        return;
    }
    dijkstra(src, dst);
}

void sum_of_subsets_demo() {
    int durations[] = {30, 45, 60, 20, 35};
    int chosen[5];
    found = 0;
    printf("   Free slot = 80 min, leftover requests = {30, 45, 60, 20, 35}\n");
    subset_search(durations, 5, 0, 0, 80, chosen, 0);
    if (found == 0)
        printf("   No exact subset found.\n");
}

int main() {
    int choice;
    init_graph();
    load_sample_data();
    do {
        printf("\n===== AI-Based Hospital Appointment Scheduling System =====\n"
               "1. Show all patients (BST inorder)\n"
               "2. Search patient by ID\n"
               "3. Add new patient\n"
               "4. Show appointment queue (heap)\n"
               "5. Heap sort patients by severity\n"
               "6. Shortest path between departments (Dijkstra)\n"
               "7. OT slot allocation (0/1 knapsack DP)\n"
               "8. Pack free slot exactly (sum of subsets)\n"
               "9. Exit\nChoice: ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            printf("   Patients in BST, inorder (sorted by ID):\n");
            bst_inorder(root);
            break;
        case 2: {
            int id;
            printf("   Enter patient ID: ");
            scanf("%d", &id);
            Patient *p = bst_search(root, id);
            if (p != NULL)
                printf("   Found: ID %d, %s, %s, severity %d\n", p->id, p->name, p->disease, p->severity);
            else
                printf("   Patient not found.\n");
            break;
        }
        case 3: add_patient(); break;
        case 4: show_heap(0); break;
        case 5: show_heap(1); break;
        case 6: dijkstra_menu(); break;
        case 7: knapsack_ot(); break;
        case 8: sum_of_subsets_demo(); break;
        case 9: printf("   Exiting.\n"); break;
        default: printf("   Invalid choice, try again.\n");
        }
    } while (choice != 9);
    return 0;
}
```