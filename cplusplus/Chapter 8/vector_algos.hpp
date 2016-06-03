#ifndef VECTOR_ALGOS_HPP
#define VECTOR_ALGOS_HPP

#include <vector>

std::vector<int> read_int_vector();

int sum(std::vector<int> v);
std::vector<int> filter_greater_than(std::vector<int> v, int x);

inline int average(std::vector<int> v) {
    if (v.empty())
        return 0;
    int size = v.size();
    return sum(v)/size;
}

#endif