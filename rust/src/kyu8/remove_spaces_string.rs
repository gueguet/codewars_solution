// https://www.codewars.com/kata/57eae20f5500ad98e50002c5/solutions/rust

pub fn no_space(x : String) -> String{
  return x.split_whitespace().collect();
}

pub fn main() {
    no_space("ohla que tal".to_string());
}