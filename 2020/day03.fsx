   
let day03b (arr: seq<string>) r d =
    arr
    |> Seq.mapi (fun i x -> 
        if i = 0 then 0
        elif i % d <> 0 then 0
        else (if x.[((r*( (i/d))) % x.Length)] = '#' then 1 else 0)
    )
    |> Seq.sum

let day03 (arr: seq<string>) = day03b arr 3 1

let day03p2 (arr: seq<string>) =
    [
        (1, 1)
        (3, 1)
        (5, 1)
        (7, 1)
        (1, 2)
    ]
    |> Seq.map (fun (r, d) -> uint64 (day03b arr r d))
    |> Seq.fold (*) (uint64 1 )
    // |> Seq.iter (printfn "%d")