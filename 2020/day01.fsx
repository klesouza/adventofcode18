let readLines = sprintf "./inputs/%s.txt" >> System.IO.File.ReadLines

//let input = readLines "01"

type ResultSum = 
    | NotYet of (list<int> * int)
    | Found of int


let rec getSum (arr: list<int>) ie (i: int) =
    // printfn "%d %d" ie i
    let s = i + arr.[ie]
    if s > 2020 then getSum arr (ie - 1) i
    elif s = 2020 then Found (i * arr.[ie])
    else NotYet (arr, ie)

let day01 (arr: seq<string>) = 
    let filter2020 =
        arr
        |> Seq.map int
        |> Seq.sort
        |> Seq.filter ((>) 2020)

    let day01Array = Seq.toList filter2020
     
    filter2020
        |> Seq.map ((getSum) day01Array (day01Array.Length-1))
        |> Seq.pick (fun result ->
            match result with
                | NotYet _ -> None
                | Found v -> Some v
        )

let day01p2 (arr: seq<string>)  =
    let filter2020 =
        arr
        |> Seq.map int
        |> Seq.sort
        |> Seq.filter ((>) 2020)

    let day01Array = Seq.toList filter2020
    
    //Give up trying to make it more functional :|
    let mutable found = -1
    let mutable x = 0
    let mutable y = 1
    let mutable z = (day01Array.Length-1)
    while found = -1 do
        let s = day01Array.[x] + day01Array.[y] + day01Array.[z]
        if s > 2020 then z <- z - 1
        elif s < 2020 then
            if y = (z - 1) then x <- x+1
            else y <- y+1
        else found <- day01Array.[x] * day01Array.[y] * day01Array.[z]
    found

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


