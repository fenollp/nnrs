use std::env;

fn sigmoid (x: f64) -> f64 {
   1 / (1 + exp(-x))
}

fn sigmoid_prime (x: f64) -> f64 {
   x * (1f64 - x)
}

#[test]
fn it_works() {
}
