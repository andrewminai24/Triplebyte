function f(x){
    x *= 2;
    return function(y){
        y *= x;
        return function (z){
            return z * y;
        }
    }
}


let g = f(3)(4)(5);

console.log(g);
