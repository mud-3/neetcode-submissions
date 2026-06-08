class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int val) : val(val), next(nullptr) {}
    ListNode(int val, ListNode* next) : val(val), next(next) {}
};
class LinkedList {
private:
    ListNode* head;
    ListNode* tail;
public:
    LinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    int get(int index) {
        ListNode* Node = head;

        for (int i = 0; i < index; i++) {
            if (!Node->next) {
                return -1;
            }
            Node = Node->next;
        }

        return Node->val;
    }

    void insertHead(int val) {
        if (head->val == -1) {
            head = new ListNode(val);
            tail = new ListNode(val);
        } else {
            head = new ListNode(val, head);
        }
    }
    
    void insertTail(int val) {
        if (tail->val == -1) {
            tail = new ListNode(val);
            head = new ListNode(val);
        } else {
            ListNode* Node = head;

            while(Node->next) {
                Node = Node->next;
            }

            Node->next = new ListNode(val);
            tail = new ListNode(val);
        }
    }

    bool remove(int index) {
        ListNode* Node = head;
        ListNode* previous = nullptr;

        for (int i = 0; i < index; i++) {
            if (!Node->next) {
                return false;
            }
            previous = Node;
            Node = Node->next;
        }
        if (!previous) {
            if (head->val == -1) {
                return false;
            }
            head = head->next;
        } else {
            previous->next = Node->next;
            delete Node;
        }
        return true;
    }

    vector<int> getValues() {
        vector<int> list;
        ListNode* Node = head;
        while (Node) {
            if (head->val == -1) {
                break;
            }
            list.push_back(Node->val);
            Node = Node->next;
        }
        return list;
    }
};
