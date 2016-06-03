// Hack around stdlib bug with C++14.
#include <initializer_list>  // force libstdc++ to include its config
#undef _GLIBCXX_HAVE_GETS    // correct broken config
// End hack.

#include "vector_algos.hpp"
#include <iostream>
#include <string>

std::vector<int> read_int_vector() {
    std::vector<int> result;
    int x;

    std::cout << "Enter as many numbers as you want:\n";

    while (true) {
        while (std::cin >> x)
            result.push_back(x);

        if (std::cin.eof())
            break;

        std::cin.clear();

        std::string s;
        std::getline(std::cin, s);

        std::cout << "Warning, ignoring: " << s << "\n";
    }

    std::cout << "End of file encountered, stopping input.\n";
    return result;
}

int sum(std::vector<int> v) {
    int total = 0;
    for (auto e : v)
        total += e;
    return total;
}

std::vector<int> filter_greater_than(std::vector<int> v, int x) {
    std::vector<int> result;
    for (auto e : v)
        if (e > x)
            result.push_back(e);
    return result;
}