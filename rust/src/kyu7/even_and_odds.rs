pub fn evens_and_odds(n: u64) -> String {
    if n%2 == 0 {
        return format!("{:b}", n);
    }
    else {
        return format!("{:x}", n);
    }
}


pub fn main() {
    evens_and_odds(63);
}


