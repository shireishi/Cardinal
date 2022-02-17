struct System {
    void error(const char* message) {
        printf("\033[38;2;{};{};{}m{}\033[m\n", 255, 0, 0, message);
    }
    void notify(const char* message) {
        printf("\033[38;2;{};{};{}m{}\033[m\n", 0, 255, 0, message);
    }
    void broadcast(const char* message) {
        printf("\033[38;2;{};{};{}m{}\033[m\n", 0, 255, 255, message);
    }
}