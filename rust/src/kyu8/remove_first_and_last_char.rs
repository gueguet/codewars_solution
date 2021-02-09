// https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/rust

pub fn remove_char(s: &str) -> String {
    
    let testyoyo : String = s.to_string();
    let slice = &testyoyo[1..testyoyo.len()-1];
    let res : String = slice.to_string();
    return res;

}


pub fn main() {
    remove_char("ohla");
}


// on line answer
// s[1..s.len() - 1].to_string()