fn hash(mut data: Vec<String>) -> String {
    println!("{:?}", data);
    String::from("hello world")
}

fn main() {
    let test: Vec<String> = vec![String::from("I dont know what you want from me")];
    let returned: String = hash(test);
    println!("{:?}", returned);
}