using namespace std;
class Solution {
private:
    stack<int> numStack;

public:
    int calculate(int num1, int num2, string sign) {
        if (sign == "+") {
            return num1 + num2;
        }
        if (sign == "-") {
            return num1 - num2;
        }
        if (sign == "*") {
            return num1 * num2;
        }
        return num1 / num2;
    }

    bool isOperator(string token) {
        return (token == "+" or token == "-" or token == "*" or token == "/");
    }

    int evalRPN(vector<string>& tokens) {
        for (string token : tokens) {
            if (isOperator(token)) {
                int num1 = numStack.top();
                numStack.pop();
                int num2 = numStack.top();
                numStack.pop();
                numStack.push(calculate(num2, num1, token));
            } else {
                numStack.push(stoi(token));
            }
        }
        return numStack.top();
    }
};