use compare::{Compare, natural};
use std::cmp::Ordering::{Less, Equal, Greater};

fn hash(mut data: Vec<String>) -> String {
    println!("{:?}", data);
    let comparison_string: String = String::from("Never gonna give you up");
    let cmp = natural();
    if cmp.compares_eq(data, comparison_string) {
        println!("Hello world");
    }
    comparison_string
}

fn main() {
    let test: Vec<String> = vec![String::from("I dont know what you want from me")];
    let returned: String = hash(test);
    println!("{:?}", returned);
}