class DynamicArray {
private:
    int* list;
    int max_size;
    int size;

public:
    DynamicArray(int capacity) {
        max_size = capacity;
        size = 0;
        list = new int[max_size];
    }

    int get(int i) {
        return list[i];
    }

    void set(int i, int n) {
        list[i] = n;
    }

    void pushback(int n) {
        if (size == max_size) {
            resize();
        }
        list[size] = n;
        size ++;
    }

    int popback() {
        size --;
        return list[size];
    }

    void resize() {
        max_size *= 2;
        int* new_list = new int[max_size];

        for (int i = 0; i < size; i++) {
            new_list[i] = list[i];
        }

        delete[] list;
        list = new_list;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return max_size;
    }
};
