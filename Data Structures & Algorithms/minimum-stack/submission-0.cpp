class MinStack {
private:
    std::stack<int> stack;
    std::stack<int> minStack;

public:
    MinStack() {}
    
    void push(int value) {
        stack.push(value);

        if (!minStack.empty()) {
            if (minStack.top() < value) {
                value = minStack.top();
            }
        }

        minStack.push(value);
    }
    
    void pop() {
        stack.pop();
        minStack.pop();
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
