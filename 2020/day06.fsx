let day06 (arr: seq<string>) =
    seq {
        let mutable cSet = Set.empty<char>
        for x in arr do
            match x.Length with
            | 0 -> 
                yield cSet
                cSet <- Set.empty<char>
            | _ -> cSet <- x.ToCharArray() |> Set.ofArray |> (Set.union cSet)
        yield cSet
    }
    |> Seq.map Set.count
    |> Seq.sum


    
