#include <iostream>

using namespace std;

#define SIZE 26

class trie_node {
 public:
  trie_node *child[SIZE];
  trie_node() : 
};

class trie {
    typedef struct trie_node_s {
        struct trie_node_s *child[SIZE];
    } trie_node_t;

 private:
    trie_node_t *root_;
    void destroy_ (trie_node_t *root) {
        if (root == NULL) {
            return root;
        }
        for (int i = 0; i < SIZE; i++) {
            destroy_(root->child[i]);
        }
        delete root;
    }
 public:
    trie() : root_(NULL) {}
    ~trie() { destroy_(root_); }
    int insert(string s);
    int search(string s);
    int remove(string s);
}

int
trie::insert (string s)
{
    trie_node_t *cur;
    if (!root_) {
        root_ = new trie_node_t;
    }
    cur = root;
    for (auto ch : s) {
        unsigned c = ch-'a';
        if (!cur->child[c]) {
            cur->child[c] = new trie_node_t;
        }


    }
}

