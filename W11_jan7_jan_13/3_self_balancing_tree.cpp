/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

int safe_ht(node* root) {
    if(root == nullptr)
        return -1;
    else
        return root->ht;
}

node* insert(node* root, int val)
{
    // Recursive insert
    if(val < root->val) {
        if(root->left == nullptr)
            root->left = new node {val, nullptr, nullptr, 0};
        else
            root->left = insert(root->left, val);
    }
    else if(val > root->val) {
        if(root->right == nullptr)
            root->right = new node {val, nullptr, nullptr, 0};
        else
            root->right = insert(root->right, val);
    }
    root->ht = max(safe_ht(root->left), safe_ht(root->right)) + 1;

    // Solving unbalanced
    if(safe_ht(root->left) == safe_ht(root->right) + 2) {
        node* temp;
        // Left-Right Case
        if(safe_ht(root->left->left) == safe_ht(root->left->right) - 1) {
            temp = root->left;
            root->left = temp->right;
            temp->right = root->left->left;
            root->left->left = temp;
            root->left->left->ht = max(safe_ht(root->left->left->left), safe_ht(root->left->left->right)) + 1;
            root->left->ht = root->left->left->ht + 1;
        }
        // Left-Left Case
        temp = root;
        root = root->left;
        temp->left = root->right;
        root->right = temp;
        root->right->ht = max(safe_ht(root->right->left), safe_ht(root->right->right)) + 1;
        root->ht = max(root->left->ht, root->right->ht) + 1;
    }
    else if(safe_ht(root->left) == safe_ht(root->right) - 2) {
        node* temp;
        // Right-Left Case
        if(safe_ht(root->right->right) == safe_ht(root->right->left) - 1) {
            temp = root->right;
            root->right = temp->left;
            temp->left = root->right->right;
            root->right->right = temp;
            root->right->right->ht = max(safe_ht(root->right->right->right), safe_ht(root->right->right->left)) + 1;
            root->right->ht = root->right->right->ht + 1;
        }
        // Right-Right Case
        temp = root;
        root = root->right;
        temp->right = root->left;
        root->left = temp;
        root->left->ht = max(safe_ht(root->left->right), safe_ht(root->left->left)) + 1;
    }
    return root;
}