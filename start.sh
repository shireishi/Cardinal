if [[${@:2} = python]]; then
    builtin cd Python/src
    pythonw server.py
else
    builtin cd Rust/src
    rustc server.rs
    ./server
fi