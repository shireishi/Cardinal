#include <cstdio>

class System {
    System() { // Here the system class should recieve an instance of the client object to send broadcast messages
        return void;
    }
    public:
        void error(const char* message) {
            printf("\033[38;2;{};{};{}m{}\033[m\n", 255, 0, 0, message);
        }
        void notify(const char* message) {
            printf("\033[38;2;{};{};{}m{}\033[m\n", 255, 0, 0, message);
        }
        void broadcast(const char* message) {
            printf("\033[38;2;{};{};{}m{}\033[m\n", 255, 0, 0, message);
        }
    private:
        const char* _author = "Keys";
}