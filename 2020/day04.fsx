open System.Text.RegularExpressions

let mandatoryItemsSet = Set.ofList [
    "byr"
    "iyr"
    "eyr"
    "hgt"
    "hcl"
    "ecl"
    "pid"
    // "cid"
]
let between a b v = v >= a && v <= b
let (|Regex|_|) pattern input =
        let m = Regex.Match(input, pattern)
        if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
        else None
let validate x v = 
    match x with
    | "byr" -> between 1920 2002 (int v )
    | "iyr" -> between 2010 2020 (int v )
    | "eyr" -> between 2020 2030 (int v )
    | "hgt" -> 
        match v with
        | Regex @"^([\d]{3})cm$" [hgt] -> between 150 193 (int hgt)
        | Regex @"^([\d]{2})in$" [hgt] -> between 59 76 (int hgt)
        | _ -> false
    | "hcl" -> Regex.IsMatch(v, @"^#[0-9a-f]{6}$")
    | "ecl" -> Set.contains v (Set.ofList ["amb"; "blu"; "brn"; "gry"; "grn"; "hzl"; "oth"])
    | "pid" -> Regex.IsMatch(v, @"^[\d]{9}$")
    | _ -> true


let day04 check (arr: seq<string>) =
    arr
    |> Seq.scan (fun (i, s) t -> 
        if Set.isEmpty s then (i, mandatoryItemsSet) //Avoid cid in last line
        else
        match t.Length with
            | 0 -> (i+1, mandatoryItemsSet)
            | _ -> (i, Set.difference s ((t.Split ' ' ) 
                                            |> Array.map (fun kv -> 
                                                let x = kv.Split ':'
                                                (x.[0], validate x.[0] x.[1])
                                            )
                                            |> Array.filter (fun (k, v) -> not check || v)
                                            |> Array.map (fun (k, v) -> k)
                                            |> Set.ofArray
                                        ))
    ) (0, mandatoryItemsSet)
    |> Seq.mapi (fun i (ix, s) -> (i, ix, s))
    |> Seq.filter (fun (i, ix, s) -> Set.isEmpty s)
    |> Seq.length
    
