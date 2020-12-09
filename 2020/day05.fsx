let getBounds (bottom, top) action =
    match action with
    | 'F' | 'L' -> (bottom, bottom+(top-bottom)/2)
    | _ -> (1+bottom+(top-bottom)/2, top)


let day05 (arr: seq<string>) =
    arr
    |> Seq.map (fun seat ->
        let (row, _) = 
            seat
            |> Seq.take 7
            |> Seq.fold (getBounds) (0, 127)
        let (column, _) =
            seat
            |> Seq.skip 7
            |> Seq.fold (getBounds) (0, 7)

        row * 8 + column
    )
    |> Seq.max