let readLines = sprintf "./inputs/%s.txt" >> System.IO.File.ReadLines

//let input = readLines "01"

type ResultSum = 
    | NotYet of (list<int> * int)
    | Found of int


let rec getSum2 (arr: list<int>) ie (i: int) =
    // printfn "%d %d" ie i
    let s = i + arr.[ie]
    if s > 2020 then getSum2 arr (ie - 1) i
    elif s = 2020 then Found (i * arr.[ie])
    else NotYet (arr, ie)

let getSum3 result =
    // printfn "%A" result
    match result with
        | NotYet _ -> None
        | Found v -> Some v

let day01 (arr: seq<string>) = 
    let filter2020 =
        arr
        |> Seq.map int
        |> Seq.sort
        |> Seq.filter ((>) 2020)

    let day01Array = Seq.toList filter2020
     
    filter2020
        |> Seq.map ((getSum2) day01Array (day01Array.Length-1))
        |> Seq.pick getSum3

// printfn "%i" (day01 input)
// [ 
// "1721"
// "979"
// "366"
// "299"
// "675"
// "1456" ]
// |> day01
// |> printfn "%i"