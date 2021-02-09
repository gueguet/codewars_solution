// https://www.codewars.com/kata/563e320cee5dddcf77000158/train/rust

pub fn get_average(marks: &[f32]) -> f32 {
    let sum: f32 = Iterator::sum(marks.iter());
    let avg: f32 = sum / (marks.len() as f32);

    return avg.trunc();
}


pub fn main() {
    get_average(&[1., 5., 87., 45., 8., 8.]);
}