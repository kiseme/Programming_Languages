use std::io;

struct Point {
    x: f64,
    y: f64,
}

#[allow(dead_code)]
struct Line {
    p1: Point,
    p2: Point,
}

const N: i32 = 5;

fn main() {

let mut Lines: Vec<Vec<f32>> = vec![];

  for j in 0..N{
    let mut points: Vec<f32> = vec![];
    println!("enter points x1,y1 x2,y2"); 
    let mut s = String::new(); 
    
    io::stdin().read_line(&mut s);
    let mut v: Vec<_> = s.split(|q| q == ',' || q == ' ' || q == '\n').collect(); 
    for i in 0..4 { 
      let num: f32 = v[i].trim().parse().expect("введите число"); 
      points.push(num); 
    }
    Lines.push(points);
  }
  
  for j in 1..Lines.len(){
  let A1: f32 = Lines[0][1] - Lines[0][3];
  let B1: f32 = Lines[0][2] - Lines[0][0];
  let A2: f32 = Lines[j][1] - Lines[j][3];
  let B2: f32 = Lines[j][2] - Lines[j][0];
  let C1: f32 = Lines[0][0] * Lines[0][3] - Lines[0][2] * Lines[0][1];
  let C2: f32 = Lines[j][0] * Lines[j][3] - Lines[j][2] * Lines[j][1];
    if A1*B2-A2*B1 != 0.0 {
      println!("пересеклось");
      let X: f32 = -((C1*B2)-(C2*B1))/((A1*B2)-(A2*B1));
      let Y: f32 = -((A1*C2)-(A2*C1))/((A1*B2)-(A2*B1));
    }
    println!("{:?}", Lines[j]); 
  }
}
